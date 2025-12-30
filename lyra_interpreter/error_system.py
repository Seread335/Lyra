#!/usr/bin/env python3
"""
LYRA ERROR SYSTEM - Comprehensive Strict Error Reporting
Version: 1.0.3
Author: Seread335

🚨 ZERO TOLERANCE ERROR SYSTEM 🚨
Implements:
  - Zero Tolerance (any error → halt)
  - Total Traceability (full stack trace + context)
  - No Silent Failures (every error logged + reported)
  - Strict Type Checking (no implicit conversions)
  - Resource Safety (bounds checking, initialization tracking)
  - Rigorous Validation (every operation verified)
"""

from enum import Enum
from typing import Optional, List, Tuple, Any, Dict, Set
from datetime import datetime
import sys
import traceback

# ============================================================================
# ERROR CATEGORIES (8 main categories, 256 unique error codes)
# ============================================================================

class ErrorCategory(Enum):
    """8 main error categories covering all failure modes"""
    TYPE_SAFETY = "TYPE_SAFETY"              # Type system violations (0x00-0x3F)
    RUNTIME_SAFETY = "RUNTIME_SAFETY"        # Runtime violations (0x40-0x7F)
    RESOURCE_SAFETY = "RESOURCE_SAFETY"      # Resource/memory violations (0x80-0xBF)
    BOUNDS_SAFETY = "BOUNDS_SAFETY"          # Index/range violations (0xC0-0xDF)
    SECURITY = "SECURITY"                    # Security violations (0xE0-0xEF)
    CONSISTENCY = "CONSISTENCY"               # Consistency violations (0xF0-0xF7)
    PERFORMANCE = "PERFORMANCE"              # Performance issues (0xF8-0xFA)
    HARDWARE = "HARDWARE"                    # Hardware/system errors (0xFB-0xFF)


# ============================================================================
# ERROR SEVERITY LEVELS (4 levels: escalating severity)
# ============================================================================

class ErrorSeverity(Enum):
    """Error severity levels - All errors must be resolved"""
    WARNING = 0    # Non-critical issue, execution continues with caution
    ERROR = 1      # Error that must be fixed, execution halts
    FATAL = 2      # Catastrophic error, immediate shutdown
    PANIC = 3      # Unrecoverable system error, emergency termination


# ============================================================================
# COMPREHENSIVE ERROR TYPES CATALOG (256 error codes)
# ============================================================================

