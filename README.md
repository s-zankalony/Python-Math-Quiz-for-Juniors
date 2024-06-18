# Math Quiz for Juniors

## Overview

**Math Quiz for Juniors** is a simple command-line program designed to help young learners practice basic arithmetic operations. The program generates random math questions and provides immediate feedback on the correctness of the answers.

## Features

- Generates random numbers for arithmetic questions.
- Supports four basic arithmetic operations: addition, subtraction, multiplication, and division.
- Provides immediate feedback with colorful text.
- Allows the user to play multiple rounds of the quiz.

## Requirements

- Python 3.x
- `flashy_text` module (included in the repo)

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python 3.x installed on your system.

## Usage

To run the quiz, execute the script using Python:

```sh
python math_quiz.py
```

Follow the on-screen instructions to select an arithmetic operation and answer the questions.

## Functions

### `generate_random_number()`
Generates a random integer between 1 and 10.

### `add(num1, num2)`
Returns the sum of `num1` and `num2`.

### `subtract(num1, num2)`
Returns the difference between `num1` and `num2`.

### `multiply(num1, num2)`
Returns the product of `num1` and `num2`.

### `divide(num1, num2)`
Returns the quotient of `num1` divided by `num2`.

### `swap(a, b)`
Swaps the values of `a` and `b` and returns the swapped values.

### `quiz()`
Main function for the quiz, handles user interaction, generates questions, and checks answers.

### `main()`
Entry point of the script, calls the `quiz()` function.

## Example

When you run the script, you will see the following prompts:

```
==========================
Welcome to Math Quiz for Juniors!
==========================
Please select an operation:
1. Add
2. Subtract
3. Multiply
4. Divide
Enter your choice (1/2/3/4): 
```

After selecting an operation, the program will generate a question. For example:

```
What is 3 + 5?
Enter your answer: 
```

If you answer correctly, you will see a "Correct!" message in green text. If the answer is incorrect, you will see an "Incorrect!" message in red text, along with the correct answer.

You will then be asked if you want to play again. Type "y" to continue or "n" to exit the program.

## License

This project is licensed under the MIT License.

## Acknowledgements

- `flashy_text` module for colorful text feedback, included in this repository.

Enjoy the quiz and happy learning!