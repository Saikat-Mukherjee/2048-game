# Quick Setup Guide

## Prerequisites
- Python 3.10 or higher
- uv package manager (will be installed if not present)

## Setup Steps

### 1. Install uv (if not already installed)

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Install Dependencies

```bash
uv sync
```

This will install pygame and set up the virtual environment.

### 3. Run the Game

**Option 1: Using the run script (Windows)**
```
run_game.bat
```

**Option 2: Using the run script (macOS/Linux)**
```bash
chmod +x run_game.sh
./run_game.sh
```

**Option 3: Using uv directly**
```bash
uv run python main.py
```

**Option 4: Using standard Python (after uv sync)**
```bash
python main.py
```

## Controls

- **↑ ↓ ← →** (Arrow Keys): Move tiles
- **W A S D**: Alternative movement keys
- **Mouse Click**: Click "New Game" to restart

## Troubleshooting

### Issue: "uv: command not found"
**Solution**: Make sure uv is installed and in your PATH. Restart your terminal after installation.

### Issue: "pygame not found"
**Solution**: Run `uv sync` to install dependencies.

### Issue: Game window doesn't appear
**Solution**: Make sure you have a display available. If using SSH/remote, you'll need X11 forwarding.

## Customization

Edit `src/config.py` to customize:
- Window size
- Grid size (4x4, 5x5, etc.)
- Colors
- Animation speeds
- Font sizes

## Have Fun!

Enjoy playing 2048! Try to reach the 2048 tile and beyond!
