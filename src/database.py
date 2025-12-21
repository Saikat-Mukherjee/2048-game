"""
Database module for 2048 game
Manages high scores using SQLite
"""
import sqlite3
import os
from datetime import datetime
from pathlib import Path


class ScoreDatabase:
    def __init__(self, db_path="game_data.db"):
        """Initialize database connection"""
        # Store database in user's directory
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Create the scores table if it doesn't exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT NOT NULL,
                score INTEGER NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_score(self, player_name, score):
        """Save a score to the database"""
        if score == 0:
            return  # Don't save zero scores
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            'INSERT INTO scores (player_name, score, timestamp) VALUES (?, ?, ?)',
            (player_name, score, datetime.now())
        )
        
        conn.commit()
        conn.close()
    
    def get_top_scores(self, limit=10):
        """Get top scores from the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT player_name, score, timestamp 
            FROM scores 
            ORDER BY score DESC 
            LIMIT ?
        ''', (limit,))
        
        scores = cursor.fetchall()
        conn.close()
        
        return scores
    
    def get_player_best(self, player_name):
        """Get the best score for a specific player"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT MAX(score) 
            FROM scores 
            WHERE player_name = ?
        ''', (player_name,))
        
        result = cursor.fetchone()
        conn.close()
        
        return result[0] if result[0] is not None else 0
    
    def clear_all_scores(self):
        """Clear all scores from the database (use with caution!)"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM scores')
        
        conn.commit()
        conn.close()
