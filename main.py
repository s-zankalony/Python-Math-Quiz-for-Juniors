import random
from flashy_text import flashy_text


def generate_random_number():
    return random.randint(1, 10)

def add(num1,num2):
  return num1+num2
def subtract(num1,num2):
  return num1-num2
def multiply(num1,num2):
  return num1*num2
def divide(num1,num2):
  return num1/num2

def swap(a,b):
  # Swap the values
  a, b = b, a
  # Return the swapped values
  return a, b

def quiz():
  print("==========================")
  print("Welcome to Math Quiz for Juniors!")
  print("==========================")
  print("Please select an operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")

  choice = input("Enter your choice (1/2/3/4): ")
  num1 = generate_random_number()
  num2 = generate_random_number()
  if choice == '1':
    result = add(num1, num2)
    print(f"What is {num1} + {num2}?")
    answer = int(input("Enter your answer: "))
    if answer == result:
      flashy_text("Correct!", "green", "white")
    else:
      flashy_text("Incorrect!", "red", "white")
      print("Incorrect. The correct answer is", result)
  elif choice == '2':
    if num1 < num2:
      num1, num2 = swap(num1, num2)
    result = subtract(num1, num2)
    print(f"What is {num1} - {num2}?")
    answer = int(input("Enter your answer: "))
    if answer == result:
      flashy_text("Correct!", "green", "white")
    else:
      flashy_text("Incorrect!", "red", "white")
      print("Incorrect. The correct answer is", result)
  elif choice == '3':
      result = multiply(num1, num2)
      print(f"What is {num1} * {num2}?")
      answer = int(input("Enter your answer: "))
      if answer == result:
        flashy_text("Correct!", "green", "white")
      else:
        flashy_text("Incorrect!", "red", "white")
        print("Incorrect. The correct answer is", result)
  elif choice == '4':
      if num2 == 0:
        num2 = generate_random_number()
      while num1 % num2 != 0:
        num1 = generate_random_number()
        num2 = generate_random_number()
      result = divide(num1, num2)
      print(f"What is {num1} / {num2}?")
      answer = float(input("Enter your answer: "))
      if answer == result:
        flashy_text("Correct!", "green", "white")
      else:
        flashy_text("Incorrect!", "red", "white")
        print("Incorrect. The correct answer is", result)
  else:
      print("Invalid input. Please try again.")

  print("Do you want to play again? (y/n)")
  play_again = input()
  if play_again.lower() == "y":
    quiz()
  else:
    print("Thank you for playing!")

def main():
  quiz()

  


if __name__ == '__main__':
  main()
  