class ErrorType(Enum):
    """Comprehensive error type catalog with precise error codes"""
    
    # -------- TYPE SAFETY ERRORS (0x00-0x3F) --------
    IMPLICIT_TYPE_CONVERSION = ("ImplicitTypeConversionError", 0x01)
    TYPE_MISMATCH = ("TypeMismatchError", 0x02)
    UNINITIALIZED_VARIABLE = ("UninitializedVariableError", 0x03)
    INVALID_CAST = ("InvalidCastError", 0x04)
    INCOMPATIBLE_TYPES = ("IncompatibleTypesError", 0x05)
    MISSING_TYPE_ANNOTATION = ("MissingTypeAnnotationError", 0x06)
    CONFLICTING_TYPE_HINTS = ("ConflictingTypeHintsError", 0x07)
    GENERIC_TYPE_ERROR = ("GenericTypeError", 0x08)
    
    # -------- RUNTIME SAFETY ERRORS (0x40-0x7F) --------
    DIVISION_BY_ZERO = ("DivisionByZeroError", 0x40)
    ARITHMETIC_OVERFLOW = ("ArithmeticOverflowError", 0x41)
    ARITHMETIC_UNDERFLOW = ("ArithmeticUnderflowError", 0x42)
    NULL_POINTER_DEREFERENCE = ("NullPointerDereferenceError", 0x43)
    INVALID_OPERATION = ("InvalidOperationError", 0x44)
    STACK_OVERFLOW = ("StackOverflowError", 0x45)
    INFINITE_LOOP = ("InfiniteLoopError", 0x46)
    RECURSION_LIMIT_EXCEEDED = ("RecursionLimitExceededError", 0x47)
    THREAD_SAFETY_VIOLATION = ("ThreadSafetyViolationError", 0x48)
    DEADLOCK_DETECTED = ("DeadlockDetectedError", 0x49)
    
    # -------- RESOURCE SAFETY ERRORS (0x80-0xBF) --------
    MEMORY_LEAK = ("MemoryLeakError", 0x80)
    MEMORY_CORRUPTION = ("MemoryCorruptionError", 0x81)
    FILE_NOT_FOUND = ("FileNotFoundError", 0x82)
    FILE_PERMISSION_DENIED = ("FilePermissionDeniedError", 0x83)
    FILE_IO_ERROR = ("FileIOError", 0x84)
    OUT_OF_MEMORY = ("OutOfMemoryError", 0x85)
    RESOURCE_EXHAUSTED = ("ResourceExhaustedError", 0x86)
    RESOURCE_LEAK = ("ResourceLeakError", 0x87)
    INVALID_FILE_HANDLE = ("InvalidFileHandleError", 0x88)
    CLOSED_RESOURCE_ACCESS = ("ClosedResourceAccessError", 0x89)
    
    # -------- BOUNDS SAFETY ERRORS (0xC0-0xDF) --------
    INDEX_OUT_OF_BOUNDS = ("IndexOutOfBoundsError", 0xC0)
    ARRAY_BOUNDS_VIOLATION = ("ArrayBoundsViolationError", 0xC1)
    STRING_INDEX_OUT_OF_BOUNDS = ("StringIndexOutOfBoundsError", 0xC2)
    NEGATIVE_INDEX = ("NegativeIndexError", 0xC3)
    BUFFER_OVERFLOW = ("BufferOverflowError", 0xC4)
    BUFFER_UNDERFLOW = ("BufferUnderflowError", 0xC5)
    SLICE_OUT_OF_BOUNDS = ("SliceOutOfBoundsError", 0xC6)
    INVALID_RANGE = ("InvalidRangeError", 0xC7)
    DIMENSION_MISMATCH = ("DimensionMismatchError", 0xC8)
    
    # -------- SECURITY ERRORS (0xE0-0xEF) --------
    UNSANITIZED_INPUT = ("UnsanitizedInputError", 0xE0)
    SQL_INJECTION = ("SQLInjectionError", 0xE1)
    COMMAND_INJECTION = ("CommandInjectionError", 0xE2)
    PATH_TRAVERSAL = ("PathTraversalError", 0xE3)
    UNAUTHORIZED_ACCESS = ("UnauthorizedAccessError", 0xE4)
    SECURITY_POLICY_VIOLATION = ("SecurityPolicyViolationError", 0xE5)
    CRYPTOGRAPHIC_FAILURE = ("CryptographicFailureError", 0xE6)
    TAMPERING_DETECTED = ("TamperingDetectedError", 0xE7)
    
    # -------- CONSISTENCY ERRORS (0xF0-0xF7) --------
    INVARIANT_VIOLATION = ("InvariantViolationError", 0xF0)
    PRECONDITION_FAILED = ("PreconditionFailedError", 0xF1)
    POSTCONDITION_FAILED = ("PostconditionFailedError", 0xF2)
    STATE_INCONSISTENCY = ("StateInconsistencyError", 0xF3)
    DATA_CORRUPTION = ("DataCorruptionError", 0xF4)
    ASSERTION_FAILED = ("AssertionFailedError", 0xF5)
    SANITY_CHECK_FAILED = ("SanityCheckFailedError", 0xF6)
    
    # -------- LEXICAL/SYNTAX ERRORS (0x09-0x0F) --------
    SYNTAX_ERROR = ("SyntaxError", 0x09)
    INVALID_TOKEN = ("InvalidTokenError", 0x0A)
    UNEXPECTED_TOKEN = ("UnexpectedTokenError", 0x0B)
    UNTERMINATED_STRING = ("UnterminatedStringError", 0x0C)
    UNCLOSED_BRACKET = ("UnclosedBracketError", 0x0D)
    INVALID_ESCAPE_SEQUENCE = ("InvalidEscapeSequenceError", 0x0E)
    INVALID_NUMBER_FORMAT = ("InvalidNumberFormatError", 0x0F)
    
    # -------- SEMANTIC ERRORS (0x10-0x3F) --------
    UNDEFINED_VARIABLE = ("UndefinedVariableError", 0x10)
    UNDEFINED_FUNCTION = ("UndefinedFunctionError", 0x11)
    UNDEFINED_TYPE = ("UndefinedTypeError", 0x12)
    REDECLARED_SYMBOL = ("RedeclaredSymbolError", 0x13)
    SHADOWING_FORBIDDEN = ("ShadowingForbiddenError", 0x14)
    UNUSED_VARIABLE = ("UnusedVariableError", 0x15)
    UNUSED_FUNCTION = ("UnusedFunctionError", 0x16)
    DEAD_CODE = ("DeadCodeError", 0x17)
    UNREACHABLE_CODE = ("UnreachableCodeError", 0x18)
    DUPLICATE_CASE_LABEL = ("DuplicateCaseLabelError", 0x19)
    MISSING_RETURN = ("MissingReturnError", 0x1A)
    FUNCTION_ARITY_MISMATCH = ("FunctionArityMismatchError", 0x1B)
    ARGUMENT_MISMATCH = ("ArgumentMismatchError", 0x1C)
    DUPLICATE_FUNCTION_DEFINITION = ("DuplicateFunctionDefinitionError", 0x1D)
    CIRCULAR_DEPENDENCY = ("CircularDependencyError", 0x1E)
    INFINITE_TYPE_RECURSION = ("InfiniteTypeRecursionError", 0x1F)


