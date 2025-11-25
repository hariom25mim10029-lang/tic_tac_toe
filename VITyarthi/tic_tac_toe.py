import os
import json
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod


class Board:
    """Manages the game board state and operations"""
    
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.size = 3
    
    def display(self):
        """Display the current board state"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n   TIC TAC TOE\n")
        print("     0   1   2")
        for i, row in enumerate(self.grid):
            print(f"  {i}  {row[0]} | {row[1]} | {row[2]}")
            if i < 2:
                print("    -----------")
        print()
    
    def is_valid_move(self, row: int, col: int) -> bool:
        """Validate if move is within bounds and cell is empty"""
        return 0 <= row < 3 and 0 <= col < 3 and self.grid[row][col] == ' '
    
    def make_move(self, row: int, col: int, symbol: str) -> bool:
        """Place symbol on board if valid"""
        if self.is_valid_move(row, col):
            self.grid[row][col] = symbol
            return True
        return False
    
    def is_full(self) -> bool:
        """Check if board is completely filled"""
        return all(cell != ' ' for row in self.grid for cell in row)
    
    def reset(self):
        """Clear the board"""
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
    
    def get_state(self) -> List[List[str]]:
        """Return current board state"""
        return [row[:] for row in self.grid]


class GameLogic:
    """Handles win detection and game state evaluation"""
    
    @staticmethod
    def check_winner(board: Board) -> Optional[str]:
        """
        Check if there's a winner
        Returns: 'X', 'O', or None
        """
        grid = board.grid
        
        for row in grid:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        for col in range(3):
            if grid[0][col] == grid[1][col] == grid[2][col] != ' ':
                return grid[0][col]
        
        if grid[0][0] == grid[1][1] == grid[2][2] != ' ':
            return grid[0][0]
        if grid[0][2] == grid[1][1] == grid[2][0] != ' ':
            return grid[0][2]
        
        return None
    
    @staticmethod
    def is_game_over(board: Board) -> Tuple[bool, Optional[str]]:
        """
        Check if game is over
        Returns: (is_over, winner_or_draw)
        """
        winner = GameLogic.check_winner(board)
        if winner:
            return True, winner
        if board.is_full():
            return True, 'Draw'
        return False, None


class Player(ABC):
    """Abstract base class for players"""
    
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol
        self.wins = 0
    
    @abstractmethod
    def get_move(self, board: Board) -> Tuple[int, int]:
        """Get player's move"""
        pass


class HumanPlayer(Player):
    """Human player with input validation"""
    
    def get_move(self, board: Board) -> Tuple[int, int]:
        """Get move from user with validation"""
        while True:
            try:
                move = input(f"{self.name} ({self.symbol}), enter row,col (e.g., 0,1): ").strip()
                row, col = map(int, move.split(','))
                
                if board.is_valid_move(row, col):
                    return row, col
                else:
                    print("Invalid move! Cell occupied or out of bounds.")
            except (ValueError, IndexError):
                print("Invalid format! Use: row,col (e.g., 0,1)")
            except KeyboardInterrupt:
                raise


class AIPlayer(Player):
    """AI player with minimax algorithm"""
    
    def get_move(self, board: Board) -> Tuple[int, int]:
        """Get AI move using minimax"""
        print(f"{self.name} is thinking...")
        best_score = float('-inf')
        best_move = None
        
        for i in range(3):
            for j in range(3):
                if board.grid[i][j] == ' ':
                    board.grid[i][j] = self.symbol
                    score = self._minimax(board, 0, False)
                    board.grid[i][j] = ' '
                    
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        return best_move
    
    def _minimax(self, board: Board, depth: int, is_max: bool) -> int:
        """Minimax algorithm for optimal play"""
        winner = GameLogic.check_winner(board)
        
        if winner == self.symbol:
            return 10 - depth
        elif winner:
            return depth - 10
        elif board.is_full():
            return 0
        
        if is_max:
            best = float('-inf')
            opponent = 'O' if self.symbol == 'X' else 'X'
            for i in range(3):
                for j in range(3):
                    if board.grid[i][j] == ' ':
                        board.grid[i][j] = self.symbol
                        best = max(best, self._minimax(board, depth + 1, False))
                        board.grid[i][j] = ' '
            return best
        else:
            best = float('inf')
            opponent = 'O' if self.symbol == 'X' else 'X'
            for i in range(3):
                for j in range(3):
                    if board.grid[i][j] == ' ':
                        board.grid[i][j] = opponent
                        best = min(best, self._minimax(board, depth + 1, True))
                        board.grid[i][j] = ' '
            return best


