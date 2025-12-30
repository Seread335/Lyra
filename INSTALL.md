# Installation & Usage Guide - Lyra Programming Language v1.0.2-FEZZ

## Table of Contents
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Command Line Usage](#command-line-usage)
- [Writing Your First Program](#writing-your-first-program)
- [Troubleshooting](#troubleshooting)

---

## Installation

### Prerequisites
- **Python 3.7 or higher** (check with `python --version`)
- **pip** (Python package manager)
- **Git** (for cloning the repository)

### Option 1: Installation from GitHub (Recommended)

```bash
# Clone the repository
git clone https://github.com/Seread335/Lyra.git
cd Lyra

# Install the package
pip install -e .

# Verify installation
lyra --version
```

### Option 2: Installation from Source

```bash
# Clone the repository
git clone https://github.com/Seread335/Lyra.git
cd Lyra

# Install dependencies (if any)
pip install -r requirements.txt

# Make the interpreter executable (optional, for Linux/Mac)
chmod +x lyra_interpreter/lyra_interpreter.py
```

### Option 3: Direct Usage (Without Installation)

```bash
# Clone the repository
git clone https://github.com/Seread335/Lyra.git
cd Lyra

# Run files directly
python lyra_interpreter/lyra_interpreter.py path/to/your/file.lyra
```

---

## Quick Start

### 1. Running Examples

```bash
# Run the Fibonacci example
lyra lyra_interpreter/examples/fibonacci.lyra

# Run the prime checker
lyra lyra_interpreter/examples/prime_checker.lyra

# Run all examples
for example in lyra_interpreter/examples/*.lyra; do
    echo "Running $example..."
    lyra "$example"
done
```

### 2. Interactive REPL (Coming Soon)

```bash
# Start the interactive REPL
lyra --repl
```

### 3. Batch Execution (Windows Users)

Use the provided batch file:

```bash
# Windows only
lyra.bat

# This provides an interactive menu with:
# - Run example files
# - Get language information
# - Check system readiness
# - View help information
```

---

## Command Line Usage

### Syntax

```bash
lyra [options] <file.lyra>
```

### Options

| Option | Description |
|--------|-------------|
| `--version` | Show interpreter version |
| `--help` | Show help message |
| `--debug` | Run in debug mode with detailed output |
| `--profile` | Show execution time and performance metrics |
| `--repl` | Start interactive REPL mode |

### Examples

```bash
# Run a Lyra program
lyra myprogram.lyra

# Run with debug output
lyra --debug myprogram.lyra

# Run with performance profiling
lyra --profile myprogram.lyra

# Show version
lyra --version

# Show help
lyra --help
```

---

## Writing Your First Program

### Hello World

Create a file called `hello.lyra`:

```lyra
print("Hello, World!")
```

Run it:

```bash
lyra hello.lyra
```

### Simple Variables and Operations

Create a file called `math.lyra`:

```lyra
# Variables
let x: i32 = 10
let y: i32 = 20

# Basic operations
let sum: i32 = x + y
let product: i32 = x * y

print("Sum: ")
print(sum)
print("Product: ")
print(product)
```

Run it:

```bash
lyra math.lyra
```

### Functions

Create a file called `functions.lyra`:

```lyra
# Define a function
proc add(a: i32, b: i32) -> i32 {
    return a + b
}

proc multiply(a: i32, b: i32) -> i32 {
    return a * b
}

# Call functions
let result1: i32 = add(5, 3)
let result2: i32 = multiply(4, 7)

print("5 + 3 = ")
print(result1)
print("4 * 7 = ")
print(result2)
```

Run it:

```bash
lyra functions.lyra
```

### Control Flow

Create a file called `control.lyra`:

```lyra
# If statement
let age: i32 = 25

if age >= 18 {
    print("You are an adult")
} else {
    print("You are a minor")
}

# Loop
let i: i32 = 0
while i < 5 {
    print("Count: ")
    print(i)
    let i: i32 = i + 1
}
```

Run it:

```bash
lyra control.lyra
```

### Recursion

Create a file called `recursion.lyra`:

```lyra
# Fibonacci recursive function
proc fib(n: i32) -> i32 {
    if n <= 1 {
        return n
    }
    return fib(n - 1) + fib(n - 2)
}

# Calculate fibonacci(10)
let result: i32 = fib(10)
print("Fibonacci(10) = ")
print(result)
```

Run it:

```bash
lyra recursion.lyra
```

---

## Language Features

### Supported Data Types

- `i32` - 32-bit integer
- `f64` - 64-bit floating-point number
- `str` - String
- `bool` - Boolean (true/false)

### Operators

#### Arithmetic
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Modulo

#### Comparison
- `==` Equal
- `!=` Not equal
- `<` Less than
- `>` Greater than
- `<=` Less than or equal
- `>=` Greater than or equal

#### Logical
- `&&` AND
- `||` OR
- `!` NOT

### Keywords

- `let` - Variable declaration
- `proc` - Function definition
- `if` - Conditional statement
- `else` - Else clause
- `while` - Loop
- `return` - Return from function
- `true`, `false` - Boolean values

---

## Troubleshooting

### Issue: Python not found

**Solution:**
- Install Python 3.7+ from [python.org](https://www.python.org)
- Make sure Python is in your system PATH
- Try using `python3` instead of `python`

### Issue: "command not found: lyra"

**Solution:**
- Make sure you installed using `pip install -e .`
- Try running directly: `python lyra_interpreter/lyra_interpreter.py file.lyra`
- Check that your Python installation is correct

### Issue: Syntax errors in my program

**Solution:**
- Check that all strings are properly quoted
- Make sure variable types are specified with `:`
- Verify function syntax: `proc name(param: type) -> returnType { ... }`
- Use `lyra --debug` to get more detailed error messages

### Issue: "module not found" error

**Solution:**
- Make sure you're in the Lyra repository root directory
- Try running with full path: `python lyra_interpreter/lyra_interpreter.py`
- Reinstall using `pip install -e .`

### Issue: Programs running slowly

**Solution:**
- Use `lyra --profile` to identify bottlenecks
- Avoid deeply nested recursion
- Use loops instead of recursive calls where possible
- Check for infinite loops

---

## File Structure

```
Lyra/
├── lyra_interpreter/
│   ├── lyra_interpreter.py     # Main interpreter
│   ├── examples/               # Example programs
│   │   ├── fibonacci.lyra
│   │   ├── prime_checker.lyra
│   │   └── ... (more examples)
│   ├── src/lyra/              # Additional Lyra source files
│   └── tests/                 # Test suite
├── lyra-vscode-extension/     # VS Code extension
├── setup.py                    # Installation script
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview
```

---

## Getting Help

- **GitHub Issues:** https://github.com/Seread335/Lyra/issues
- **Documentation:** See `/docs` directory
- **Examples:** Check `/lyra_interpreter/examples` directory

---

## Next Steps

1. ✅ Install Lyra
2. ✅ Run the examples
3. ✅ Write your first program
4. 📚 Read the [documentation](../docs)
5. 🤝 Contribute to the project

Happy coding! 🚀
