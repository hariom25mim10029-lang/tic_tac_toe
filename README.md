# 🎮 Tic Tac Toe Game

A comprehensive implementation of the classic Tic Tac Toe game with an unbeatable , opponent, built using Python with clean architecture and modern software engineering principles.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)

![Status](https://img.shields.io/badge/status-active-success.svg)

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Game Modes](#-game-modes)
- [Technical Det,ls](#-technical-det,ls)
- [Project Structure](#-project-structure)
- [Testing](#-testing)
- [Contributing](#-contributing)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)
- 

## ✨ Features

- 🤖 **Unbeatable ,** - Implements minimax algorithm for optimal gameplay
- 👥 **Multiple Game Modes** - Play ag,nst another human or challenge the ,
- 📊 **Statistics Tracking** - Persistent game statistics saved to JSON
- ✅ **Input Validation** - Robust error handling for all user inputs
- 🎨 **Clean Interface** - Intuitive terminal-based UI with clear visuals
- 🏗️ **Modular Design** - Well-organized code following SOLID principles
- 📝 **Comprehensive Documentation** - Det,led docstrings and comments
- 💾 **Data Persistence** - Game history saved across sessions

## 🎬 Demo

```
   TIC TAC TOE

     0   1   2
  0  X | O |  
    -----------
  1    | X | O
    -----------
  2  O |   | X

Hariom (X), enter row,col (e.g., 0,1): 2,1
```

## 🏛️ Architecture

The project follows a modular architecture with clear separation of concerns:

```
┌─────────────────────────────────────────┐
│       GameController (M,n Loop)         │
│         - Orchestrates gameplay          │
└──────────────┬──────────────────────────┘
               │
       ┌───────┴───────┐
       │               │
┌──────▼──────┐ ┌─────▼──────┐
│    Board    │ │ GameLogic  │
│  Management │ │Win Detection│
└─────────────┘ └────────────┘
       │               │
┌──────▼───────────────▼──────┐
│     Player Management        │
│  (Human/, with Minimax)     │
└──────────────┬───────────────┘
               │
       ┌───────▼────────┐
       │   Statistics   │
       │  (Persistence) │
       └────────────────┘
```

### 📦 Modules

1. **Board Management** - Handles game board state and operations
2. **Game Logic** - Win detection and game state evaluation
3. **Player Management** - Abstract player classes with Human and , implementations
4. **Statistics** - Tracks and persists game data to JSON
5. **Game Controller** - M,n orchestrator coordinating all components

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses Python standard library only)

### Steps

1. Clone the repository:
```bash
https://github.com/hariom25mim10029-lang/tic_tac_toe.git
cd tictactoe
```

2. Run the game:
```bash
python tic_tac_toe.py
```

That's it! No additional setup needed.

## 🎯 Usage

### Starting the Game

```bash
python tic_tac_toe.py
```

### M,n Menu Options

```
=== TIC TAC TOE SETUP ===
1. Player vs Player
2. Player vs ,
3. View Statistics
4. Exit
```

### Making Moves

Enter moves in the format `row,col` where both row and column are numbers from 0-2:

```
Hariom (X), enter row,col (e.g., 0,1): 1,1
```

**Board Coordinates:**
```
     0   1   2
  0  • | • | •
    -----------
  1  • | • | •
    -----------
  2  • | • | •
```

### Example Game Session

```bash
$ python tictactoe.py

========================================
   WELCOME TO TIC TAC TOE
========================================

=== TIC TAC TOE SETUP ===
1. Player vs Player
2. Player vs ,
3. View Statistics
4. Exit

Select option (1-4): 2
Your name: Hariom

   TIC TAC TOE
     0   1   2
  0    |   |  
    -----------
  1    |   |  
    -----------
  2    |   |  

Hariom (X), enter row,col: 1,1
, is thinking...

# Game continues...

🎉 Hariom WINS!

Play ag,n? (y/n): n

=== GAME STATISTICS ===
Total Games: 1
X Wins: 1
O Wins: 0
Draws: 0
========================
```

## 🕹️ Game Modes

### 1. Player vs Player
Two human players take turns playing as X and O. Perfect for:
- Playing with friends
- Teaching others the game
- Local multiplayer fun

### 2. Player vs ,
Challenge an unbeatable , opponent that uses the minimax algorithm. The ,:
- Never makes mistakes
- Always plays optimally
- Will win or draw every game
- Provides a challenging experience

### 3. View Statistics
Access det,led statistics including:
- Total games played
- X wins count
- O wins count
- Number of draws
- Persistent across sessions





**Key Features:**
- **Time Complexity:** O(b^d) where b=branching factor, d=depth
- **Space Complexity:** O(d) for recursion stack
- **Optimization:** Depth-based scoring (10-depth) for efficiency
- **Result:** Guaranteed optimal play

### Design Patterns Used

- **Strategy Pattern** - Different player types (Human/,)
- **Abstract Base Class** - Player interface
- **Single Responsibility** - Each class has one clear purpose
- **Dependency Injection** - Components loosely coupled

### Data Structures

- **Board:** 2D list (3×3 matrix) for O(1) access
- **Statistics:** JSON file for platform-independent persistence

## 📁 Project Structure

```
tictactoe/
│
├── tictactoe.py          # M,n application file (~350 lines)
│   ├── Board             # Board management class
│   ├── GameLogic         # Win detection logic
│   ├── Player            # Abstract player class
│   ├── HumanPlayer       # Human player implementation
│   ├── ,Player          # , with minimax algorithm
│   ├── Statistics        # Data persistence
│   └── GameController    # M,n game orchestrator
│
├── stats.json            # Game statistics (auto-generated)
├── README.md             # This file
├── LICENSE               # MIT License
└── .gitignore            # Git ignore file
```

## 🧪 Testing

### Manual Test Cases

#### Board Management
- ✅ Valid move placement
- ✅ Invalid move (out of bounds)
- ✅ Invalid move (occupied cell)
- ✅ Board full detection
- ✅ Board reset functionality

#### Win Detection
- ✅ Row wins (all 3 rows)
- ✅ Column wins (all 3 columns)
- ✅ Diagonal wins (both diagonals)
- ✅ Draw detection
- ✅ Game in progress state

#### , Behavior
- ✅ Blocks opponent's winning move
- ✅ Takes av,lable winning move
- ✅ Plays optimally in all scenarios
- ✅ Never loses (always wins or draws)

#### Input Validation
- ✅ Valid input format (e.g., "1,2")
- ✅ Invalid format handling
- ✅ Out of bounds detection
- ✅ Occupied cell prevention

### Running Tests

Currently, the project uses manual testing. To test:

```bash
python tictactoe.py
```

Then follow test scenarios in each mode.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to new functions/classes
- Update README if adding new features
- Test thoroughly before submitting
- Write clear commit messages

## 🚧 Future Enhancements

### Planned Features

- [ ] **GUI Implementation** - Tkinter or Pygame interface
- [ ] **Network Multiplayer** - Play online with friends
- [ ] **Difficulty Levels** - Easy/Medium/Hard , modes
- [ ] **Larger Boards** - Support for 4×4, 5×5 grids
- [ ] **Undo Feature** - Take back moves
- [ ] **Move History** - Complete game replay
- [ ] **Player Profiles** - Individual player statistics
- [ ] **Tournament Mode** - Best-of-N series
- [ ] **Theme Customization** - Different visual themes
- [ ] **Sound Effects** - Audio feedback for moves
- [ ] **Unit Tests** - Automated test suite
- [ ] **CLI Arguments** - Command-line configuration

### Ideas Welcome!

Have an idea? Open an issue or submit a pull request!

## 👨‍💻 Author

**Hariom Jamliya**
- Roll Number: 25MIM10029
- GitHub: https://github.com/hariom25mim10029-lang



## 🙏 Acknowledgments

- Inspired by the classic Tic Tac Toe game
- Minimax algorithm concept from , literature
- Python community for excellent documentation
- Contributors and testers

## 📊 Project Stats

![Lines of Code](https://img.shields.io/badge/lines%20of%20code-350+-brightgreen)
![Modules](https://img.shields.io/badge/modules-5-blue)
![Classes](https://img.shields.io/badge/classes-7-orange)



## ⭐ Star History

If you find this project useful, please consider giving it a star!

---

<div align="center">

**Made with ❤️ by Hariom Jamliya**

[⬆ Back to Top](#-tic-tac-toe-game)

</div>
