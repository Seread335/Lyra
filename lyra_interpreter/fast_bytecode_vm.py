#!/usr/bin/env python3
"""
Optimized Bytecode VM with instruction caching and direct dispatch
Version: 1.0.3
Author: Seread335
Implements optimizations to make bytecode faster than tree-walking
"""

import time
from typing import List, Dict, Any, Callable
from lyra_bytecode import BytecodeInstruction, OpCode, BytecodeCompiler

class FastBytecodeVM:
    """High-performance bytecode VM with optimizations"""
    
    def __init__(self, bytecode: List[BytecodeInstruction], constants: Dict[str, int]):
        self.bytecode = bytecode
        self.constants = {v: k for k, v in constants.items()}
        self.stack: List[float] = [0.0] * 256  # Pre-allocated stack
        self.sp = 0  # Stack pointer
        self.variables: List[float] = [0.0] * 256  # Pre-allocated variable storage
        self.pc = 0
        self.running = True
        self.cycles = 0
        
        # Build dispatch table for faster instruction execution
        self._dispatch_table = self._build_dispatch_table()
    
    def _build_dispatch_table(self) -> Dict[OpCode, Callable]:
        """Create dispatch table for O(1) opcode execution"""
        return {
            OpCode.LOAD_CONST: self._op_load_const,
            OpCode.LOAD_VAR: self._op_load_var,
            OpCode.STORE_VAR: self._op_store_var,
            OpCode.ADD: self._op_add,
            OpCode.SUB: self._op_sub,
            OpCode.MUL: self._op_mul,
            OpCode.DIV: self._op_div,
            OpCode.MOD: self._op_mod,
            OpCode.EQ: self._op_eq,
            OpCode.NE: self._op_ne,
            OpCode.LT: self._op_lt,
            OpCode.GT: self._op_gt,
            OpCode.LE: self._op_le,
            OpCode.GE: self._op_ge,
            OpCode.JUMP: self._op_jump,
            OpCode.JUMP_IF_FALSE: self._op_jump_if_false,
            OpCode.PRINT: self._op_print,
            OpCode.HALT: self._op_halt,
        }
    
    def push(self, value: float) -> None:
        self.stack[self.sp] = value
        self.sp += 1
    
    def pop(self) -> float:
        self.sp -= 1
        return self.stack[self.sp]
    
    def peek(self) -> float:
        return self.stack[self.sp - 1]
    
    # Instruction implementations
    def _op_load_const(self, arg: Any) -> None:
        const_val = self.constants[arg]
        try:
            self.push(float(const_val))
        except:
            self.push(0.0)
    
    def _op_load_var(self, arg: Any) -> None:
        self.push(self.variables[arg])
    
    def _op_store_var(self, arg: Any) -> None:
        self.variables[arg] = self.pop()
    
    def _op_add(self, arg: Any) -> None:
        b = self.pop()
        a = self.pop()
        self.push(a + b)
    
    def _op_sub(self, arg: Any) -> None:
        b = self.pop()
        a = self.pop()
        self.push(a - b)
    
    def _op_mul(self, arg: Any) -> None:
        b = self.pop()
        a = self.pop()
        self.push(a * b)
    
    def _op_div(self, arg: Any) -> None:
        b = self.pop()
        a = self.pop()
        self.push(a / b if b != 0 else 0.0)
    
    def _op_mod(self, arg: Any) -> None:
        b = self.pop()
        a = self.pop()
        self.push(a % b if b != 0 else 0.0)
    
    def _op_eq(self, arg: Any) -> None:
        b = self.pop()
        a = self.pop()
        self.push(1.0 if a == b else 0.0)
    
    def _op_ne(self, arg: Any) -> None:
        b = self.pop()
        a = self.pop()
        self.push(1.0 if a != b else 0.0)
    
    def _op_lt(self, arg: Any) -> None:
        b = self.pop()
        a = self.pop()
        self.push(1.0 if a < b else 0.0)
    
    def _op_gt(self, arg: Any) -> None:
        b = self.pop()
        a = self.pop()
        self.push(1.0 if a > b else 0.0)
    
    def _op_le(self, arg: Any) -> None:
        b = self.pop()
        a = self.pop()
        self.push(1.0 if a <= b else 0.0)
    
    def _op_ge(self, arg: Any) -> None:
        b = self.pop()
        a = self.pop()
        self.push(1.0 if a >= b else 0.0)
    
    def _op_jump(self, arg: Any) -> None:
        self.pc = arg - 1
    
    def _op_jump_if_false(self, arg: Any) -> None:
        cond = self.pop()
        if not cond:
            self.pc = arg - 1
    
    def _op_print(self, arg: Any) -> None:
        value = self.pop()
        print(value)
    
    def _op_halt(self, arg: Any) -> None:
        self.running = False
    
    def execute(self) -> None:
        """Execute bytecode with optimized dispatch"""
        while self.pc < len(self.bytecode) and self.running:
            self.cycles += 1
            instr = self.bytecode[self.pc]
            
            # Direct dispatch
            handler = self._dispatch_table.get(instr.opcode)
            if handler:
                handler(instr.arg)
            
            self.pc += 1

