# Contributing to TinyInterpreter

Thank you for your interest in contributing to TinyInterpreter! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### **Reporting Issues**
- Use the GitHub issue tracker to report bugs or request features
- Include detailed steps to reproduce bugs
- Provide sample code that demonstrates the issue
- Include your Python version and operating system

### **Suggesting Features**
- Open an issue with the "enhancement" label
- Describe the feature and its use case
- Consider how it fits with the Arabic programming language theme

### **Code Contributions**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass (`python Test.py`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to your branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 🏗️ Development Setup

### **Prerequisites**
- Python 3.6 or higher
- Git

### **Setup**
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/TinyArabicInterpreter.git
cd TinyArabicInterpreter

# Run tests to ensure everything works
python Test.py

# Test the REPL
python REPL.py
```

## 📋 Coding Standards

### **Code Style**
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and small

### **Documentation**
- Update README.md for user-facing changes
- Update ARCHITECTURE.md for architectural changes
- Add comments for complex logic
- Include examples in docstrings

### **Testing**
- Add tests for all new features
- Ensure error cases are tested
- Maintain test coverage for existing functionality
- Use the existing test framework in `Test.py`

## 🎯 Areas for Contribution

### **Language Features**
- New operators or functions
- Additional control flow constructs
- Data structures (arrays, dictionaries)
- Function definitions
- Import/export functionality

### **Error Handling**
- New error types
- Better error messages
- Error recovery mechanisms
- Warnings system

### **Tooling**
- Syntax highlighting
- Code formatter
- Debugger
- Performance profiler
- IDE integration

### **Documentation**
- Tutorials and examples
- Language specification
- API documentation
- Video tutorials

### **Testing**
- Additional test cases
- Performance benchmarks
- Integration tests
- Property-based testing

## 🔧 Architecture Guidelines

### **Visitor Pattern**
- All new AST nodes must implement the `accept(visitor)` method
- New visitors should extend the `Visitor` base class
- Keep evaluation logic in `InterpreterVisitor`

### **Error System**
- Use structured errors from `Errors.py`
- Include position information for all errors
- Provide helpful error messages

### **Position Tracking**
- All tokens must include position information
- AST nodes should carry position data
- Use `Position` class for line/column tracking

## 📝 Pull Request Guidelines

### **Before Submitting**
- [ ] All tests pass (`python Test.py`)
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] New features have tests
- [ ] No linting errors

### **PR Description**
- Describe what the PR does
- Reference any related issues
- Include screenshots for UI changes
- List any breaking changes

### **Review Process**
- Maintainers will review all PRs
- Address feedback promptly
- Keep PRs focused and small
- Respond to review comments

## 🐛 Bug Reports

### **Template**
```markdown
**Bug Description**
A clear description of the bug.

**To Reproduce**
Steps to reproduce the behavior:
1. Run '...'
2. Type '...'
3. See error

**Expected Behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment**
- Python version: [e.g. 3.9]
- OS: [e.g. Windows 10]
- TinyInterpreter version: [e.g. latest]

**Additional Context**
Any other context about the problem.
```

## 💡 Feature Requests

### **Template**
```markdown
**Feature Description**
A clear description of the feature.

**Use Case**
Why is this feature needed?

**Proposed Solution**
How should this feature work?

**Alternatives**
Other solutions you've considered.

**Additional Context**
Any other context or screenshots.
```

## 🎓 Learning Resources

### **Compiler Design**
- "Crafting Interpreters" by Robert Nystrom
- "Compilers: Principles, Techniques, and Tools" (Dragon Book)
- "Modern Compiler Implementation" by Andrew Appel

### **Python Best Practices**
- PEP 8 Style Guide
- Python Design Patterns
- Testing with Python

### **Arabic Language Processing**
- Unicode handling in Python
- Right-to-left text processing
- Arabic character encoding

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Code Review**: Ask for help in PR comments

## 🏆 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

---

Thank you for contributing to TinyInterpreter! 🎉
