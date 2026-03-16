# eri-code

This project uses `uv` for Python environment and dependency management.

## Use `uv`

Please use `uv` instead of `pip`, `venv`, or `poetry` commands when working in this repo.

## Install `uv`

Choose one of the following:

### macOS and Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Homebrew

```bash
brew install uv
```

### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

You can confirm the install with:

```bash
uv --version
```

## Project setup

### 1. Create a virtual environment

```bash
uv venv
```

### 2. Activate the virtual environment

macOS and Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

If this repo includes a `pyproject.toml`, run:

```bash
uv sync
```

If you are installing a package manually, use:

```bash
uv pip install <package-name>
```

## Common commands

Run a Python file:

```bash
uv run python your_script.py
```

Add a dependency to the project:

```bash
uv add <package-name>
```

Add a development dependency:

```bash
uv add --dev <package-name>
```
