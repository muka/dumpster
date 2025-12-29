# Dumpster

Dumpster is a tool to create a single-file context dump of your codebase, perfect for AI analysis or documentation.

## Features

- Collects code from multiple files into one output file
- Supports Git integration for version information
- Configurable through dump.yaml
- Handles various file types including Python, Markdown, YAML, and more

## Installation

```bash
pip install dumpster
```

## Usage

1. Create a dump.yaml configuration file:
```yaml
output: sources.txt
extensions:
  - .py
  - .md
  - .yaml
contents:
  - "**/*.py"
  - "**/*.md"
```

You can also use `dumpster init` to create a stub `dump.yaml` and create/update the local `.gitignore`

2. Run the dump command:
```bash
dumpster
```

## Configuration

The `dump.yaml` file supports these options:

- `output`: Output file path (default: sources.txt)
- `extensions`: List of file extensions to include
- `contents`: Patterns of files to include
- `exclude`: Patterns of files to exclude
- `prompt`: Optional prompt text
- `header`: Optional header text
- `footer`: Optional footer text

## Git Integration

Dumpster automatically includes Git metadata in the output:
- Repository root
- Current branch
- Commit hash
- Commit time
- Author information
- Dirty status

## Development

Dumpster uses these dependencies:
- GitPython for Git operations
- Pydantic for configuration validation
- PyYAML for YAML parsing

The project follows semantic versioning and uses uv for dependency management.

## LICENSE