class Statistics:
    """Manages game statistics and persistence"""
    
    def __init__(self, filename='stats.json'):
        self.filename = filename
        self.data = self._load()
    
    def _load(self) -> dict:
        """Load statistics from file"""
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {'games': 0, 'x_wins': 0, 'o_wins': 0, 'draws': 0}
    
    def save(self):
        """Save statistics to file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.data, f, indent=2)
        except IOError as e:
            print(f"Error saving stats: {e}")
    
    def update(self, result: Optional[str]):
        """Update statistics with game result"""
        self.data['games'] += 1
        if result == 'X':
            self.data['x_wins'] += 1
        elif result == 'O':
            self.data['o_wins'] += 1
        elif result == 'Draw':
            self.data['draws'] += 1
        self.save()
    
    def display(self):
        """Display statistics"""
        print("\n=== GAME STATISTICS ===")
        print(f"Total Games: {self.data['games']}")
        print(f"X Wins: {self.data['x_wins']}")
        print(f"O Wins: {self.data['o_wins']}")
        print(f"Draws: {self.data['draws']}")
        print("=" * 24 + "\n")


class GameController:
    """Main game controller orchestrating all components"""
    
    def __init__(self):
        self.board = Board()
        self.stats = Statistics()
        self.player1 = None
        self.player2 = None
        self.current_player = None
    
    def setup_game(self):
        """Setup game mode and players"""
        print("\n=== TIC TAC TOE SETUP ===")
        print("1. Player vs Player")
        print("2. Player vs AI")
        print("3. View Statistics")
        print("4. Exit")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '1':
            name1 = input("Player 1 name: ").strip() or "Player 1"
            name2 = input("Player 2 name: ").strip() or "Player 2"
            self.player1 = HumanPlayer(name1, 'X')
            self.player2 = HumanPlayer(name2, 'O')
            return True
        
        elif choice == '2':
            name = input("Your name: ").strip() or "Player"
            self.player1 = HumanPlayer(name, 'X')
            self.player2 = AIPlayer("AI", 'O')
            return True
        
        elif choice == '3':
            self.stats.display()
            return self.setup_game()
        
        elif choice == '4':
            return False
        
        else:
            print("Invalid choice!")
            return self.setup_game()
    
    def play_turn(self):
        """Execute one player turn"""
        self.board.display()
        
        try:
            row, col = self.current_player.get_move(self.board)
            
            if self.board.make_move(row, col, self.current_player.symbol):
                return True
            else:
                print("Invalid move! Try again.")
                return False
        except KeyboardInterrupt:
            print("\n\nGame interrupted!")
            raise
    
    def switch_player(self):
        """Switch to the other player"""
        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )
    
    def play_game(self):
        """Main game loop"""
        self.board.reset()
        self.current_player = self.player1
        
        while True:
            if self.play_turn():
                is_over, result = GameLogic.is_game_over(self.board)
                
                if is_over:
                    self.board.display()
                    
                    if result == 'Draw':
                        print("It's a DRAW!")
                    else:
                        winner = self.player1 if result == self.player1.symbol else self.player2
                        winner.wins += 1
                        print(f"🎉 {winner.name} WINS!")
                    
                    self.stats.update(result)
                    break
                
                self.switch_player()
    
    def run(self):
        """Main application loop"""
        print("\n" + "="*40)
        print("   WELCOME TO TIC TAC TOE")
        print("="*40)
        
        try:
            while True:
                if not self.setup_game():
                    print("\nThanks for playing!")
                    break
                
                self.play_game()
                
                play_again = input("\nPlay again? (y/n): ").strip().lower()
                if play_again != 'y':
                    self.stats.display()
                    print("Thanks for playing!")
                    break
        
        except KeyboardInterrupt:
            print("\n\nGame terminated by user.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    game = GameController()
    game.run()
