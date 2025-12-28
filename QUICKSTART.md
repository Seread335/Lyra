# Quick Start Guide - Lyra Programming Language

Get started with Lyra in 5 minutes! ⚡

## Installation (30 seconds)

```bash
# Clone and install
git clone https://github.com/Seread335/Lyra.git
cd Lyra
pip install -e .

# Verify
lyra --version
```

Or run directly without installation:
```bash
python lyra_interpreter/lyra_interpreter.py path/to/file.lyra
```

---

## Your First Program (1 minute)

Create `hello.lyra`:
```lyra
print("Hello, Lyra!")
```

Run it:
```bash
lyra hello.lyra
```

---

## 5 Core Concepts (2 minutes)

### 1. Variables
```lyra
let x: i32 = 10          # Integer
let name: str = "Alice"  # String
let pi: f64 = 3.14       # Float
let active: bool = true  # Boolean
```

### 2. Math
```lyra
let a: i32 = 5
let b: i32 = 3
print(a + b)  # 8
print(a * b)  # 15
```

### 3. Functions
```lyra
proc greet(name: str) -> str {
    return name
}

print(greet("World"))  # Outputs: World
```

### 4. Conditionals
```lyra
let age: i32 = 20

if age >= 18 {
    print("Adult")
} else {
    print("Minor")
}
```

### 5. Loops
```lyra
let i: i32 = 0
while i < 5 {
    print(i)
    let i: i32 = i + 1
}
```

---

## Run Examples (1 minute)

```bash
# Fibonacci sequence
lyra lyra_interpreter/examples/fibonacci.lyra

# Check if number is prime
lyra lyra_interpreter/examples/prime_checker.lyra

# Sum numbers 1-100
lyra lyra_interpreter/examples/sum_numbers.lyra

# Multiplication table
lyra lyra_interpreter/examples/multiplication_table.lyra
```

---

## Common Tasks

### Create and Run a File

```bash
# Create a new file
echo "print(\"Hello\")" > myprogram.lyra

# Run it
lyra myprogram.lyra
```

### Run with Debug Info

```bash
lyra --debug myprogram.lyra
```

### Check Performance

```bash
lyra --profile myprogram.lyra
```

---

## Program Structure

```lyra
# 1. Declare variables
let x: i32 = 10

# 2. Define functions
proc double(n: i32) -> i32 {
    return n * 2
}

# 3. Use conditionals
if x > 5 {
    print("Large")
}

# 4. Use loops
let i: i32 = 0
while i < 3 {
    print(double(i))
    let i: i32 = i + 1
}
```

---

## Supported Data Types

| Type | Example | Description |
|------|---------|-------------|
| `i32` | `10` | 32-bit integer |
| `f64` | `3.14` | Float/decimal |
| `str` | `"hello"` | Text/string |
| `bool` | `true` | true/false |

---

## Next Steps

- 📖 Read [INSTALL.md](INSTALL.md) for detailed installation
- 📚 Check [documentation](docs/) for advanced features
- 💡 Explore [examples](lyra_interpreter/examples/) for more code samples
- 🐛 Report issues on [GitHub](https://github.com/Seread335/Lyra/issues)

---

## Example: Simple Calculator

Create `calculator.lyra`:

```lyra
proc add(a: i32, b: i32) -> i32 {
    return a + b
}

proc subtract(a: i32, b: i32) -> i32 {
    return a - b
}

proc multiply(a: i32, b: i32) -> i32 {
    return a * b
}

proc divide(a: i32, b: i32) -> i32 {
    return a / b
}

let x: i32 = 20
let y: i32 = 4

print("20 + 4 = ")
print(add(x, y))

print("20 - 4 = ")
print(subtract(x, y))

print("20 * 4 = ")
print(multiply(x, y))

print("20 / 4 = ")
print(divide(x, y))
```

Run it:
```bash
lyra calculator.lyra
```

Output:
```
20 + 4 = 
24.0
20 - 4 = 
16.0
20 * 4 = 
80.0
20 / 4 = 
5.0
```

---

**Ready to code? Start with the examples above and explore the [documentation](INSTALL.md)!** 🚀
