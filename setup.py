#!/usr/bin/env python3
"""
Lyra Language - Setup and Installation Script
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
requirements = []
if os.path.exists("requirements.txt"):
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="lyra-language",
    version="1.0.3",
    author="Seread335",
    author_email="seread335@gmail.com",
    description="Lyra Programming Language - A modern, efficient language interpreter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Seread335/Lyra.git",
    project_urls={
        "Bug Tracker": "https://github.com/Seread335/Lyra/issues",
        "Documentation": "https://github.com/Seread335/Lyra/tree/main/docs",
        "Source Code": "https://github.com/Seread335/Lyra",
    },
    packages=find_packages(include=["lyra_interpreter", "lyra_interpreter.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Interpreters",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "lyra=lyra_interpreter.lyra_interpreter:main_cli",
        ],
    },
    include_package_data=True,
    package_data={
        "lyra_interpreter": [
            "examples/*.lyra",
            "src/lyra/*.lyra",
            "tools/*.lyra",
        ],
    },
    zip_safe=False,
)
