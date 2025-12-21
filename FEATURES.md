# 2048 Game Features Guide

## Main Menu System

When you launch the game, you'll see a professional main menu with three options:

### Menu Options

1. **New Game**
   - Starts a fresh game with a clean 4x4 grid
   - Resets score to 0
   - Places two random tiles (2 or 4) on the grid

2. **High Scores**
   - Displays the top 10 scores from all players
   - Shows player name, score, and rank
   - Press ESC or click "Back to Menu" to return

3. **Quit**
   - Exits the game application

## Gameplay Features

### Game Controls

**Movement:**
- ↑ ↓ ← → (Arrow Keys): Move tiles in any direction
- W A S D: Alternative movement controls
- Tiles slide in the direction pressed and merge when identical

**Control Panel (Bottom of Screen):**
- **New Game**: Restart with a fresh grid
- **Menu**: Return to main menu
- **High Scores**: View leaderboard during gameplay

### Game Mechanics

**Tile Movement:**
- All tiles slide in the selected direction
- When two tiles with the same number touch, they merge
- Merged tiles double in value (2+2=4, 4+4=8, etc.)
- Each move generates a new tile (2 or 4) in a random empty cell

**Scoring:**
- You earn points equal to the value of newly merged tiles
- Merging 2+2 = 4 points
- Merging 4+4 = 8 points
- Merging 1024+1024 = 2048 points!

**Win Condition:**
- Create a tile with value 2048
- You can continue playing after winning to achieve higher scores

**Game Over:**
- Occurs when no more moves are possible
- No empty cells AND no adjacent tiles can merge
- Triggers the score submission screen

## High Score System

### Score Submission

When the game ends:

1. **Name Entry Screen** appears
   - Type your name (up to 20 characters)
   - Use Backspace to correct mistakes
   - Press Enter or click "Submit" to save
   - Press ESC to skip and return to menu
   - If no name entered, saves as "Anonymous"

2. **Database Storage**
   - Scores are permanently saved in SQLite database
   - File: `game_data.db` in the game directory
   - Survives game restarts

### High Scores Display

**Leaderboard Features:**
- Shows top 10 highest scores
- Displays: Rank, Player Name, Score
- Sorted from highest to lowest score
- No time limit - can be viewed anytime

**Navigation:**
- Click "Back to Menu" to return
- Press ESC for quick return
- Access from main menu or during gameplay

## Visual Features

### Animations

**New Tile Animation:**
- Tiles "pop in" when they appear
- Smooth scale-up effect
- Makes new tiles easy to spot

**Merge Animation:**
- Tiles pulse when merging
- Visual feedback for successful combinations
- Satisfying confirmation of moves

**Color Scheme:**
- Each tile value has unique colors
- 2-4: Light beige
- 8-64: Orange to red gradient
- 128-512: Golden yellow
- 1024+: Dark prestigious colors
- High contrast for easy reading

### UI Elements

**Score Display:**
- Current score (top right)
- Best score ever (top right)
- Both update in real-time

**Grid:**
- Professional rounded corners
- Clear tile separation
- Smooth color transitions

**Buttons:**
- Hover effects for better feedback
- Consistent styling throughout
- Large, easy-to-click targets

## Database Information

### File Location
- **Database File**: `game_data.db`
- **Location**: Game root directory
- **Type**: SQLite 3
- **Auto-created**: On first game over

### Data Stored
- Player name (text)
- Score (integer)
- Timestamp (datetime)
- Unique ID (auto-increment)

### Database Operations

**Viewing Data:**
You can view the database using any SQLite browser:
- DB Browser for SQLite (free, cross-platform)
- Command line: `sqlite3 game_data.db`

**Query Examples:**
```sql
-- View all scores
SELECT * FROM scores ORDER BY score DESC;

-- View top 10
SELECT player_name, score FROM scores ORDER BY score DESC LIMIT 10;

-- View player's best
SELECT MAX(score) FROM scores WHERE player_name = 'YourName';

-- Count total games
SELECT COUNT(*) FROM scores;
```

**Backup:**
Simply copy `game_data.db` to backup your scores.

**Reset:**
Delete `game_data.db` to clear all scores (will be recreated on next game over).

## Tips for High Scores

1. **Corner Strategy**: Keep your highest tile in a corner
2. **Build in One Direction**: Don't spread tiles randomly
3. **Plan Ahead**: Think 2-3 moves ahead
4. **Avoid Random Moves**: Every move should have purpose
5. **Maintain Order**: Keep tiles in descending order
6. **Don't Fill the Grid**: Leave room for new tiles
7. **Merge Systematically**: Combine smaller tiles first

## Keyboard Shortcuts

**During Gameplay:**
- Arrow Keys / WASD: Move tiles
- No pause function (game is turn-based)

**Game Over Screen:**
- Type: Enter name
- Backspace: Delete character
- Enter: Submit score
- ESC: Skip to menu

**High Scores Screen:**
- ESC: Return to menu

**Main Menu:**
- Click only (no keyboard shortcuts)

## Troubleshooting

### Database Issues

**Database file not created:**
- Play a game until game over
- Enter a name and submit
- Database will be created automatically

**Scores not saving:**
- Check write permissions in game directory
- Ensure score is greater than 0
- Verify name was entered (or left for Anonymous)

**Duplicate scores:**
- This is normal - each game creates a new entry
- Multiple games with same score are all recorded
- Leaderboard shows top 10 regardless of duplicates

### Display Issues

**Buttons not responding:**
- Ensure you're clicking (not just hovering)
- Check mouse is over button (look for color change)

**Animations not smooth:**
- Check system resources
- Close other programs
- Game runs at 60 FPS by default

## Future Enhancements

**Planned Features:**
- Sound effects
- Music toggle
- Statistics page
- Achievement system
- Multiple difficulty levels
- Daily challenges
- Online leaderboards

Enjoy playing 2048! 🎮
