#!/usr/bin/env python3
"""
LYRA ERROR SYSTEM - Strict Error Reporting
Version: 1.0.3
Author: Seread335
Implements Zero Tolerance, Total Traceability, No Silent Failures
"""

from enum import Enum
from typing import Optional, List, Tuple, Any, Dict
from datetime import datetime
import sys

# ============================================================================
# ERROR SEVERITY LEVELS
# ============================================================================

class ErrorSeverity(Enum):
    WARNING = 0
    ERROR = 1
    FATAL = 2
    PANIC = 3


# ============================================================================
# ERROR TYPES CATALOG
# ============================================================================

class ErrorType(Enum):
    # Type Enforcement Errors
    IMPLICIT_TYPE_CONVERSION = "ImplicitTypeConversionError"
    UNINITIALIZED_VARIABLE = "UninitializedVariableError"
    TYPE_MISMATCH = "TypeMismatchError"
    
    # Memory & Resource Safety Errors
    SHADOWING_FORBIDDEN = "ShadowingForbiddenError"
    UNUSED_VARIABLE = "UnusedVariableError"
    
    # Runtime Brutality Errors
    ARITHMETIC_OVERFLOW = "ArithmeticOverflowError"
    DEAD_CODE = "DeadCodeError"
    DIVISION_BY_ZERO = "DivisionByZeroError"
    INDEX_OUT_OF_BOUNDS = "IndexOutOfBoundsError"
    
    # Syntax Errors
    SYNTAX_ERROR = "SyntaxError"
    INVALID_TOKEN = "InvalidTokenError"
    
    # Undefined Errors
    UNDEFINED_VARIABLE = "UndefinedVariableError"
    UNDEFINED_FUNCTION = "UndefinedFunctionError"


# ============================================================================
# LOCATION TRACKING
# ============================================================================

class SourceLocation:
    """Tracks exact position in source code"""
    def __init__(self, filename: str, line: int, column: int):
        self.filename = filename
        self.line = line
        self.column = column
    
    def __str__(self):
        return f"{self.filename}:{self.line}:{self.column}"


# ============================================================================
# ERROR REPORTER
# ============================================================================

