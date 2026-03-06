"""Shared pytest fixtures for this repository.

This file is intentionally repository-agnostic so it can be reused across
teaching examples without depending on project-specific modules.
"""

import pytest


@pytest.fixture(scope="session")
def sample_numbers() -> tuple[int, int, int]:
    """Provide a small numeric sample for basic unit tests."""
    return (1, 2, 3)


@pytest.fixture(scope="session")
def sample_text() -> str:
    """Provide a reusable text sample for parsing/string tests."""
    return "A, Bee, bee, , C"


@pytest.fixture(scope="function")
def sample_config() -> dict[str, object]:
    """Provide a generic config payload for tests that need dict inputs."""
    return {"debug": True, "retries": 2, "timeout_seconds": 5}


@pytest.fixture(scope="function")
def temp_workdir(tmp_path):
    """Provide a temporary directory path for file-based tests."""
    return tmp_path


class IgnoreObj:
    """A permissive stand-in object for tests that need a no-op placeholder."""

    def __getattr__(self, __name: str):
        return self

    def __call__(self, *args, **kwargs):
        return self

    def __setattr__(self, __name: str, __value):
        return None

    def __getitem__(self, __key: str):
        return self

    def __setitem__(self, __key: str, __value):
        return None


@pytest.fixture(scope="package")
def ignore_obj():
    """Provide a generic no-op object for dependency isolation in tests."""
    return IgnoreObj()
