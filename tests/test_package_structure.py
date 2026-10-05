import importlib

import pytest

SUBPACKAGE_NAMES = ["core", "data", "costs", "backtest", "evaluation"]


@pytest.mark.parametrize("subpackage_name", SUBPACKAGE_NAMES)
def test_subpackage_has_a_docstring(subpackage_name: str) -> None:
    module = importlib.import_module(f"market_workbench.{subpackage_name}")

    assert module.__doc__ is not None
    assert module.__doc__.strip() != ""