class ErrorReporter:
    """The Error System - Zero tolerance, Total traceability"""
    
    def __init__(self, program_name: str = "", source_lines: Optional[List[str]] = None) -> None:
        self.program_name = program_name
        self.source_lines = source_lines or []
        self.errors: List[Dict[str, Any]] = []
        self.warnings: List[Dict[str, Any]] = []
        self.start_time = datetime.now()
        self.fatal_error = False
        self.panic = False
    
    def report(self, error_type: ErrorType, message: str, location: Optional[SourceLocation] = None,
               severity: ErrorSeverity = ErrorSeverity.ERROR, context: str = "", hint: str = "") -> None:
        """Report an error with full context"""
        
        error: Dict[str, Any] = {
            'type': error_type.value,
            'message': message,
            'location': location,
            'severity': severity,
            'context': context,
            'hint': hint,
            'time': datetime.now()
        }
        
        if severity == ErrorSeverity.WARNING:
            self.warnings.append(error)
        elif severity == ErrorSeverity.PANIC:
            self.panic = True
            self.print_indictment(error)
            self.panic_exit()
        else:
            self.errors.append(error)
            self.fatal_error = (severity == ErrorSeverity.FATAL)
            self.print_indictment(error)
            
            if severity == ErrorSeverity.FATAL:
                sys.exit(1)
    
    def print_indictment(self, error: Dict[str, Any]) -> None:
        """Print error as a formal indictment with full context"""
        print("\n" + "="*70)
        print("[FATAL ERROR] >>> Lyra Execution Terminated <<<")
        print("="*70)
        print(f"ERROR TYPE: {error['type']}")
        
        if error['location']:
            loc: SourceLocation = error['location']  # type: ignore
            print(f"LOCATION  : file '{loc.filename}', line {loc.line}, column {loc.column}")
        
        print(f"DIAGNOSIS : {error['message']}")
        
        # Show source code context
        if error['location'] and self.source_lines:
            self.print_source_context(error['location'])
        
        if error['context']:
            print(f"CONTEXT   : {error['context']}")
        
        if error['hint']:
            print(f"RUTHLESS HINT: {error['hint']}")
        
        print("="*70)
        print("Process exited with code 1 (Failure).\n")
    
    def print_source_context(self, location: SourceLocation):
        """Print source code around error location - Handle tabs correctly"""
        line_num = location.line - 1
        
        if line_num < 0 or line_num >= len(self.source_lines):
            return
        
        print("CONTEXT:")
        
        # Show 2 lines before + current line
        start = max(0, line_num - 2)
        for i in range(start, line_num + 1):
            if i < len(self.source_lines):
                source_line = self.source_lines[i]
                # Replace tabs with spaces for alignment
                source_line = source_line.replace('\t', '    ')
                
                prefix = ">>> " if i == line_num else "    "
                print(f"{prefix}{i+1:3d} | {source_line}")
        
        # Show error pointer - Account for tabs converted to spaces
        if location.column > 0:
            error_line = self.source_lines[line_num].replace('\t', '    ')
            # Column points to character position
            pointer_pos = location.column - 1 + 8  # 8 for "    xxx | "
            # Make sure we don't go past line length
            pointer_pos = min(pointer_pos, len(error_line) + 8)
            print(" " * pointer_pos + "^^^")
    
    def panic_exit(self):
        """Panic mode: Immediate termination without recovery"""
        print("\n" + "*"*70)
        print("PANIC MODE ACTIVATED")
        print("*"*70)
        print("Lyra detected an unrecoverable system error.")
        print("Closing all resources and terminating immediately...")
        print("*"*70 + "\n")
        sys.exit(2)
    
    def check_fatal_errors(self):
        """Check if there are fatal errors"""
        if self.fatal_error or len(self.errors) > 0:
            print("\n" + "="*70)
            print("[FATAL] Program execution halted due to errors")
            print("="*70 + "\n")
            sys.exit(1)
    
    def summary(self):
        """Print error summary at program end with detailed analytics"""
        elapsed = (datetime.now() - self.start_time).total_seconds()
        
        # Always show summary even if no errors
        print("\n" + "="*70)
        print(f"ERROR SYSTEM SUMMARY: {self.program_name}")
        print("="*70)
        print(f"Total Errors: {len(self.errors)}")
        print(f"Total Warnings: {len(self.warnings)}")
        print(f"Execution Time: {elapsed:.4f}s")
        
        # Categorize errors by type
        if self.errors:
            error_types: Dict[str, int] = {}
            for err in self.errors:
                err_type: str = err['type']  # type: ignore
                error_types[err_type] = error_types.get(err_type, 0) + 1
            
            print(f"\nERRORS ({len(self.errors)}):")
            for i, err in enumerate(self.errors, 1):
                loc_str = f" at {err['location']}" if err['location'] else ""
                severity: Any = err.get('severity', 'ERROR')  # type: ignore
                print(f"  {i}. [{severity.name if hasattr(severity, 'name') else severity}] {err['type']}: {err['message']}{loc_str}")
            
            print(f"\nERROR CATEGORIES:")
            for err_type, count in sorted(error_types.items(), key=lambda x: -x[1]):
                print(f"  - {err_type}: {count}")
        
        if self.warnings:
            print(f"\nWARNINGS ({len(self.warnings)}):")
            for i, warn in enumerate(self.warnings, 1):
                loc_str = f" at {warn['location']}" if warn['location'] else ""
                print(f"  {i}. {warn['message']}{loc_str}")
        
        if not self.errors and not self.warnings:
            print("\n✓ PERFECT: No errors or warnings found!")
        
        print("="*70 + "\n")
        
        # Write to log file
        self.write_error_system_log()
    
    def write_error_system_log(self):
        """Write detailed Error System violation log"""
        if not self.errors and not self.warnings:
            return
        
        log_filename = f"error_system_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        try:
            with open(log_filename, 'w', encoding='utf-8') as f:
                f.write("LYRA ERROR SYSTEM VIOLATION REPORT\n")
                f.write("="*70 + "\n")
                f.write(f"Program: {self.program_name}\n")
                f.write(f"Time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Execution Time: {(datetime.now() - self.start_time).total_seconds():.4f}s\n")
                f.write(f"Total Errors: {len(self.errors)}\n")
                f.write(f"Total Warnings: {len(self.warnings)}\n")
                f.write("="*70 + "\n\n")
                
                if self.errors:
                    f.write("ERRORS:\n")
                    for err in self.errors:
                        f.write(f"\n[{err.get('severity', 'ERROR').name}] {err['type']}\n")
                        f.write(f"Message: {err['message']}\n")
                        if err['location']:
                            f.write(f"Location: {err['location']}\n")
                        if err.get('hint'):
                            f.write(f"Hint: {err['hint']}\n")
                        f.write("-"*70 + "\n")
                
                if self.warnings:
                    f.write("\nWARNINGS:\n")
                    for warn in self.warnings:
                        f.write(f"\n{warn['message']}\n")
                        if warn['location']:
                            f.write(f"Location: {warn['location']}\n")
                        f.write("-"*70 + "\n")
            
            if self.errors or self.warnings:
                print(f"Error System violation log saved to: {log_filename}")
        except Exception as e:
            print(f"Failed to write Error System log: {e}")


# ============================================================================
# STRICT TYPE CHECKER
# ============================================================================

