"""Regression tests for the orchestrator's stock-out coordination prompt."""

from src.agents.orchestrator.prompts import SYSTEM_PROMPT


def test_inventory_and_pricing_are_requested_in_parallel() -> None:
    assert "Call the inventory and pricing specialists in parallel" in SYSTEM_PROMPT
    assert "do not wait for one result before starting the other" in SYSTEM_PROMPT
    assert "sequentially" not in SYSTEM_PROMPT
