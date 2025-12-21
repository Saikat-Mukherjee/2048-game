"""
Main game controller for 2048
Handles game loop, event handling, and game flow
"""
import pygame
import sys
from src.game_logic import Game2048
from src.ui import GameUI
from src.database import ScoreDatabase
from src.config import *


class GameState:
    """Enum for game states"""
    MENU = "menu"
    PLAYING = "playing"
    GAME_OVER = "game_over"
    HIGH_SCORES = "high_scores"


class Game2048App:
    def __init__(self):
        pygame.init()
        
        # Set up display
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("2048 - Addictive Puzzle Game")
        
        # Set up clock
        self.clock = pygame.time.Clock()
        
        # Initialize game components
        self.game = Game2048(GRID_SIZE)
        self.ui = GameUI(self.screen)
        self.db = ScoreDatabase()
        
        # Game state
        self.running = True
        self.state = GameState.MENU
        self.player_name = ""
        self.cursor_blink_time = 0
        self.show_cursor = True
    
    def handle_events(self):
        """Handle user input events"""
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif self.state == GameState.MENU:
                self.handle_menu_events(event, mouse_pos)
            
            elif self.state == GameState.PLAYING:
                self.handle_playing_events(event, mouse_pos)
            
            elif self.state == GameState.GAME_OVER:
                self.handle_game_over_events(event, mouse_pos)
            
            elif self.state == GameState.HIGH_SCORES:
                self.handle_high_scores_events(event, mouse_pos)
    
    def handle_menu_events(self, event, mouse_pos):
        """Handle events in menu state"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check which button was clicked
            if self.ui.menu_buttons[0].is_clicked(event):  # New Game
                self.new_game()
                self.state = GameState.PLAYING
            elif self.ui.menu_buttons[1].is_clicked(event):  # High Scores
                self.state = GameState.HIGH_SCORES
            elif self.ui.menu_buttons[2].is_clicked(event):  # Quit
                self.running = False
    
    def handle_playing_events(self, event, mouse_pos):
        """Handle events during gameplay"""
        if event.type == pygame.KEYDOWN:
            if not self.game.game_over:
                moved = False
                
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    moved = self.game.make_move('UP')
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    moved = self.game.make_move('DOWN')
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    moved = self.game.make_move('LEFT')
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    moved = self.game.make_move('RIGHT')
                
                # Trigger animations if move was successful
                if moved:
                    if self.game.new_tile_position:
                        self.ui.animate_new_tile(self.game.new_tile_position)
                    if self.game.merged_positions:
                        self.ui.animate_merge(self.game.merged_positions)
                
                # Check for game over
                if self.game.game_over:
                    self.state = GameState.GAME_OVER
                    self.player_name = ""
        
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check control panel buttons
            if self.ui.control_buttons[0].is_clicked(event):  # New Game
                self.new_game()
            elif self.ui.control_buttons[1].is_clicked(event):  # Menu
                self.state = GameState.MENU
            elif self.ui.control_buttons[2].is_clicked(event):  # High Scores
                self.state = GameState.HIGH_SCORES
    
    def handle_game_over_events(self, event, mouse_pos):
        """Handle events in game over state"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                # Submit score
                self.submit_score()
            elif event.key == pygame.K_BACKSPACE:
                self.player_name = self.player_name[:-1]
            elif event.key == pygame.K_ESCAPE:
                self.state = GameState.MENU
            else:
                # Add character to name (max 20 characters)
                if len(self.player_name) < 20 and event.unicode.isprintable():
                    self.player_name += event.unicode
        
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if submit button was clicked (returned from draw method)
            pass
    
    def handle_high_scores_events(self, event, mouse_pos):
        """Handle events in high scores state"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.state = GameState.MENU
        
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if back button was clicked (handled in render)
            pass
    
    def submit_score(self):
        """Submit the player's score to the database"""
        if not self.player_name.strip():
            self.player_name = "Anonymous"
        
        self.db.save_score(self.player_name.strip(), self.game.score)
        self.state = GameState.HIGH_SCORES
    
    def get_button_rect(self):
        """Get the new game button rect (DEPRECATED)"""
        pass
    
    def new_game(self):
        """Start a new game"""
        self.game.reset()
        self.state = GameState.PLAYING
        self.ui.new_tile_scale.clear()
        self.ui.merge_pulse.clear()
    
    def update(self, dt):
        """Update game state"""
        self.ui.update_animations(dt)
        
        # Update cursor blink for name input
        self.cursor_blink_time += dt
        if self.cursor_blink_time >= 0.5:
            self.cursor_blink_time = 0
            self.show_cursor = not self.show_cursor
    
    def render(self):
        """Render the game"""
        mouse_pos = pygame.mouse.get_pos()
        
        if self.state == GameState.MENU:
            self.ui.draw_main_menu(mouse_pos)
        
        elif self.state == GameState.PLAYING:
            # Draw background
            self.ui.draw_background()
            
            # Draw header with scores
            self.ui.draw_header(self.game.score, self.game.best_score)
            
            # Draw grid and tiles
            self.ui.draw_grid(self.game)
            
            # Draw control panel
            self.ui.setup_control_buttons()
            self.ui.draw_control_panel(mouse_pos)
        
        elif self.state == GameState.GAME_OVER:
            # Draw the game in background
            self.ui.draw_background()
            self.ui.draw_header(self.game.score, self.game.best_score)
            self.ui.draw_grid(self.game)
            self.ui.setup_control_buttons()
            self.ui.draw_control_panel(mouse_pos)
            
            # Draw game over overlay with input
            submit_button = self.ui.draw_game_over_with_input(
                self.game.score, mouse_pos, self.player_name, self.show_cursor
            )
            
            # Handle submit button click
            for event in pygame.event.get([pygame.MOUSEBUTTONDOWN]):
                if submit_button.is_clicked(event):
                    self.submit_score()
        
        elif self.state == GameState.HIGH_SCORES:
            scores = self.db.get_top_scores(10)
            back_button = self.ui.draw_high_scores(scores, mouse_pos)
            
            # Handle back button click
            for event in pygame.event.get([pygame.MOUSEBUTTONDOWN]):
                if back_button.is_clicked(event):
                    self.state = GameState.MENU
        
        # Update display
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            # Calculate delta time
            dt = self.clock.tick(FPS) / 1000.0
            
            # Handle events
            self.handle_events()
            
            # Update game state
            self.update(dt)
            
            # Render
            self.render()
        
        pygame.quit()
        sys.exit()


def main():
    """Entry point for the game"""
    app = Game2048App()
    app.run()


if __name__ == "__main__":
    main()
