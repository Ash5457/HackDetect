# HackDetect: Trust No One, Not Even Your Terminal

![HackDetect Logo](https://github.com/Ash5457/HackDetect/blob/main/Logo.png)

A cybersecurity-themed social deduction game that combines the paranoia of Among Us with the aesthetic of classic hacker films. Built entirely in Python with a terminal-based interface that makes you feel like you're investigating a real cyber attack.

## 🎮 Game Overview

**HackDetect** is a multiplayer social deduction game where players take on the roles of security analysts investigating a breach in their organization's systems. One player might secretly be the hacker causing the breach, or the threat might be coming from an external source entirely. Players must analyze clues, share intelligence, and make accusations before it's too late.

### 🎯 Key Features

- **🕵️ Social Deduction Mechanics**: Hidden roles create tension and paranoia
- **💻 Authentic Hacker Aesthetic**: Matrix-style terminal interface with ASCII art
- **🔍 Dynamic Clue System**: Procedurally generated evidence that tells a story
- **👥 Multiplayer Support**: 2-8 players with scalable game mechanics
- **🎭 Dual Role Gameplay**: Play as either a security analyst or the hacker
- **🌐 External Threat Option**: Not all threats come from within
- **📊 Advanced Game States**: Corruption, planted evidence, and counter-surveillance

## 🖼️ Screenshots

### Player Interface
![Clue Interface](https://github.com/Ash5457/HackDetect/blob/main/HackDetect(Final%20Project)/Images/Clue_Interface.png)
*Standard security analyst interface showing available actions, system status, and progress tracking*

### Hacker Interface
![Hacker Menu](https://github.com/Ash5457/HackDetect/blob/main/HackDetect(Final%20Project)/Images/Hacker_Menu.png)
*The hacker's secret interface with backdoor capabilities and malicious action options*

### Security Breach Investigation
![Scan Security Breach](https://github.com/Ash5457/HackDetect/blob/main/HackDetect(Final%20Project)/Images/Scan_Security_Breach.png)
*Players can scan for security breaches, discovering suspicious activity with Matrix-style visual effects*

### False Evidence Planting
![False Evidence](https://github.com/Ash5457/HackDetect/blob/main/HackDetect(Final%20Project)/Images/False_Evidence.png)
*Hackers can plant false evidence to frame innocent players and mislead the investigation*

## 🎲 How to Play

### For Security Analysts
1. **Investigate**: Scan system logs for suspicious activity
2. **Analyze**: Review collected clues for patterns and connections
3. **Collaborate**: Share intelligence with other players (or don't...)
4. **Deduce**: Submit breach analysis reports when you think you've found the threat

### For the Hacker (if selected)
1. **Sabotage**: Plant false evidence pointing to innocent players
2. **Corrupt**: Damage other players' collected evidence
3. **Evade**: Use counter-surveillance to avoid detection
4. **Deceive**: Blend in with legitimate investigators while sowing chaos

### Win Conditions
- **Analysts Win**: Correctly identify the hacker or external threat source
- **Hacker Wins**: Remain undetected for 10 rounds OR mislead analysts into wrong accusations

## 🛠️ Technical Implementation

### Architecture
- **Language**: Python 3.8+
- **UI Framework**: Custom terminal interface using `colorama`
- **Game Logic**: Object-oriented design with modular components
- **Clue Generation**: Deterministic procedural system using player-specific seeds
- **State Management**: Comprehensive tracking of player states, evidence, and game progression

### Key Components
- **`ClueSystem`**: Generates contextual cybersecurity evidence
- **`EnhancedUI`**: Manages terminal effects, colors, and visual feedback
- **`Player`**: Tracks individual game state, clues, and special abilities
- **`HackerGame`**: Core game loop and logic management

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Terminal that supports ANSI color codes
- Minimum terminal width of 90 characters (recommended: 120+)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hackdetect.git
   cd hackdetect
   ```

2. **Install dependencies**
   ```bash
   pip install colorama
   ```

3. **Run the game**
   ```bash
   python hackdetect.py
   ```

### System-Specific Instructions

#### Windows
```bash
# Install Python from python.org if not already installed
pip install colorama
python hackdetect.py
```

#### macOS
```bash
# Using Homebrew (recommended)
brew install python3
pip3 install colorama
python3 hackdetect.py
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install colorama
python3 hackdetect.py
```

### Virtual Environment Setup (Recommended)
```bash
python -m venv hackdetect-env
source hackdetect-env/bin/activate  # On Windows: hackdetect-env\Scripts\activate
pip install colorama
python hackdetect.py
```

## 🎮 Game Setup

1. **Launch the game**
2. **Choose number of players** (2-8 supported)
3. **Enable external threats** (optional - adds uncertainty about threat source)
4. **Enter player codenames** when prompted
5. **Begin investigation!**

### Multiplayer Setup
- All players share the same computer
- Players take turns and look away during others' turns
- Game prompts when to switch players
- Private information is hidden between turns

## 🧠 Game Design Philosophy

### Influenced by Game Studies Theory
- **Mechanics**: Hidden information, time pressure, unreliable data
- **Dynamics**: Paranoia, cooperation, deception
- **Aesthetics**: Tension, mystery, social interaction

### Player Types Supported (Bartle Taxonomy)
- **Achievers**: Focus on collecting the most clues
- **Explorers**: Try to understand the clue generation system
- **Socializers**: Engage in discussion and alliance-building  
- **Killers**: (If hacker) Mislead and eliminate other players

## 📋 Features Deep Dive

### Advanced Hacker Abilities
- **False Evidence Planting**: Create misleading clues targeting innocent players
- **Log Corruption**: Make collected evidence unreadable
- **Counter-Surveillance**: Deploy honeypots, access blocks, and communication jamming
- **Intelligence Interception**: Monitor other players' activities

### Clue System
- **Contextual Generation**: Clues reference real cybersecurity concepts
- **Player-Specific**: Each player sees unique evidence based on deterministic seeds
- **Pattern Recognition**: Players can combine analysis for deeper insights
- **Multiple Attack Vectors**: Data theft, system breaches, insider threats, network anomalies

### UI/UX Features
- **Matrix Rain Effect**: Atmospheric scrolling character animations
- **Glitch Effects**: Text corruption for dramatic emphasis
- **Color-Coded Alerts**: Visual feedback system for different message types
- **Progress Tracking**: Visual indicators for game state and player progress

## 🔧 Configuration Options

### Game Variables (configurable in code)
```python
MAX_ROUNDS = 10                    # Game duration
EXTERNAL_HACKER_CHANCE = 0.45      # Probability of external vs internal threat
PLANTED_EVIDENCE_CHANCE = 0.3      # Likelihood of finding false evidence
CLUE_CORRUPTION_RATE = 0.3         # Character corruption percentage
```

### Display Options
- Terminal width detection and adjustment
- Customizable color schemes via colorama
- Adjustable animation speeds
- Debug logging option

## 📊 Game Analytics & Balancing

### Metrics Tracked
- Player discovery rates
- False accusation frequency  
- Hacker success rates by strategy
- Game duration statistics

### Balance Considerations
- Clue-to-player ratios
- Evidence corruption rates
- Counter-surveillance effectiveness
- Information sharing incentives

## 🐛 Troubleshooting

### Common Issues

**Terminal too narrow**
- Resize terminal to at least 90 characters wide
- Game will display error message if too narrow

**Colors not displaying**
- Ensure terminal supports ANSI color codes
- Try different terminal applications (Windows Terminal, iTerm2, etc.)

**Python import errors**
- Verify Python 3.8+ installation: `python --version`
- Install colorama: `pip install colorama`
- Check virtual environment activation

**Game crashes/freezes**
- Check terminal size and compatibility
- Review hackdetect.log for error details
- Restart with fresh terminal session

## 🚧 Future Enhancements

### Planned Features
- [ ] Network multiplayer support
- [ ] Save/load game states  
- [ ] Custom scenario editor
- [ ] Statistics dashboard
- [ ] AI player opponents
- [ ] Mobile terminal client
- [ ] Tournament mode

### Technical Improvements
- [ ] Configuration file support
- [ ] Plugin architecture for custom roles
- [ ] Performance optimizations
- [ ] Cross-platform packaging
- [ ] Automated testing suite

## 🤝 Contributing

Contributions welcome! Please see [CONTRIBUTING.md](https://github.com/Ash5457/HackDetect/blob/main/HackDetect(Final%20Project)/CONTRIBUTING.md) for guidelines.

### Development Setup
```bash
git clone https://github.com/yourusername/hackdetect.git
cd hackdetect
python -m venv dev-env
source dev-env/bin/activate
pip install -r requirements-dev.txt
python -m pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Ash5457/HackDetect/blob/main/LICENSE%20(MIT)) file for details.

## 🙏 Acknowledgments

- Inspired by Among Us and classic hacker cinema
- Built with Python and colorama
- Game design influenced by academic game studies
- ASCII art and terminal aesthetics inspired by The Matrix

## 📞 Contact

**Developer**: Akash Bahl  
**Email**: akashbahl1926@gmail.com  
**LinkedIn**: https://www.linkedin.com/in/akash-bahl-akb5457/  
**Portfolio**: [Work-in-Progress...]

---

*"In cybersecurity, trust is a luxury you can't afford. In HackDetect, it might be the key to survival."*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Terminal](https://img.shields.io/badge/Interface-Terminal-green.svg)]()