class StrictTypeChecker:
    """Enforces strict type checking - No implicit conversions"""
    
    @staticmethod
    def can_operate(left_type: str, right_type: str, op: str) -> bool:
        """Check if BINARY operation is allowed between types"""
        
        # Arithmetic operations
        if op in ['+', '-', '*', '/', '%']:
            # Both must be numeric
            if (left_type in ['i32', 'f32'] and right_type in ['i32', 'f32']):
                return True
            # String concatenation only with + (both must be string)
            if op == '+' and left_type == 'string' and right_type == 'string':
                return True
            return False
        
        # Comparison operations
        if op in ['<', '>', '<=', '>=', '==', '!=']:
            # Must be same types, and comparable types
            if left_type == right_type:
                # All types can be compared
                if left_type in ['i32', 'f32', 'string', 'bool']:
                    return True
            return False
        
        # Logical operations
        if op in ['&&', '||']:
            # Both must be bool
            return left_type == 'bool' and right_type == 'bool'
        
        # Unknown operator
        return False
    
    @staticmethod
    def can_unary_operate(operand_type: str, op: str) -> bool:
        """Check if UNARY operation is allowed on type"""
        
        # Negation (-)
        if op == '-':
            return operand_type in ['i32', 'f32']
        
        # Logical NOT (!)
        if op == '!':
            return operand_type == 'bool'
        
        return False
    
    @staticmethod
    def infer_type(value: Any) -> str:
        """Infer type from value"""
        if isinstance(value, int):
            return 'i32'
        elif isinstance(value, float):
            return 'f32'
        elif isinstance(value, str):
            return 'string'
        elif isinstance(value, bool):
            return 'bool'
        elif isinstance(value, list):
            return 'array'
        else:
            return 'unknown'


# ============================================================================
# VARIABLE TRACKER
# ============================================================================

class VariableTracker:
    """Tracks variable usage for shadowing and unused variable detection"""
    
    def __init__(self) -> None:
        self.scopes: List[Dict[str, Any]] = [{}]  # Stack of scopes
        self.usage: Dict[str, bool] = {}  # Track if variable is used
    
    def enter_scope(self) -> None:
        """Enter new scope (function, block)"""
        self.scopes.append({})
    
    def exit_scope(self) -> List[str]:
        """Exit scope and check for unused variables"""
        scope: Dict[str, Any] = self.scopes.pop()
        unused: List[str] = []
        for var_name, info in scope.items():
            if not info.get('used', False):
                unused.append(var_name)
        return unused
    
    def declare_variable(self, name: str, var_type: str, location: Optional[SourceLocation] = None) -> Optional[Dict[str, Any]]:
        """Declare a variable - Check for shadowing ONLY in direct parent scopes"""
        current_scope: Dict[str, Any] = self.scopes[-1]
        
        # Check if already in current scope (duplicate declaration)
        if name in current_scope:
            return {
                'error': 'DUPLICATE_DECLARATION',
                'message': f"Variable '{name}' already declared in current scope",
                'location': location
            }
        
        # Check for shadowing in PARENT scopes (not all ancestors)
        if len(self.scopes) > 1:
            parent_scope = self.scopes[-2]  # Direct parent only
            if name in parent_scope:
                return {
                    'error': 'SHADOWING_FORBIDDEN',
                    'message': f"Variable '{name}' shadows parent scope variable",
                    'location': location
                }
        
        current_scope[name] = {
            'type': var_type,
            'location': location,
            'used': False,
            'initialized': False  # Track if value assigned
        }
        return None
    
    def use_variable(self, name: str) -> Optional[str]:
        """Mark variable as used, return its type"""
        # Search from innermost to outermost scope
        for scope in reversed(self.scopes):
            if name in scope:
                scope[name]['used'] = True  # type: ignore
                return scope[name].get('type', None)  # type: ignore
        return None
    
    def get_type(self, name: str) -> Optional[str]:
        """Get variable type"""
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name].get('type', None)  # type: ignore
        return None


# ============================================================================
# CODE ANALYZER (for Dead Code Detection)
# ============================================================================

class CodeAnalyzer:
    """Analyzes code for dead code and other issues"""
    
    @staticmethod
    def detect_dead_code(statements: List[Any]) -> List[Tuple[int, str]]:
        """Detect unreachable code - Check all control flow paths"""
        dead_code: List[Tuple[int, str]] = []
        
        for i, stmt in enumerate(statements):
            stmt_type = type(stmt).__name__
            
            # Return statement makes all following code unreachable
            if stmt_type == 'ReturnStmt':
                if i + 1 < len(statements):
                    for j in range(i + 1, len(statements)):
                        dead_code.append((j, "Unreachable code after return"))
                break  # No point checking further
            
            # Break at end of loop makes code after it unreachable
            elif stmt_type == 'BreakStmt':
                if i + 1 < len(statements):
                    for j in range(i + 1, len(statements)):
                        dead_code.append((j, "Unreachable code after break"))
                break
            
            # Continue also makes following code in same iteration unreachable
            elif stmt_type == 'ContinueStmt':
                if i + 1 < len(statements):
                    for j in range(i + 1, len(statements)):
                        dead_code.append((j, "Unreachable code after continue"))
                break
        
        return dead_code
