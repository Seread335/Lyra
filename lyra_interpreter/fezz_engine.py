#!/usr/bin/env python3
"""
FEZZ EXECUTION ENGINE - Optimization Module for Lyra Interpreter
Version: 1.0
Purpose: Implement superscalar, out-of-order execution optimizations
Target: 2-3x performance improvement (IPC 1.9-3.1)
"""

import sys
from typing import List, Dict, Set, Tuple, Any
from enum import Enum

class InstructionType(Enum):
    """Types of instructions for FEZZ execution"""
    ARITHMETIC = 0  # +, -, *, /, %
    COMPARISON = 1  # ==, !=, <, >, <=, >=
    LOGICAL = 2     # &&, ||, !
    MEMORY = 3      # Load/Store (variable access)
    CONTROL = 4     # if, while, return, function call
    IO = 5          # print
    MISC = 6        # assignment, declaration

class DependencyType(Enum):
    """Types of instruction dependencies"""
    RAW = 0  # Read-After-Write (true dependency)
    WAR = 1  # Write-After-Read (anti-dependency)
    WAW = 2  # Write-After-Write (output dependency)
    NONE = 3  # No dependency

class FezzInstruction:
    """Represents an instruction for FEZZ execution"""
    def __init__(self, instr_type: InstructionType, operation: str, 
                 reads: Set[str], writes: Set[str], latency: int = 1):
        self.type = instr_type
        self.operation = operation
        self.reads = reads      # Variables read
        self.writes = writes    # Variables written
        self.latency = latency  # Execution latency
        self.ready_cycle = 0    # When instruction is ready
        self.issue_cycle = -1   # When it was issued
        self.complete_cycle = -1 # When it completed
        
    def __repr__(self):
        return f"FezzInstr({self.type.name}, {self.operation}, reads={self.reads}, writes={self.writes})"

class DependencyAnalyzer:
    """Analyzes dependencies between instructions"""
    
    def __init__(self):
        self.dependencies: Dict[int, List[Tuple[int, DependencyType]]] = {}
    
    def analyze(self, instructions: List[FezzInstruction]) -> Dict[int, List[Tuple[int, DependencyType]]]:
        """
        Find dependencies between instructions
        Returns: dependencies[i] = [(j, type), ...] where i depends on j
        """
        deps = {}
        
        for i in range(len(instructions)):
            deps[i] = []
            instr_i = instructions[i]
            
            # Check against all previous instructions
            for j in range(i):
                instr_j = instructions[j]
                dep_type = self._find_dependency(instr_j, instr_i)
                
                if dep_type != DependencyType.NONE:
                    deps[i].append((j, dep_type))
        
        self.dependencies = deps
        return deps
    
    def _find_dependency(self, producer: FezzInstruction, consumer: FezzInstruction) -> DependencyType:
        """Find dependency type between producer and consumer instruction"""
        
        # RAW: consumer reads what producer writes
        if consumer.reads & producer.writes:
            return DependencyType.RAW
        
        # WAR: consumer writes what producer reads
        if consumer.writes & producer.reads:
            return DependencyType.WAR
        
        # WAW: consumer writes what producer writes
        if consumer.writes & producer.writes:
            return DependencyType.WAW
        
        return DependencyType.NONE
    
    def get_critical_path_length(self, instructions: List[FezzInstruction]) -> int:
        """Calculate critical path length (longest dependency chain)"""
        if not instructions:
            return 0
        
        deps = self.analyze(instructions)
        
        # Calculate earliest ready time for each instruction
        ready_times = [0] * len(instructions)
        
        for i in range(len(instructions)):
            max_time = 0
            for j, dep_type in deps[i]:
                # RAW dependency requires waiting for producer to complete
                if dep_type == DependencyType.RAW:
                    max_time = max(max_time, ready_times[j] + instructions[j].latency)
                # WAR and WAW can sometimes be scheduled sooner
                else:
                    max_time = max(max_time, ready_times[j])
            ready_times[i] = max_time
        
        # Critical path is max completion time
        return max([ready_times[i] + instructions[i].latency for i in range(len(instructions))])