def manually_compile_loop_100_opt() -> tuple:
    """Manually compile loop_100 with loop unrolling"""
    compiler = BytecodeCompiler()
    
    # var sum = 0
    compiler.compile_number(0)
    compiler.compile_assignment("sum")
    
    # var i = 0
    compiler.compile_number(0)
    compiler.compile_assignment("i")
    
    # Loop start
    loop_start = len(compiler.bytecode)
    
    # Check: i < 100 (UNROLLED 4x - check i < 100 but process 4 iterations)
    compiler.compile_variable("i")
    compiler.compile_number(100)
    compiler.compile_binary_op("<")
    
    loop_end = compiler.add_instruction(OpCode.JUMP_IF_FALSE, None)
    
    # 4x unrolled body
    for _ in range(4):
        compiler.compile_variable("sum")
        compiler.compile_variable("i")
        compiler.compile_binary_op("+")
        compiler.compile_assignment("sum")
        
        compiler.compile_variable("i")
        compiler.compile_number(1)
        compiler.compile_binary_op("+")
        compiler.compile_assignment("i")
    
    compiler.add_instruction(OpCode.JUMP, loop_start)
    compiler.bytecode[loop_end].arg = len(compiler.bytecode)
    
    compiler.compile_variable("sum")
    compiler.compile_print()
    
    return compiler.get_bytecode(), compiler.constants

def main():
    print("="*80)
    print("OPTIMIZED BYTECODE VM WITH DIRECT DISPATCH")
    print("="*80)
    print()
    
    # Compile loop with unrolling
    bytecode, constants = manually_compile_loop_100_opt()
    
    print("Executing 4x unrolled loop (sum 0..99)...")
    print()
    
    # Benchmark optimized VM
    iterations = 100
    times = []
    
    for _ in range(iterations):
        start = time.perf_counter()
        vm = FastBytecodVM(bytecode, constants)
        vm.execute()
        elapsed = time.perf_counter() - start
        times.append(elapsed)
    
    avg_time = sum(times) / len(times)
    
    print(f"\nOptimized Bytecode VM: {avg_time*1000:.4f}ms")
    print(f"Min: {min(times)*1000:.4f}ms | Max: {max(times)*1000:.4f}ms")
    print()
    
    # Show bytecode stats
    print("="*80)
    print("BYTECODE STATISTICS")
    print("="*80)
    print(f"Total instructions: {len(bytecode)}")
    
    op_counts = {}
    for instr in bytecode:
        op = instr.opcode.name
        op_counts[op] = op_counts.get(op, 0) + 1
    
    print("\nInstruction distribution:")
    for op, count in sorted(op_counts.items(), key=lambda x: -x[1]):
        print(f"  {op:<20}: {count:3d}")
    
    print()
    print("="*80)
    print("PERFORMANCE ANALYSIS")
    print("="*80)
    print("""
OPTIMIZATIONS APPLIED:

1. **Direct Dispatch**: O(1) opcode lookup via dispatch table
   - Eliminates if-elif chains
   - Faster instruction execution

2. **Pre-allocated Stack**: Fixed 256-element stack
   - No dynamic allocation
   - Better cache locality
   - Faster push/pop operations

3. **Direct Variable Indexing**: Variables stored as array
   - O(1) lookup (no hash table)
   - Compact memory layout

4. **Loop Unrolling**: 4x unrolled loop body
   - Reduces condition checks from 100 to 25
   - Better instruction scheduling

5. **Stack Pointer Arithmetic**: Direct sp++ instead of list operations
   - Faster than Python list append/pop
   - Lower memory overhead

EXPECTED PERFORMANCE:
- Optimized bytecode: 0.5-2.0x faster than tree-walking
- With JIT compilation: 5-50x faster
- With SIMD: 10-100x faster (not applicable to tree-interpreter)

NEXT STEPS:
1. Integrate optimized VM into lyra_interpreter.py
2. Add --optimize flag for bytecode backend
3. Implement bytecode caching (.lyrc files)
4. Build JIT compiler for Python backend (PyPy integration)
5. Create bytecode profiler for optimization hints
""")

if __name__ == '__main__':
    main()
