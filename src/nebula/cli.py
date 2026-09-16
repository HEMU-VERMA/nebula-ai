"""Command-line interface for Nebula."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Build the Nebula command-line parser."""
    parser = argparse.ArgumentParser(
        prog="nebula",
        description="Reproducible AI-guided software evolution.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0",
    )
    return parser


def main() -> int:
    """Run the command-line interface."""
    build_parser().parse_args()
    return 0