class SuperscalarExecutor:
    """Superscalar execution window (6-wide issue)"""
    
    ISSUE_WIDTH = 6  # Can issue up to 6 instructions per cycle
    
    def __init__(self):
        self.dep_analyzer = DependencyAnalyzer()
        self.execution_log = []
    
    def execute(self, instructions: List[FezzInstruction]) -> Dict[str, Any]:
        """
        Execute instructions with superscalar + OoO capabilities
        Returns: execution statistics
        """
        if not instructions:
            return {
                'total_cycles': 0,
                'instructions_issued': 0,
                'ipc': 0.0,
                'parallelism_factor': 0.0
            }
        
        # Analyze dependencies
        deps = self.dep_analyzer.analyze(instructions)
        
        # Find independent instruction groups
        independent_groups = self._find_independent_groups(instructions, deps)
        
        # Execute with superscalar
        total_cycles = self._execute_superscalar(instructions, deps, independent_groups)
        
        # Calculate performance metrics
        ipc = len(instructions) / max(total_cycles, 1)
        parallelism_factor = min(len(independent_groups) / self.ISSUE_WIDTH, 1.0)
        
        return {
            'total_cycles': total_cycles,
            'instructions_issued': len(instructions),
            'ipc': ipc,
            'parallelism_factor': parallelism_factor,
            'speedup': 1.0 / max(ipc / 1.0, 1.0),  # vs baseline 1 IPC
            'independent_groups': len(independent_groups)
        }
    
    def _find_independent_groups(self, instructions: List[FezzInstruction], 
                                deps: Dict[int, List[Tuple[int, DependencyType]]]) -> List[List[int]]:
        """Find groups of independent instructions that can execute in parallel"""
        groups = []
        issued = set()
        
        while len(issued) < len(instructions):
            current_group = []
            current_group_vars = set()  # Variables used in current group
            
            # Try to find up to ISSUE_WIDTH independent instructions
            for i in range(len(instructions)):
                if i in issued:
                    continue
                
                # Check if this instruction can be issued
                can_issue = True
                
                # Check dependencies
                for j, dep_type in deps[i]:
                    if j not in issued and dep_type == DependencyType.RAW:
                        can_issue = False
                        break
                
                # Check for conflicts within group
                if can_issue:
                    # WAW and WAR within group are harder, check them
                    for prev_instr in current_group:
                        if instructions[i].writes & instructions[prev_instr].reads:
                            can_issue = False
                            break
                        if instructions[i].writes & instructions[prev_instr].writes:
                            can_issue = False
                            break
                
                if can_issue and len(current_group) < self.ISSUE_WIDTH:
                    current_group.append(i)
                    issued.add(i)
            
            if current_group:
                groups.append(current_group)
        
        return groups
    
    def _execute_superscalar(self, instructions: List[FezzInstruction], 
                            deps: Dict[int, List[Tuple[int, DependencyType]]],
                            groups: List[List[int]]) -> int:
        """Execute instructions and return total cycles"""
        # In superscalar execution, groups execute in parallel
        # Critical path dominates
        total_cycles = 0
        ready_times = [0] * len(instructions)
        
        for group in groups:
            group_max_time = 0
            
            for i in group:
                # Calculate when this instruction is ready
                ready_time = 0
                for j, dep_type in deps[i]:
                    if dep_type == DependencyType.RAW:
                        ready_time = max(ready_time, ready_times[j] + instructions[j].latency)
                
                ready_times[i] = ready_time
                group_max_time = max(group_max_time, ready_time)
            
            # Group completes after max latency in group
            max_latency = max([instructions[i].latency for i in group])
            total_cycles = max(total_cycles, group_max_time + max_latency)
        
        return total_cycles

class FezzOptimizer:
    """Main FEZZ optimizer class"""
    
    def __init__(self):
        self.executor = SuperscalarExecutor()
        self.stats = {}
    
    def optimize_ast(self, ast: Any) -> Tuple[Any, Dict[str, Any]]:
        """
        Analyze and optimize an AST for better execution
        Returns: (original_ast, optimization_stats)
        """
        # Extract instruction sequence from AST
        instructions = self._extract_instructions(ast)
        
        if not instructions:
            return ast, {'optimized': False, 'reason': 'No instructions to optimize'}
        
        # Execute with FEZZ
        exec_stats = self.executor.execute(instructions)
        
        # Store statistics
        self.stats = {
            'fezz_enabled': True,
            'ipc': exec_stats['ipc'],
            'speedup': exec_stats['speedup'],
            'parallelism_factor': exec_stats['parallelism_factor'],
            'independent_groups': exec_stats['independent_groups'],
            'instructions_analyzed': exec_stats['instructions_issued']
        }
        
        return ast, self.stats
    
    def _extract_instructions(self, ast: Any) -> List[FezzInstruction]:
        """Extract FezzInstructions from AST (simplified)"""
        # This is a simplified version - real version would traverse AST
        return []
    
    def get_stats(self) -> Dict[str, Any]:
        """Get optimization statistics"""
        return self.stats

# Helper function to create instructions from expressions
def create_instruction_from_expr(expr: str, reads: Set[str], writes: Set[str]) -> FezzInstruction:
    """Create a FEZZ instruction from an expression"""
    
    # Determine instruction type
    if any(op in expr for op in ['+', '-', '*', '/', '%']):
        instr_type = InstructionType.ARITHMETIC
        latency = 1 if '+' in expr or '-' in expr else 2  # MUL is 2-cycle
    elif any(op in expr for op in ['==', '!=', '<', '>', '<=', '>=']):
        instr_type = InstructionType.COMPARISON
        latency = 1
    elif any(op in expr for op in ['&&', '||', '!']):
        instr_type = InstructionType.LOGICAL
        latency = 1
    elif 'print' in expr:
        instr_type = InstructionType.IO
        latency = 3  # I/O is slower
    else:
        instr_type = InstructionType.MISC
        latency = 1
    
    return FezzInstruction(instr_type, expr, reads, writes, latency)

# Performance tracking
class PerformanceMonitor:
    """Track FEZZ performance metrics during execution"""
    
    def __init__(self):
        self.instructions_executed = 0
        self.cycles_simulated = 0
        self.cache_hits = 0
        self.cache_misses = 0
        self.branch_predictions = 0
        self.branch_mispredictions = 0
    
    def report(self) -> Dict[str, Any]:
        """Generate performance report"""
        ipc = self.instructions_executed / max(self.cycles_simulated, 1)
        cache_hit_rate = self.cache_hits / max(self.cache_hits + self.cache_misses, 1)
        branch_accuracy = self.branch_predictions / max(self.branch_predictions + self.branch_mispredictions, 1)
        
        return {
            'instructions_executed': self.instructions_executed,
            'cycles_simulated': self.cycles_simulated,
            'ipc': ipc,
            'cache_hit_rate': cache_hit_rate,
            'branch_prediction_accuracy': branch_accuracy,
            'speedup_vs_baseline': ipc / 1.0
        }
