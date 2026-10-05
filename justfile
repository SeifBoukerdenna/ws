# List every recipe.
default:
    @just --list

# Install Python and the dev tools into .venv.
setup:
    uv sync

# Lint, format check, strict type check, tests.
check:
    uv run ruff check .
    uv run ruff format --check .
    uv run pyright
    uv run pytest

# Format the code and apply safe lint fixes.
fmt:
    uv run ruff format .
    uv run ruff check --fix .

# Run pytest; arguments pass through.
test *arguments:
    uv run pytest {{arguments}}

# Run scripts/<name>.py; arguments pass through.
run name *arguments:
    uv run python scripts/{{name}}.py {{arguments}}
