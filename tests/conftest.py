# tests/conftest.py
from __future__ import annotations

import pytest
from pathlib import Path


@pytest.fixture
def tmp_path(tmp_path_factory: pytest.TempPathFactory) -> Path:
    """
    Provide a per-test temporary directory Path.

    Notes:
    - Pytest already provides a built-in `tmp_path` fixture by default.
    - This conftest defines it explicitly only in case your environment/plugins
      have disabled or shadowed the built-in fixture.
    """
    return tmp_path_factory.mktemp("dumpster")
