"""
Core game logic for 2048
Handles grid management, tile movements, and game state
"""
import random
import copy


class Game2048:
    def __init__(self, grid_size=4):
        self.grid_size = grid_size
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.score = 0
        self.best_score = 0
        self.game_over = False
        self.won = False
        self.moved = False
        self.merged_positions = []
        self.new_tile_position = None
        
        # Add two initial tiles
        self.add_random_tile()
        self.add_random_tile()
    
    def add_random_tile(self):
        """Add a random tile (2 or 4) to an empty cell"""
        empty_cells = [(i, j) for i in range(self.grid_size) 
                      for j in range(self.grid_size) if self.grid[i][j] == 0]
        
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4
            self.new_tile_position = (i, j)
            return True
        return False
    
    def compress(self, row):
        """Remove zeros and shift non-zero values to the left"""
        new_row = [num for num in row if num != 0]
        new_row += [0] * (self.grid_size - len(new_row))
        return new_row
    
    def merge(self, row):
        """Merge adjacent equal values"""
        merged_positions_in_row = []
        for i in range(self.grid_size - 1):
            if row[i] != 0 and row[i] == row[i + 1]:
                row[i] *= 2
                row[i + 1] = 0
                self.score += row[i]
                merged_positions_in_row.append(i)
                
                # Check for win
                if row[i] >= 2048:
                    self.won = True
        
        return row, merged_positions_in_row
    
    def move_left(self):
        """Move all tiles to the left"""
        self.moved = False
        self.merged_positions = []
        new_grid = []
        
        for i, row in enumerate(self.grid):
            compressed = self.compress(row)
            merged, merged_pos = self.merge(compressed)
            final_row = self.compress(merged)
            new_grid.append(final_row)
            
            # Track merged positions
            for pos in merged_pos:
                self.merged_positions.append((i, pos))
            
            # Check if anything changed
            if row != final_row:
                self.moved = True
        
        self.grid = new_grid
    
    def move_right(self):
        """Move all tiles to the right"""
        self.moved = False
        self.merged_positions = []
        new_grid = []
        
        for i, row in enumerate(self.grid):
            reversed_row = row[::-1]
            compressed = self.compress(reversed_row)
            merged, merged_pos = self.merge(compressed)
            final_row = self.compress(merged)[::-1]
            new_grid.append(final_row)
            
            # Track merged positions (adjusted for reversed row)
            for pos in merged_pos:
                self.merged_positions.append((i, self.grid_size - 1 - pos))
            
            if row != final_row:
                self.moved = True
        
        self.grid = new_grid
    
    def move_up(self):
        """Move all tiles up"""
        self.moved = False
        self.merged_positions = []
        
        # Transpose
        transposed = [[self.grid[j][i] for j in range(self.grid_size)] 
                     for i in range(self.grid_size)]
        
        new_grid = []
        for i, row in enumerate(transposed):
            compressed = self.compress(row)
            merged, merged_pos = self.merge(compressed)
            final_row = self.compress(merged)
            new_grid.append(final_row)
            
            # Track merged positions
            for pos in merged_pos:
                self.merged_positions.append((pos, i))
            
            if row != final_row:
                self.moved = True
        
        # Transpose back
        self.grid = [[new_grid[j][i] for j in range(self.grid_size)] 
                    for i in range(self.grid_size)]
    
    def move_down(self):
        """Move all tiles down"""
        self.moved = False
        self.merged_positions = []
        
        # Transpose
        transposed = [[self.grid[j][i] for j in range(self.grid_size)] 
                     for i in range(self.grid_size)]
        
        new_grid = []
        for i, row in enumerate(transposed):
            reversed_row = row[::-1]
            compressed = self.compress(reversed_row)
            merged, merged_pos = self.merge(compressed)
            final_row = self.compress(merged)[::-1]
            new_grid.append(final_row)
            
            # Track merged positions (adjusted for reversed row)
            for pos in merged_pos:
                self.merged_positions.append((self.grid_size - 1 - pos, i))
            
            if row != final_row:
                self.moved = True
        
        # Transpose back
        self.grid = [[new_grid[j][i] for j in range(self.grid_size)] 
                    for i in range(self.grid_size)]
    
    def can_move(self):
        """Check if any moves are possible"""
        # Check for empty cells
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == 0:
                    return True
        
        # Check for possible merges
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                current = self.grid[i][j]
                # Check right
                if j < self.grid_size - 1 and current == self.grid[i][j + 1]:
                    return True
                # Check down
                if i < self.grid_size - 1 and current == self.grid[i + 1][j]:
                    return True
        
        return False
    
    def make_move(self, direction):
        """Make a move in the specified direction"""
        self.new_tile_position = None
        self.merged_positions = []
        
        if direction == 'UP':
            self.move_up()
        elif direction == 'DOWN':
            self.move_down()
        elif direction == 'LEFT':
            self.move_left()
        elif direction == 'RIGHT':
            self.move_right()
        
        # Add new tile if move was successful
        if self.moved:
            self.add_random_tile()
            
            # Check game over
            if not self.can_move():
                self.game_over = True
        
        # Update best score
        if self.score > self.best_score:
            self.best_score = self.score
        
        return self.moved
    
    def reset(self):
        """Reset the game"""
        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.score = 0
        self.game_over = False
        self.won = False
        self.moved = False
        self.merged_positions = []
        self.new_tile_position = None
        
        # Add two initial tiles
        self.add_random_tile()
        self.add_random_tile()
