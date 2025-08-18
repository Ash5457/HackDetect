# Contributing to HackDetect

Thanks for your interest in contributing to HackDetect! This document provides guidelines and information for contributors.

## 🤝 Ways to Contribute

### Bug Reports
- Use the GitHub issue tracker to report bugs
- Include detailed steps to reproduce the issue
- Mention your operating system and Python version
- Provide terminal screenshots if relevant

### Feature Requests
- Submit feature ideas through GitHub issues
- Explain the use case and potential impact
- Consider backward compatibility
- Be open to discussion and refinement

### Code Contributions
- Fork the repository and create a feature branch
- Follow the coding standards outlined below
- Write tests for new functionality
- Update documentation as needed

### Documentation
- Improve existing documentation
- Add code comments for complex logic
- Create tutorials or examples
- Fix typos and clarify instructions

## 🚀 Getting Started

### Development Environment Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/yourusername/hackdetect.git
   cd hackdetect
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv dev-env
   source dev-env/bin/activate  # On Windows: dev-env\Scripts\activate
   ```

3. **Install development dependencies**
   ```bash
   pip install colorama
   # Add other dev dependencies as needed
   ```

4. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 Coding Standards

### Python Style Guidelines
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Keep functions focused and reasonably sized
- Add docstrings for classes and complex functions

### Code Structure
- Maintain the existing class structure
- Keep UI logic separate from game logic
- Use type hints where appropriate
- Handle errors gracefully

### Example Code Style
```python
class ExampleClass:
    """Brief description of the class."""
    
    def __init__(self, param: str) -> None:
        """Initialize with parameter."""
        self.param = param
    
    def process_data(self, data: list) -> dict:
        """Process input data and return results."""
        # Implementation here
        pass
```

## 🧪 Testing

### Running Tests
```bash
python -m pytest tests/
```

### Test Coverage
- Write unit tests for new functions
- Test edge cases and error conditions
- Ensure terminal UI components work across platforms
- Test multiplayer scenarios

### Manual Testing
- Test on different operating systems
- Verify terminal compatibility
- Check game balance and playability
- Validate user experience flows

## 📋 Pull Request Process

### Before Submitting
1. Ensure your code follows the style guidelines
2. Run all tests and verify they pass
3. Update documentation if needed
4. Test your changes thoroughly

### Pull Request Guidelines
1. **Clear Description**: Explain what your PR does and why
2. **Reference Issues**: Link to relevant issue numbers
3. **Small, Focused Changes**: Keep PRs manageable in scope
4. **Update CHANGELOG**: Add your changes to the changelog
5. **Screenshots**: Include terminal screenshots for UI changes

### PR Template
```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing
- [ ] Tested on Windows/macOS/Linux
- [ ] All existing tests pass
- [ ] Added new tests if applicable

## Screenshots
Include screenshots for UI-related changes.
```

## 🐛 Issue Guidelines

### Bug Reports Should Include
- **Environment**: OS, Python version, terminal type
- **Steps to Reproduce**: Detailed, numbered steps
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Screenshots**: Terminal output if relevant

### Feature Requests Should Include
- **Problem Statement**: What issue does this solve?
- **Proposed Solution**: How should it work?
- **Alternatives**: Other approaches considered
- **Additional Context**: Any other relevant information

## 🎮 Game Design Considerations

### Balance and Gameplay
- Consider impact on game balance
- Ensure changes work for different player counts
- Maintain the social deduction core mechanics
- Preserve the hacker/cybersecurity theme

### User Experience
- Keep the terminal interface intuitive
- Maintain the Matrix/hacker aesthetic
- Ensure accessibility across different terminals
- Consider players with varying technical backgrounds

## 🔧 Areas That Need Help

### High Priority
- [ ] Network multiplayer implementation
- [ ] Save/load game state functionality
- [ ] Performance optimizations for large terminals
- [ ] Cross-platform terminal compatibility testing

### Medium Priority
- [ ] AI player opponents
- [ ] Custom scenario editor
- [ ] Statistics and analytics dashboard
- [ ] Mobile terminal client support

### Low Priority
- [ ] Plugin system for custom roles
- [ ] Tournament mode
- [ ] Localization support
- [ ] Advanced visual effects

## 📚 Resources

### Learning Materials
- [Python PEP 8 Style Guide](https://pep8.org/)
- [Colorama Documentation](https://pypi.org/project/colorama/)
- [Terminal Escape Sequences](https://en.wikipedia.org/wiki/ANSI_escape_code)

### Game Design References
- Among Us mechanics and social deduction principles
- Classic hacker film aesthetics (The Matrix, WarGames)
- Terminal-based game design patterns

## 💬 Communication

### Getting Help
- Create an issue for questions about contributing
- Join discussions on existing issues and PRs
- Be respectful and constructive in all interactions

### Code Review Process
- All contributions require code review
- Reviews focus on code quality, functionality, and game balance
- Be open to feedback and suggestions
- Reviewers should provide constructive, helpful comments

## 🏆 Recognition

Contributors will be recognized in:
- The project README
- Release notes for significant contributions
- GitHub contributor statistics

Thank you for helping make HackDetect better!
