"""
UI components for 2048 game
Handles rendering, animations, and visual effects
"""
import pygame
import math
from datetime import datetime
from src.config import *


class Button:
    """Generic button class for menu interactions"""
    def __init__(self, x, y, width, height, text, font_size=24):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.is_hovered = False
    
    def update(self, mouse_pos):
        """Update button hover state"""
        self.is_hovered = self.rect.collidepoint(mouse_pos)
    
    def draw(self, screen):
        """Draw the button"""
        color = MENU_BUTTON_HOVER if self.is_hovered else MENU_BUTTON_COLOR
        pygame.draw.rect(screen, color, self.rect, border_radius=5)
        
        text_surface = self.font.render(self.text, True, MENU_BUTTON_TEXT)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def is_clicked(self, event):
        """Check if button was clicked"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.is_hovered
        return False


class GameUI:
    def __init__(self, screen):
        self.screen = screen
        self.tiles_animating = {}
        self.new_tile_scale = {}
        self.merge_pulse = {}
        
        # Initialize fonts
        pygame.font.init()
        self.title_font = pygame.font.Font(None, TITLE_FONT_SIZE)
        self.score_label_font = pygame.font.Font(None, SCORE_LABEL_SIZE)
        self.score_value_font = pygame.font.Font(None, SCORE_VALUE_SIZE)
        
        # Menu fonts
        self.menu_title_font = pygame.font.Font(None, MENU_TITLE_SIZE)
        self.menu_subtitle_font = pygame.font.Font(None, MENU_SUBTITLE_SIZE)
        self.high_score_title_font = pygame.font.Font(None, HIGH_SCORE_TITLE_SIZE)
        self.high_score_entry_font = pygame.font.Font(None, HIGH_SCORE_ENTRY_SIZE)
        
        # Create tile fonts
        self.tile_fonts = {}
        for value, size in TILE_FONT_SIZES.items():
            self.tile_fonts[value] = pygame.font.Font(None, size)
        
        # Default font for larger numbers
        self.tile_fonts['default'] = pygame.font.Font(None, 25)
        
        # Menu buttons
        self.menu_buttons = []
        self.control_buttons = []
        self.setup_menu_buttons()
    
    def setup_menu_buttons(self):
        """Setup main menu buttons"""
        center_x = WINDOW_WIDTH // 2
        start_y = 250
        
        self.menu_buttons = [
            Button(
                center_x - MENU_BUTTON_WIDTH // 2,
                start_y,
                MENU_BUTTON_WIDTH,
                MENU_BUTTON_HEIGHT,
                "New Game",
                28
            ),
            Button(
                center_x - MENU_BUTTON_WIDTH // 2,
                start_y + MENU_BUTTON_HEIGHT + MENU_BUTTON_SPACING,
                MENU_BUTTON_WIDTH,
                MENU_BUTTON_HEIGHT,
                "High Scores",
                28
            ),
            Button(
                center_x - MENU_BUTTON_WIDTH // 2,
                start_y + (MENU_BUTTON_HEIGHT + MENU_BUTTON_SPACING) * 2,
                MENU_BUTTON_WIDTH,
                MENU_BUTTON_HEIGHT,
                "Quit",
                28
            )
        ]
    
    def setup_control_buttons(self):
        """Setup in-game control buttons"""
        y_pos = WINDOW_HEIGHT - CONTROL_PANEL_HEIGHT // 2 - CONTROL_BUTTON_HEIGHT // 2
        spacing = 15
        total_width = CONTROL_BUTTON_WIDTH * 3 + spacing * 2
        start_x = (WINDOW_WIDTH - total_width) // 2
        
        self.control_buttons = [
            Button(start_x, y_pos, CONTROL_BUTTON_WIDTH, CONTROL_BUTTON_HEIGHT, "New Game", 20),
            Button(start_x + CONTROL_BUTTON_WIDTH + spacing, y_pos, CONTROL_BUTTON_WIDTH, CONTROL_BUTTON_HEIGHT, "Menu", 20),
            Button(start_x + (CONTROL_BUTTON_WIDTH + spacing) * 2, y_pos, CONTROL_BUTTON_WIDTH, CONTROL_BUTTON_HEIGHT, "High Scores", 20)
        ]
    
    def get_tile_font(self, value):
        """Get appropriate font size for tile value"""
        if value in self.tile_fonts:
            return self.tile_fonts[value]
        return self.tile_fonts['default']
    
    def get_tile_color(self, value):
        """Get background and text color for a tile value"""
        if value in TILE_COLORS:
            return TILE_COLORS[value]
        # For values higher than 8192
        return TILE_COLORS[8192]
    
    def draw_rounded_rect(self, surface, color, rect, radius=10):
        """Draw a rounded rectangle"""
        pygame.draw.rect(surface, color, rect, border_radius=radius)
    
    def draw_background(self):
        """Draw the game background"""
        self.screen.fill(BACKGROUND_COLOR)
    
    def draw_header(self, score, best_score):
        """Draw the header with title and scores"""
        # Title
        title_text = self.title_font.render("2048", True, (119, 110, 101))
        self.screen.blit(title_text, (20, 20))
        
        # Score boxes
        score_box_width = 110
        score_box_height = 60
        score_box_y = 20
        
        # Best score box
        best_x = WINDOW_WIDTH - score_box_width - 20
        best_rect = pygame.Rect(best_x, score_box_y, score_box_width, score_box_height)
        self.draw_rounded_rect(self.screen, SCORE_BOG_BG, best_rect, 5)
        
        best_label = self.score_label_font.render("BEST", True, SCORE_TEXT_COLOR)
        best_value = self.score_value_font.render(str(best_score), True, SCORE_VALUE_COLOR)
        
        best_label_rect = best_label.get_rect(centerx=best_x + score_box_width // 2, top=score_box_y + 8)
        best_value_rect = best_value.get_rect(centerx=best_x + score_box_width // 2, top=score_box_y + 28)
        
        self.screen.blit(best_label, best_label_rect)
        self.screen.blit(best_value, best_value_rect)
        
        # Score box
        score_x = best_x - score_box_width - 10
        score_rect = pygame.Rect(score_x, score_box_y, score_box_width, score_box_height)
        self.draw_rounded_rect(self.screen, SCORE_BOG_BG, score_rect, 5)
        
        score_label = self.score_label_font.render("SCORE", True, SCORE_TEXT_COLOR)
        score_value = self.score_value_font.render(str(score), True, SCORE_VALUE_COLOR)
        
        score_label_rect = score_label.get_rect(centerx=score_x + score_box_width // 2, top=score_box_y + 8)
        score_value_rect = score_value.get_rect(centerx=score_x + score_box_width // 2, top=score_box_y + 28)
        
        self.screen.blit(score_label, score_label_rect)
        self.screen.blit(score_value, score_value_rect)
    
    def get_grid_position(self):
        """Calculate the starting position of the grid"""
        grid_width = GRID_SIZE * TILE_SIZE + (GRID_SIZE + 1) * GRID_PADDING
        x = (WINDOW_WIDTH - grid_width) // 2
        y = 120  # Positioned to fit comfortably with control panel below
        return x, y
    
    def draw_grid(self, game):
        """Draw the game grid with tiles"""
        grid_x, grid_y = self.get_grid_position()
        
        # Draw grid background
        grid_width = GRID_SIZE * TILE_SIZE + (GRID_SIZE + 1) * GRID_PADDING
        grid_height = GRID_SIZE * TILE_SIZE + (GRID_SIZE + 1) * GRID_PADDING
        grid_rect = pygame.Rect(grid_x, grid_y, grid_width, grid_height)
        self.draw_rounded_rect(self.screen, GRID_BACKGROUND, grid_rect, 10)
        
        # Draw empty tile backgrounds
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                x = grid_x + GRID_PADDING + j * (TILE_SIZE + GRID_PADDING)
                y = grid_y + GRID_PADDING + i * (TILE_SIZE + GRID_PADDING)
                tile_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                self.draw_rounded_rect(self.screen, EMPTY_TILE_COLOR, tile_rect, 5)
        
        # Draw tiles with values
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                value = game.grid[i][j]
                if value != 0:
                    self.draw_tile(i, j, value, game)
    
    def draw_tile(self, row, col, value, game):
        """Draw a single tile with animation support"""
        grid_x, grid_y = self.get_grid_position()
        x = grid_x + GRID_PADDING + col * (TILE_SIZE + GRID_PADDING)
        y = grid_y + GRID_PADDING + row * (TILE_SIZE + GRID_PADDING)
        
        # Get tile colors
        bg_color, text_color = self.get_tile_color(value)
        
        # Handle new tile animation
        scale = 1.0
        pos_key = (row, col)
        if game.new_tile_position == pos_key and pos_key in self.new_tile_scale:
            scale = self.new_tile_scale[pos_key]
        
        # Handle merge animation
        if pos_key in self.merge_pulse:
            pulse = self.merge_pulse[pos_key]
            scale = 1.0 + pulse * 0.15
        
        # Calculate scaled size
        scaled_size = int(TILE_SIZE * scale)
        offset = (TILE_SIZE - scaled_size) // 2
        
        tile_rect = pygame.Rect(x + offset, y + offset, scaled_size, scaled_size)
        self.draw_rounded_rect(self.screen, bg_color, tile_rect, 5)
        
        # Draw text
        font = self.get_tile_font(value)
        text = font.render(str(value), True, text_color)
        text_rect = text.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))
        self.screen.blit(text, text_rect)
    
    def draw_control_panel(self, mouse_pos):
        """Draw the control panel with buttons"""
        # Draw panel background
        panel_rect = pygame.Rect(0, WINDOW_HEIGHT - CONTROL_PANEL_HEIGHT, WINDOW_WIDTH, CONTROL_PANEL_HEIGHT)
        pygame.draw.rect(self.screen, (187, 173, 160), panel_rect)
        
        # Update and draw buttons
        for button in self.control_buttons:
            button.update(mouse_pos)
            button.draw(self.screen)
        
        return self.control_buttons
    
    def draw_new_game_button(self, mouse_pos):
        """Draw the new game button (DEPRECATED - use control panel instead)"""
        # This method is kept for compatibility but no longer used
        pass
    
    def draw_game_over(self, score, won=False):
        """Draw game over overlay"""
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(230)
        overlay.fill(BACKGROUND_COLOR)
        self.screen.blit(overlay, (0, 0))
        
        # Message
        message_font = pygame.font.Font(None, 60)
        if won:
            message_text = message_font.render("You Win!", True, (237, 197, 63))
        else:
            message_text = message_font.render("Game Over!", True, GAME_OVER_TEXT)
        
        message_rect = message_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        self.screen.blit(message_text, message_rect)
        
        # Score
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render(f"Score: {score}", True, GAME_OVER_TEXT)
        score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 10))
        self.screen.blit(score_text, score_rect)
        
        # Instructions
        inst_font = pygame.font.Font(None, 24)
        inst_text = inst_font.render("Click 'New Game' to play again", True, GAME_OVER_TEXT)
        inst_rect = inst_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60))
        self.screen.blit(inst_text, inst_rect)
    
    def animate_new_tile(self, position):
        """Start animation for a new tile"""
        self.new_tile_scale[position] = 0.0
    
    def animate_merge(self, positions):
        """Start animation for merged tiles"""
        for pos in positions:
            self.merge_pulse[pos] = 1.0
    
    def update_animations(self, dt):
        """Update all animations"""
        # Update new tile animations
        to_remove = []
        for pos, scale in self.new_tile_scale.items():
            scale += dt * 5  # Animation speed
            if scale >= 1.0:
                scale = 1.0
                to_remove.append(pos)
            self.new_tile_scale[pos] = scale
        
        for pos in to_remove:
            del self.new_tile_scale[pos]
        
        # Update merge pulse animations
        to_remove = []
        for pos, pulse in self.merge_pulse.items():
            pulse -= dt * 6  # Decay speed
            if pulse <= 0:
                to_remove.append(pos)
            else:
                self.merge_pulse[pos] = pulse
        
        for pos in to_remove:
            del self.merge_pulse[pos]
    
    def draw_main_menu(self, mouse_pos):
        """Draw the main menu screen"""
        self.draw_background()
        
        # Draw title
        title = self.menu_title_font.render("2048", True, MENU_TITLE_COLOR)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 120))
        self.screen.blit(title, title_rect)
        
        # Draw subtitle
        subtitle = self.menu_subtitle_font.render("Slide to combine numbers!", True, MENU_SUBTITLE_COLOR)
        subtitle_rect = subtitle.get_rect(center=(WINDOW_WIDTH // 2, 180))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Update and draw menu buttons
        for button in self.menu_buttons:
            button.update(mouse_pos)
            button.draw(self.screen)
        
        return self.menu_buttons
    
    def draw_high_scores(self, scores, mouse_pos):
        """Draw the high scores screen"""
        self.draw_background()
        
        # Draw title
        title = self.high_score_title_font.render("HIGH SCORES", True, HIGH_SCORE_TEXT_COLOR)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 50))
        self.screen.blit(title, title_rect)
        
        # Draw scores
        start_y = 120
        for i, (player_name, score, timestamp) in enumerate(scores, 1):
            y_pos = start_y + i * 40
            
            # Rank
            rank_text = self.high_score_entry_font.render(f"{i}.", True, HIGH_SCORE_RANK_COLOR)
            self.screen.blit(rank_text, (50, y_pos))
            
            # Player name
            name_text = self.high_score_entry_font.render(player_name, True, HIGH_SCORE_TEXT_COLOR)
            self.screen.blit(name_text, (100, y_pos))
            
            # Score
            score_text = self.high_score_entry_font.render(str(score), True, HIGH_SCORE_TEXT_COLOR)
            score_rect = score_text.get_rect(right=WINDOW_WIDTH - 50, centery=y_pos + 12)
            self.screen.blit(score_text, score_rect)
        
        # Draw back button
        back_button = Button(
            WINDOW_WIDTH // 2 - 100,
            WINDOW_HEIGHT - 80,
            200,
            50,
            "Back to Menu",
            28
        )
        back_button.update(mouse_pos)
        back_button.draw(self.screen)
        
        return back_button
    
    def draw_game_over_with_input(self, score, mouse_pos, player_name="", show_cursor=True):
        """Draw game over screen with name input"""
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(230)
        overlay.fill(BACKGROUND_COLOR)
        self.screen.blit(overlay, (0, 0))
        
        # Message
        message_font = pygame.font.Font(None, 60)
        message_text = message_font.render("Game Over!", True, GAME_OVER_TEXT)
        message_rect = message_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100))
        self.screen.blit(message_text, message_rect)
        
        # Score
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render(f"Score: {score}", True, GAME_OVER_TEXT)
        score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 40))
        self.screen.blit(score_text, score_rect)
        
        # Name input prompt
        prompt_font = pygame.font.Font(None, 28)
        prompt_text = prompt_font.render("Enter your name:", True, GAME_OVER_TEXT)
        prompt_rect = prompt_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 10))
        self.screen.blit(prompt_text, prompt_rect)
        
        # Name input box
        input_width = 300
        input_height = 40
        input_x = WINDOW_WIDTH // 2 - input_width // 2
        input_y = WINDOW_HEIGHT // 2 + 40
        input_rect = pygame.Rect(input_x, input_y, input_width, input_height)
        pygame.draw.rect(self.screen, (255, 255, 255), input_rect)
        pygame.draw.rect(self.screen, (119, 110, 101), input_rect, 2)
        
        # Display name being typed
        name_font = pygame.font.Font(None, 32)
        display_name = player_name + ("|" if show_cursor else "")
        name_surface = name_font.render(display_name, True, (0, 0, 0))
        name_rect = name_surface.get_rect(midleft=(input_x + 10, input_y + input_height // 2))
        self.screen.blit(name_surface, name_rect)
        
        # Submit button
        submit_button = Button(
            WINDOW_WIDTH // 2 - 75,
            WINDOW_HEIGHT // 2 + 100,
            150,
            45,
            "Submit",
            28
        )
        submit_button.update(mouse_pos)
        submit_button.draw(self.screen)
        
        return submit_button
