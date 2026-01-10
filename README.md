# GlassPilot

GlassPilot is an open-source LLM (Large Language Model) powered assistant CLI tool designed to help developers analyze large codebases efficiently and intelligently.
Core Principles:

- Simplicity and Flexibility - flexible configuration options, allowing developers to tailor the assistant to their specific project needs
- Token Usage Transparency - Provides clear, real-time visibility into token consumption
- Context-Aware Analysis - Intelligently navigates and understands code structure, dependencies, and relationships across multiple files to provide meaningful insights

## Commands
```commandline
# Commands to execute GlassPilot
glasspilot --help
glasspilot execute 'hello world'
glasspilot echo 'hello world'
```

## Dev Commands

```commandline
# Commands to execute GlassPilot
python3 src/main.py --help
python3 src/main.py execute 'hello world'
python3 src/main.py echo 'hello world'


# Running link on local
pip install flake8
flake8 src

# Create binary executable
pyinstaller --onefile --name glasspilot src/main.py
```
