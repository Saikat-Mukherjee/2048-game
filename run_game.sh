#!/bin/bash
echo "Starting 2048 Pygame..."
echo
cd "$(dirname "$0")"
uv run python main.py
