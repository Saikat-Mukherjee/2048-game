# 2048 Pygame - Professional Edition

A modern, addictive implementation of the classic 2048 puzzle game built with Pygame. Features smooth animations, professional UI design, and engaging gameplay.

## 🎮 Features

- **Professional Main Menu**: Clean, polished menu system with smooth navigation
- **High Score Database**: SQLite database to track and display top 10 scores
- **Player Name Entry**: Enter your name when game ends to save your score
- **Smooth Animations**: Tile merging and appearance animations for satisfying gameplay
- **Professional UI**: Carefully designed color scheme matching the classic 2048 aesthetic
- **Score Tracking**: Keep track of your current score and best score
- **Control Panel**: Easy-access buttons for New Game, Menu, and High Scores
- **Responsive Controls**: Use arrow keys or WASD for intuitive tile movement
- **Game Over Detection**: Automatically detects when no more moves are possible
- **Win Detection**: Celebrates when you reach the 2048 tile!
- **Multiple Game States**: Seamless transitions between menu, gameplay, and high scores

## 🚀 Installation

This project uses `uv` for fast dependency management. If you don't have `uv` installed:

```bash
# Install uv (Windows)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or install uv (macOS/Linux)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then install dependencies:

```bash
# Sync dependencies with uv
uv sync
```

## 🎯 How to Play

Run the game:

```bash
# Using uv
uv run python main.py

# Or with standard Python (after installing dependencies)
python main.py
```

### Controls

- **Main Menu**: 
  - Click "New Game" to start playing
  - Click "High Scores" to view top players
  - Click "Quit" to exit
- **During Gameplay**:
  - **Arrow Keys** or **WASD**: Move tiles in the respective direction
  - **Control Panel Buttons**: Access New Game, Menu, and High Scores
- **Game Over Screen**:
  - Type your name to save your score
  - Press Enter or click "Submit" to save
  - Press ESC to return to menu

### Objective

- Combine tiles with the same number to create larger numbers
- Try to reach the **2048** tile to win!
- Keep playing after winning to achieve even higher scores
- The game ends when no more moves are possible

## 📁 Project Structure

```
2048-game/
├── main.py              # Game entry point & controller
├── src/
│   ├── __init__.py      # Package initialization
│   ├── config.py        # Game configuration and constants
│   ├── game_logic.py    # Core 2048 game logic
│   ├── ui.py            # Professional UI with animations & menus
│   └── database.py      # SQLite database for high scores
├── assets/              # Future assets (sounds, images)
├── game_data.db         # SQLite database (auto-created)
├── pyproject.toml       # Project dependencies (uv)
└── README.md            # This file
```

## 🎨 Color Scheme

The game uses a professional color palette that matches the classic 2048 aesthetic:

- **2-4**: Light beige tones
- **8-64**: Orange to red gradient
- **128-512**: Golden yellow tones
- **1024+**: Darker, prestigious colors
- **Background**: Soft cream color for eye comfort

## 🔧 Configuration

Customize the game by modifying values in `src/config.py`:

- Window size and FPS
- Grid size (default: 4x4)
- Tile colors and sizes
- Animation speeds
- Font sizes

## 🎓 Technical Details

- **Language**: Python 3.10+
- **Game Framework**: Pygame 2.5.0+
- **Package Manager**: uv (ultrafast Python package installer)
- **Architecture**: Modular design with separated concerns:
  - Game logic (model)
  - UI rendering (view)
  - Main controller (controller)

## 🌟 Features to Make it Addictive

1. **Smooth Animations**: Tiles smoothly appear and merge
2. **Visual Feedback**: Pulse effect when tiles merge
3. **Score Competition**: Best score tracking + persistent high score leaderboard
4. **Professional Menu**: Polished main menu like commercial games
5. **Player Recognition**: Enter your name and compete for top scores
6. **Easy Navigation**: Quick access to all game features via control panel
7. **Instant Restart**: One-click new game keeps you playing

## 🤝 Contributing

Feel free to fork this project and add your own enhancements:

- Add sound effects for tile movements and merges
- Implement undo functionality
- Add different grid sizes (3x3, 5x5, etc.)
- Create difficulty levels
- Add multiplayer mode
- Enhanced statistics and achievements
- Export/import high scores

## 📝 License

This project is open source and available for educational purposes.

## 🎉 Enjoy Playing!

Challenge yourself to reach 2048 and beyond! The game is designed to be both relaxing and challenging, perfect for quick breaks or extended play sessions.
