"""Smoke-test the deterministic outputs readers are expected to see.

This complements numerical assertions by checking that the offline reference examples still
emit the key human-readable output labels used in the book and companion instructions.
"""
from __future__ import annotations

import contextlib
import io

import chapter27_rag_baseline
import chapter28_tool_agent
import reference_assertions


def capture(fn) -> str:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn()
    return buf.getvalue()


def main() -> None:
    numeric = capture(reference_assertions.main)
    assert "ALL PASS: 12 deterministic reference groups" in numeric

    rag = capture(chapter27_rag_baseline.main)
    assert "Recall@3: 1.000" in rag
    assert "MRR: 1.000" in rag
    assert "returns.md" in rag

    agent = capture(chapter28_tool_agent.main)
    assert "blocked as expected" in agent
    assert "cancellation_requested" in agent

    print("ALL REFERENCE-OUTPUT ASSERTIONS: PASS")


if __name__ == "__main__":
    main()
