quiz_data = {
    "What is the name of the tallest mountain?": "everest",
    "What is my name?": "sanjog",
    "Which company am I interning at?": "broadway",
    "Which district am I currently staying in?": "kathmandu",
    "Which district is my village located in?": "parbat"
}

print("*" * 10 + " Quiz Starts " + "*" * 10)
counter = 0

for question, correct_answer in quiz_data.items():
    user_answer = input(f"{question} = ")
    
    if user_answer.lower() == correct_answer:
        print("Correct!")
        counter += 1
    else:
        print(f"Wrong! (Answer was: {correct_answer})")

print("*" * 10 + f" Your score = {counter} " + "*" * 10)