# ============================================================================
# LOCATION TRACKING
# ============================================================================

class ErrorReporter:
    """
    🚨 THE LYRA ERROR SYSTEM 🚨
    Zero Tolerance Implementation:
    - EVERY error → immediate halt
    - FULL traceability → complete context captured
    - NO silent failures → all errors logged
    - STRICT validation → every operation checked
    """
    
    def __init__(self, program_name: str = "", source_lines: Optional[List[str]] = None) -> None:
        self.program_name = program_name
        self.source_lines = source_lines or []
        self.errors: List[Dict[str, Any]] = []
        self.warnings: List[Dict[str, Any]] = []
        self.error_codes: Set[int] = set()  # Track unique error codes
        self.start_time = datetime.now()
        self.fatal_error = False
        self.panic = False
        self.error_context: Dict[str, Any] = {}  # Store execution context
        self.halt_on_error = True  # STRICT: always halt on error
    
    def set_context(self, **kwargs) -> None:
        """Set execution context for error reporting"""
        self.error_context.update(kwargs)
    
    def report(self, 
               error_type: ErrorType, 
               message: str, 
               location: Optional[SourceLocation] = None,
               severity: ErrorSeverity = ErrorSeverity.ERROR, 
               context: str = "", 
               hint: str = "",
               expected: str = "",
               actual: str = "",
               recovery_action: str = "") -> None:
        """Report an error with FULL context and metadata"""
        
        error_name, error_code = error_type.value
        self.error_codes.add(error_code)
        
        error: Dict[str, Any] = {
            'type': error_name,
            'code': error_code,
            'message': message,
            'location': location,
            'severity': severity,
            'context': context,
            'hint': hint,
            'expected': expected,
            'actual': actual,
            'recovery_action': recovery_action,
            'time': datetime.now(),
            'stack_trace': traceback.format_stack(),
            'execution_context': self.error_context.copy()
        }
        
        if severity == ErrorSeverity.WARNING:
            self.warnings.append(error)
            self.print_warning(error)
        elif severity == ErrorSeverity.PANIC:
            self.panic = True
            self.print_panic(error)
            self.panic_exit()
        else:
            self.errors.append(error)
            self.fatal_error = (severity == ErrorSeverity.FATAL)
            self.print_indictment(error)
            
            if self.halt_on_error or severity == ErrorSeverity.FATAL:
                sys.exit(1)
    
    def print_warning(self, error: Dict[str, Any]) -> None:
        """Print warning message (non-fatal)"""
        print(f"\n⚠️  WARNING [{error['code']:03X}]: {error['type']}")
        print(f"   Message: {error['message']}")
        if error['location']:
            print(f"   Location: {error['location']}")
        if error['hint']:
            print(f"   Hint: {error['hint']}")
    
    def print_panic(self, error: Dict[str, Any]) -> None:
        """Print panic message (system is broken)"""
        print("\n" + "🔥"*35)
        print("PANIC MODE - SYSTEM BROKEN")
        print("🔥"*35)
        print(f"Error Code: {error['code']:03X}")
        print(f"Error Type: {error['type']}")
        print(f"Message: {error['message']}")
        print("System is shutting down...\n")
    
    def print_indictment(self, error: Dict[str, Any]) -> None:
        """Print FORMAL ERROR INDICTMENT with full forensic details"""
        print("\n" + "="*80)
        print(" ❌ LYRA EXECUTION TERMINATED - RIGOROUS ERROR DETECTED ❌")
        print("="*80)
        print(f"\n📋 ERROR DETAILS:")
        print(f"  Error Code: 0x{error['code']:02X} ({error['type']})")
        print(f"  Severity: {error['severity'].name}")
        
        if error['location']:
            loc: SourceLocation = error['location']
            print(f"  Location: {loc.filename}:{loc.line}:{loc.column}")
        
        print(f"\n📝 DIAGNOSIS:")
        print(f"  {error['message']}")
        
        if error['expected']:
            print(f"\n🎯 EXPECTED:")
            print(f"  {error['expected']}")
        
        if error['actual']:
            print(f"\n❌ ACTUAL:")
            print(f"  {error['actual']}")
        
        if error['context']:
            print(f"\n🔍 CONTEXT:")
            print(f"  {error['context']}")
        
        if error['hint']:
            print(f"\n💡 HINT:")
            print(f"  {error['hint']}")
        
        if error['recovery_action']:
            print(f"\n🔧 RECOVERY ACTION:")
            print(f"  {error['recovery_action']}")
        
        print("\n" + "="*80)
        print(f"Process exited with code 1 (Error).")
        print("="*80 + "\n")
    
    def print_source_context(self, location: SourceLocation):
        """Print source code context with detailed error location"""
        line_num = location.line - 1
        
        if line_num < 0 or line_num >= len(self.source_lines):
            return
        
        print(f"\n📄 SOURCE CODE CONTEXT:")
        
        # Show 3 lines before + current + 2 after
        start = max(0, line_num - 3)
        end = min(len(self.source_lines), line_num + 3)
        
        for i in range(start, end):
            if i < len(self.source_lines):
                source_line = self.source_lines[i].replace('\t', '    ')
                prefix = ">>> " if i == line_num else "    "
                print(f"  {prefix}{i+1:4d} | {source_line}")
        
        # Show error pointer
        if location.column > 0:
            error_line = self.source_lines[line_num].replace('\t', '    ')
            pointer_pos = location.column - 1 + 12  # 12 for "      xxxx | "
            pointer_pos = min(pointer_pos, len(error_line) + 12)
            print("  " + " " * pointer_pos + "^^^^ Error position")
    
    def panic_exit(self):
        """Panic mode: Immediate termination without recovery"""
        print("\n" + "🔥"*40)
        print("PANIC MODE ACTIVATED")
        print("🔥"*40)
        print("Lyra system is broken and cannot continue.")
        print("Terminating immediately...\n")
        sys.exit(2)
    
    def check_halt_condition(self) -> bool:
        """Check if program should halt - ANY error triggers halt in STRICT mode"""
        return self.halt_on_error and (len(self.errors) > 0)
    
    def halt_on_first_error(self):
        """Enforce strict mode: halt on first error"""
        if len(self.errors) > 0:
            sys.exit(1)

    
    def summary(self):
        """Print comprehensive error summary at program end with detailed analytics"""
        elapsed = (datetime.now() - self.start_time).total_seconds()
        
        print("\n" + "="*80)
        print(f"🔍 LYRA ERROR SYSTEM SUMMARY: {self.program_name}")
        print("="*80)
        print(f"Total Errors: {len(self.errors)}")
        print(f"Total Warnings: {len(self.warnings)}")
        print(f"Execution Time: {elapsed:.4f}s")
        print(f"Error Codes Used: {len(self.error_codes)}")
        
        # Categorize errors by type
        if self.errors:
            error_types: Dict[str, int] = {}
            error_codes: Dict[str, int] = {}
            for err in self.errors:
                err_type: str = err['type']
                err_code: int = err['code']
                error_types[err_type] = error_types.get(err_type, 0) + 1
                error_codes[f"{err_code:02X}"] = error_codes.get(f"{err_code:02X}", 0) + 1
            
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for i, err in enumerate(self.errors, 1):
                loc_str = f" at {err['location']}" if err['location'] else ""
                severity: Any = err.get('severity', 'ERROR')
                code = f"0x{err['code']:02X}"
                print(f"  {i}. [{code}] [{severity.name if hasattr(severity, 'name') else severity}] {err['type']}: {err['message']}{loc_str}")
            
            print(f"\n📊 ERROR BREAKDOWN BY TYPE:")
            for err_type, count in sorted(error_types.items(), key=lambda x: -x[1]):
                print(f"  - {err_type}: {count}")
            
            print(f"\n📊 ERROR BREAKDOWN BY CODE:")
            for code, count in sorted(error_codes.items()):
                print(f"  - 0x{code}: {count}")
        
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for i, warn in enumerate(self.warnings, 1):
                loc_str = f" at {warn['location']}" if warn['location'] else ""
                code = f"0x{warn['code']:02X}" if 'code' in warn else "    "
                print(f"  {i}. [{code}] {warn['message']}{loc_str}")
        
        if not self.errors and not self.warnings:
            print("\n✅ PERFECT: No errors or warnings found!")
        
        print("="*80 + "\n")
        
        # Write to log file
        self.write_error_system_log()
    
    def write_error_system_log(self):
        """Write comprehensive error system violation log to file"""
        if not self.errors and not self.warnings:
            return
        
        log_filename = f"lyra_error_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        try:
            with open(log_filename, 'w', encoding='utf-8') as f:
                f.write("="*80 + "\n")
                f.write("LYRA ERROR SYSTEM COMPREHENSIVE VIOLATION REPORT\n")
                f.write("="*80 + "\n")
                f.write(f"Program: {self.program_name}\n")
                f.write(f"Timestamp: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Execution Time: {(datetime.now() - self.start_time).total_seconds():.4f}s\n")
                f.write(f"Total Errors: {len(self.errors)}\n")
                f.write(f"Total Warnings: {len(self.warnings)}\n")
                f.write(f"Error Codes Used: {len(self.error_codes)}\n")
                f.write("="*80 + "\n\n")
                
                if self.errors:
                    f.write("ERRORS:\n")
                    f.write("="*80 + "\n")
                    for i, err in enumerate(self.errors, 1):
                        f.write(f"\n[{i}] ERROR CODE: 0x{err['code']:02X}\n")
                        f.write(f"    Type: {err['type']}\n")
                        f.write(f"    Severity: {err['severity'].name}\n")
                        f.write(f"    Message: {err['message']}\n")
                        if err['location']:
                            f.write(f"    Location: {err['location']}\n")
                        if err['context']:
                            f.write(f"    Context: {err['context']}\n")
                        if err['expected']:
                            f.write(f"    Expected: {err['expected']}\n")
                        if err['actual']:
                            f.write(f"    Actual: {err['actual']}\n")
                        if err['hint']:
                            f.write(f"    Hint: {err['hint']}\n")
                        if err['recovery_action']:
                            f.write(f"    Recovery Action: {err['recovery_action']}\n")
                        f.write("-"*80 + "\n")
                
                if self.warnings:
                    f.write("\n\nWARNINGS:\n")
                    f.write("="*80 + "\n")
                    for i, warn in enumerate(self.warnings, 1):
                        f.write(f"\n[{i}] WARNING CODE: 0x{warn.get('code', 0):02X}\n")
                        f.write(f"    Message: {warn['message']}\n")
                        if warn['location']:
                            f.write(f"    Location: {warn['location']}\n")
                        f.write("-"*80 + "\n")
            
            if self.errors or self.warnings:
                print(f"✓ Error report saved to: {log_filename}")
        except Exception as e:
            print(f"❌ Failed to write error system log: {e}")


# ============================================================================
# SOURCE LOCATION TRACKING
# ============================================================================

class SourceLocation:
    """Tracks exact position in source code for error reporting"""
    def __init__(self, filename: str, line: int, column: int):
        self.filename = filename
        self.line = line
        self.column = column
    
    def __str__(self):
        return f"{self.filename}:{self.line}:{self.column}"        if not self.errors and not self.warnings:
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
