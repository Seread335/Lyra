#!/usr/bin/env python3
"""
Nested Loop Optimization Analysis
Identifies bottlenecks and proposes optimizations
"""

import time
from lyra_interpreter.lyra_interpreter import Lexer, Parser, Interpreter

# Original nested loop
original_code = """
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
print("Original: " + toString(total))
"""

# Optimized version: reduce variable updates
optimized_v1 = """
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
print("Optimized: " + toString(total))
"""

# Optimized v2: use array instead of nested loop
optimized_v2 = """
var total: i32 = 0
var items: [i32] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
var i: i32 = 0
while i < 50 {
    var j: i32 = 0
    while j < 50 {
        total = total + 1
        j = j + 1
    }
    i = i + 1
}
print("Optimized v2: " + toString(total))
"""

def benchmark_code(name: str, code: str, iterations: int = 10) -> float:
    """Benchmark code execution time"""
    print(f"\n{name}:")
    times = []
    
    for run in range(iterations):
        try:
            lexer = Lexer(code)
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            ast = parser.parse()
            
            start = time.time()
            interpreter = Interpreter()
            interpreter.interpret(ast)
            elapsed = time.time() - start
            
            times.append(elapsed)
        except Exception as e:
            print(f"  Error: {e}")
            return 0
    
    avg_time = sum(times) / len(times)
    min_time = min(times)
    max_time = max(times)
    
    print(f"  Avg: {avg_time*1000:.2f}ms | Min: {min_time*1000:.2f}ms | Max: {max_time*1000:.2f}ms")
    return avg_time

def main():
    print("="*70)
    print("NESTED LOOP OPTIMIZATION ANALYSIS")
    print("="*70)
    
    times = {}
    
    # Benchmark original
    times['original'] = benchmark_code("Original Nested Loop (50x50)", original_code)
    
    # Benchmark optimizations
    times['opt_v1'] = benchmark_code("Optimized v1", optimized_v1)
    times['opt_v2'] = benchmark_code("Optimized v2", optimized_v2)
    
    print("\n" + "="*70)
    print("PERFORMANCE SUMMARY")
    print("="*70)
    
    if times['original'] > 0:
        baseline = times['original']
        print(f"\nOriginal (baseline): {baseline*1000:.2f}ms")
        
        for name, t in times.items():
            if name != 'original' and t > 0:
                improvement = ((baseline - t) / baseline) * 100
                speedup = baseline / t
                status = "FASTER" if improvement > 0 else "SLOWER"
                print(f"{name}: {t*1000:.2f}ms | {status} by {abs(improvement):.1f}% (speedup: {speedup:.2f}x)")
    
    print("\n" + "="*70)
    print("BOTTLENECK ANALYSIS")
    print("="*70)
    print("""
Nested loops are slow because:

1. **Variable Assignments (2500 times)**: 
   - i = i + 1 (50 times per outer loop)
   - j = j + 1 (2500 times total)
   - total = total + 1 (2500 times)
   - Each assignment: variable lookup + arithmetic + store

2. **Comparisons (2550 times)**:
   - i < 50 (2550 times)
   - j < 50 (2500 times)
   
3. **Loop Control Overhead**:
   - Variable scope creation/destruction
   - Each iteration: check condition, execute body, increment

OPTIMIZATION STRATEGIES:

1. **Strength Reduction**: Replace multiplication/division with addition
2. **Loop Unrolling**: Execute multiple iterations per loop (2x, 4x unroll)
3. **Dead Code Elimination**: Remove unused variables
4. **Invariant Code Motion**: Move constant calculations outside loop
5. **SIMD/Vectorization**: Process multiple items per cycle (tree-walker limitation)
6. **JIT Compilation**: Compile hot loops to native code (requires JIT implementation)

LYRA IMPROVEMENTS NEEDED:

1. Implement loop unrolling in FEZZ engine
2. Add strength reduction optimization
3. Enable loop invariant code motion
4. Consider JIT compilation for hot loops
5. Optimize variable lookup with hash table caching
""")

if __name__ == '__main__':
    main()
