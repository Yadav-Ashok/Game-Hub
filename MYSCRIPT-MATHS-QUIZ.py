import random

def display():
    title =( "** A Simple Math Quiz **")
    print("*" * len(title))
    print(title)
    print("*" * len(title))

def display_option():
    option = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Integer Division", "5. Exit"]
    print(option[0])
    print(option[1])
    print(option[2])
    print(option[3])
    print(option[4])


def display_separator():
    print("-" * 24)


def user_input():
    user_input = int(input("Enter your choice: "))
    while user_input > 5 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input


def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input(" = "))
    return result


def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("Correct.")
        return count
    else:
        print("Incorrect.")
        return count


def menu_option(index, count):
    number_one = random.randrange(1, 30)
    number_two = random.randrange(1, 30)
    if index is 1:
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    if index is 2:
        problem = str(number_two) + " - " + str(number_one)
        solution = number_one - number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    if index is 3:
        problem = str(number_one) + " * " + str(number_two)
        solution = number_one * number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    if index is 4:
        problem = str(number_two) + " / " + str(number_one)
        solution = number_two // number_one
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count




def display_result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("You answered", total, "questions with", correct, "correct.")
    print("Your score is ", percentage, "%. Thank you.", sep = "")


def main():
    display()
    display_option()
    display_separator()

    option = user_input()
    total = 0
    correct = 0
    while option != 5:
        total = total + 1
        correct = menu_option(option, correct)
        option = user_input()

    print("Exit the quiz.")
    display_separator()
    display_result(total, correct)

main()
