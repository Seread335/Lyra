#!/usr/bin/env python3
"""
IPC (Instructions Per Cycle) Measurement for Lyra Interpreter
Measures execution performance metrics
"""

import time
import sys
from lyra_interpreter.lyra_interpreter import Lexer, Parser, Interpreter

# Test cases
test_cases = {
    "arithmetic": """
var sum: i32 = 0
var i: i32 = 0
while i < 1000 {
    sum = sum + i
    i = i + 1
}
print("Arithmetic sum:" + tostring(sum))
""",
    
    "branches": """
var count: i32 = 0
var i: i32 = 0
while i < 100 {
    if i % 2 == 0 {
        count = count + 1
    }
    if i % 3 == 0 {
        count = count + 10
    }
    i = i + 1
}
print("Branches count:" + tostring(count))
""",
    
    "nested_loops": """
var total: i32 = 0
var i: i32 = 0
while i < 50 {
    var j: i32 = 0
    while j < 50 {
        total = total + 1
        j = j + 1
    }
    i = i + 1
}
print("Nested loops total:" + tostring(total))
""",
    
    "string_ops": """
var text: str = "Hello Lyra"
var i: i32 = 0
while i < 100 {
    var len: i32 = length(text)
    i = i + 1
}
print("String ops done")
""",
}

def count_instructions(code: str) -> int:
    """Estimate number of instructions in code"""
    # Simple heuristic: count key operations
    ops = code.count('+') + code.count('-') + code.count('*') + code.count('/')
    ops += code.count('=') + code.count('if') + code.count('while')
    ops += code.count('print') + code.count('length')
    return max(ops, 1)

def measure_performance(name: str, code: str) -> dict:
    """Measure performance metrics for a test case"""
    try:
        # Parse code
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Execute multiple times for better measurement
        iterations = 10
        start_time = time.time()
        
        for _ in range(iterations):
            interpreter = Interpreter()
            interpreter.interpret(ast)
        
        elapsed = time.time() - start_time
        
        # Calculate metrics
        instr_count = count_instructions(code)
        total_instructions = instr_count * iterations
        avg_time = elapsed / iterations
        ipc = total_instructions / max(elapsed, 0.001)  # Instructions per cycle (approximated)
        
        return {
            'name': name,
            'total_time': elapsed,
            'avg_time': avg_time,
            'instructions': instr_count,
            'ipc': ipc,
            'status': '✓'
        }
    except Exception as e:
        return {
            'name': name,
            'status': f'✗ {str(e)[:50]}',
            'total_time': 0,
            'avg_time': 0,
            'instructions': 0,
            'ipc': 0
        }

def main():
    print("="*70)
    print("LYRA IPC (Instructions Per Cycle) MEASUREMENT")
    print("Version 1.0.3")
    print("="*70)
    print()
    
    results = []
    
    for test_name, code in test_cases.items():
        print(f"Running {test_name}...", end=" ", flush=True)
        result = measure_performance(test_name, code)
        results.append(result)
        print(result['status'])
    
    print()
    print("="*70)
    print("PERFORMANCE RESULTS")
    print("="*70)
    print()
    print(f"{'Test':<20} {'Time (ms)':<12} {'Instructions':<15} {'IPC':<10}")
    print("-"*70)
    
    total_ipc = 0
    valid_count = 0
    
    for result in results:
        if result['status'] == '✓':
            time_ms = result['total_time'] * 1000
            print(f"{result['name']:<20} {time_ms:<12.3f} {result['instructions']:<15} {result['ipc']:<10.2f}")
            total_ipc += result['ipc']
            valid_count += 1
        else:
            print(f"{result['name']:<20} {result['status']}")
    
    print("-"*70)
    if valid_count > 0:
        avg_ipc = total_ipc / valid_count
        print(f"{'Average IPC:':<20} {avg_ipc:<10.2f}")
    print()
    print("="*70)
    print("NOTES:")
    print("- IPC is approximated based on instruction count and execution time")
    print("- Higher IPC indicates better instruction throughput")
    print("- Tree-walking interpreter baseline: ~0.5-2.0 IPC")
    print("- Optimized interpreter target: ~2.0-4.0 IPC")
    print("="*70)

if __name__ == '__main__':
    main()
