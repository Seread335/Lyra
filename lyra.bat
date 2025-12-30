@echo off
REM ============================================================================
REM LYRA INTERPRETER - Windows Launcher
REM A working Lyra programming language interpreter
REM Version 1.0.3
REM ============================================================================

setlocal enabledelayedexpansion

REM Get script directory
set SCRIPT_DIR=%~dp0
set INTERPRETER=%SCRIPT_DIR%lyra_interpreter\lyra_interpreter.py

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python 3 is not installed or not in PATH
    echo Please install Python 3.7 or later from https://www.python.org
    exit /b 1
)

REM Check if interpreter exists
if not exist "%INTERPRETER%" (
    echo Error: lyra_interpreter.py not found at %INTERPRETER%
    exit /b 1
)

REM Parse arguments
if "%1"=="" (
    REM No arguments - show help
    echo.
    echo ╔════════════════════════════════════════════════════════╗
    echo ║           LYRA PROGRAMMING LANGUAGE                    ║
    echo ║        Interpreter v1.0.3-IRON_RULE                   ║
    echo ║   Strict Error System with Zero Tolerance              ║
    echo ╚════════════════════════════════════════════════════════╝
    echo.
    echo Usage: lyra [file.lyra]
    echo        lyra --help    (Show this help)
    echo        lyra --version (Show version)
    echo.
    echo Examples:
    echo   lyra fibonacci_working.lyra    - Run Fibonacci example
    echo   lyra prime_checker.lyra        - Run Prime checker
    echo   lyra sum_numbers.lyra          - Run Sum calculation
    echo.
    echo Lyra Features:
    echo   - Variables: var x: i32 = 10;
    echo   - Arithmetic: +, -, *, /, %%
    echo   - Comparison: ==, !=, ^<, ^>, ^<=, ^>=
    echo   - Logic: AND, OR, NOT
    echo   - Control Flow: if/else, while loops
    echo   - Built-in: print function
    echo   - Error Handling: Try-catch blocks
    echo   - Iron Rule: Strict error enforcement
    echo.
) else if "%1"=="--version" (
    REM Show version
    echo Lyra Programming Language v1.0.3-IRON_RULE
    echo With Iron Rule Strict Error System
) else if "%1"=="--help" (
    REM Show help (same as no arguments)
    echo.
    echo ╔════════════════════════════════════════════════════════╗
    echo ║           LYRA PROGRAMMING LANGUAGE                    ║
    echo ║        Interpreter v1.0.3-IRON_RULE                   ║
    echo ║   Strict Error System with Zero Tolerance              ║
    echo ╚════════════════════════════════════════════════════════╝
    echo.
    echo Usage: lyra [file.lyra]
    echo        lyra --help    (Show this help)
    echo        lyra --version (Show version)
    echo.
    echo Examples:
    echo   lyra fibonacci_working.lyra    - Run Fibonacci example
    echo   lyra prime_checker.lyra        - Run Prime checker
    echo   lyra sum_numbers.lyra          - Run Sum calculation
    echo.
    echo Lyra Features:
    echo   - Variables: var x: i32 = 10;
    echo   - Arithmetic: +, -, *, /, %%
    echo   - Comparison: ==, !=, ^<, ^>, ^<=, ^>=
    echo   - Logic: AND, OR, NOT
    echo   - Control Flow: if/else, while loops
    echo   - Built-in: print function
    echo   - Error Handling: Try-catch blocks
    echo   - Iron Rule: Strict error enforcement
        echo Error: File not found: %1
        exit /b 1
    )
    
    REM Run Lyra file
    python "%INTERPRETER%" "%1"
)

endlocal
