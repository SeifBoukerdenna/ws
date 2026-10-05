import re
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent

# Third-party and generated directories hold files we do not own, such as the many
# .md files inside .venv, so they are pruned instead of filtered after the walk.
IGNORED_DIRECTORY_NAMES = {
    ".git",
    ".venv",
    ".ruff_cache",
    ".pytest_cache",
    "__pycache__",
    "node_modules",
}
IGNORED_DIRECTORY_RELATIVE_PATHS = {".claude/worktrees"}

ALLOWED_MARKDOWN_PATHS = {
    "AGENTS.md",
    "CLAUDE.md",
    "README.md",
    "ROADMAP.md",
    "research/_template.md",
}
ALLOWED_MARKDOWN_PATTERNS = [
    re.compile(r"research/\d{4}-\d{2}-\d{2}-[a-z0-9]+(-[a-z0-9]+)*\.md"),
    re.compile(r"\.claude/agents/[^/]+\.md"),
]


def list_repository_files(suffix: str) -> list[str]:
    matching_relative_paths: list[str] = []
    for directory_path, directory_names, file_names in REPOSITORY_ROOT.walk():
        relative_directory = directory_path.relative_to(REPOSITORY_ROOT)
        directory_names[:] = [
            name
            for name in directory_names
            if name not in IGNORED_DIRECTORY_NAMES
            and (relative_directory / name).as_posix() not in IGNORED_DIRECTORY_RELATIVE_PATHS
        ]
        matching_relative_paths.extend(
            (relative_directory / name).as_posix() for name in file_names if name.endswith(suffix)
        )
    return sorted(matching_relative_paths)


def test_repository_has_no_notebooks() -> None:
    notebook_paths = list_repository_files(".ipynb")

    assert not notebook_paths, (
        "Notebooks are never allowed (AGENTS.md hard rule 6). "
        f"Turn each into a script in scripts/: {notebook_paths}"
    )


def test_markdown_files_are_on_the_allowed_list() -> None:
    offending_paths = [
        path
        for path in list_repository_files(".md")
        if path not in ALLOWED_MARKDOWN_PATHS
        and not any(pattern.fullmatch(path) for pattern in ALLOWED_MARKDOWN_PATTERNS)
    ]

    assert not offending_paths, (
        "These .md files are not allowed (AGENTS.md hard rule 5). See the "
        f'"Where things go" section of AGENTS.md for the allowed list: {offending_paths}'
    )
