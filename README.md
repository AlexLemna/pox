# Pox

My attempt at crafting an interpreter for the Lox programming language in Python, following the wonderful *Crafting Interpreters* ([full-text website](craftinginterpreters.com), [GitHub repository](https://github.com/munificent/craftinginterpreters)) by Robert Nystrom.

For this first implementation, I've decided to keep the code as close as possible to the Java code that Nystrom originally used.

When I get stuck or need inspiration, I'm referring to:

- [FallenDeity's LoxInterpreter](https://github.com/FallenDeity/LoxInterpreter)
- [ImAKappa's pylox](https://github.com/ImAKappa/pylox)
- [MtScience's PyLox](https://github.com/MtScience/PyLox)
- plus lots of other [Lox implementations](https://github.com/munificent/craftinginterpreters/wiki/Lox-Implementations)

## Current progress

- [x] [**Chapter 4: Scanning**](http://www.craftinginterpreters.com/scanning.html). 
  - [x] *4.1: The Interpreter Framework*
  - [x] *4.2: Lexemes and Tokens*
  - *4.3 Regular Languages and Expressions* (*no code*)
  - [x] *4.4: The Scanner Class*
  - [x] *4.5: Recognizing Lexemes*
  - [x] *4.6: Longer Lexemes*
  - [x] *4.7: Reserved Words and Identifiers*

- [x] [**Chapter 5: Representing Code**](http://www.craftinginterpreters.com/representing-code.html)
  - *5.1: Context-Free Grammers* (*no code*)
  - [x] 5.2: Implementing Syntax Trees
  - [x] 5.3: Working with Trees
  - [x] 5.4: A (Not Very) Pretty Printer

- [ ] [**Chapter 6: Parsing Expressions**](http://www.craftinginterpreters.com/parsing-expressions.html)
  - [ ] 6.1: Ambiguity and the Parsing Game
  - [ ] 6.2: Recursive Descent Parsing
  - [ ] 6.3: Syntax Errors
  - [ ] 6.4: Wiring up the Parser

- [ ] [**Chapter 7: Evaluating Expressions**](http://www.craftinginterpreters.com/evaluating-expressions.html)
  - [ ] 7.1: Representing Values
  - [ ] 7.2: Evaluating Expressions
  - [ ] 7.3: Runtime Errors
  - [ ] 7.4: Hooking Up the Interpreter

- [ ] [**Chapter 8: Statements and State**](http://www.craftinginterpreters.com/statements-and-state.html)
  - [ ] 8.1: Statements
  - [ ] 8.2: Global Variables
  - [ ] 8.3: Environments
  - [ ] 8.4: Assignment
  - [ ] 8.5: Scope

- [ ] [**Chapter 9: Control Flow**](http://www.craftinginterpreters.com/control-flow.html)
  - [ ] 9.1: Turing Machines (Briefly)
  - [ ] 9.2: Conditional Execution
  - [ ] 9.3: Logical Operators
  - [ ] 9.4: While Loops
  - [ ] 9.5: For Loops
 
- [ ] [**Chapter 10: Functions**](http://www.craftinginterpreters.com/functions.html)
  - [ ] 10.1: Function Calls
  - [ ] 10.2: Native Functions
  - [ ] 10.3: Function Declarations
  - [ ] 10.4: Function Objects
  - [ ] 10.5: Return Statements
  - [ ] 10.6: Local Functions and Closures
 
- [ ] [**Chapter 11: Resolving and Binding**](http://www.craftinginterpreters.com/resolving-and-binding.html)
  - [ ] 11.1: Static Scope
  - [ ] 11.2: Semantic Analysis
  - [ ] 11.3: A Resolver Class
  - [ ] 11.4: Interpreting Resolved Variables 
  - [ ] 11.5: Resolution Errors

- [ ] [**Chapter 12: Classes**](http://www.craftinginterpreters.com/classes.html)
  - [ ] 12.1: OOP and Classes
  - [ ] 12.2: Class Declarations
  - [ ] 12.3: Creating Instances
  - [ ] 12.4: Properties on Instances
  - [ ] 12.5: Methods on Classes
  - [ ] 12.6: This
  - [ ] 12.7: Constructors and Initializers

- [ ] [**Chapter 13: Inheritance**](http://www.craftinginterpreters.com/inheritance.html)
  - [ ] 13.1: Superclasses and Subclasses
  - [ ] 13.2: Inheriting Methods
  - [ ] 13.3: Calling Superclass Methods
  - [ ] 13.4: Conclusion
 