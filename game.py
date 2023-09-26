import tkinter as tk
import random

# Create a list of children's rights questions
rights_questions = [
    "What is the right to education?",
    "What is the right to play?",
    "What is the right to be protected from violence?",
    "What is the right to express your opinion?",
    "What is the right to be treated with respect?",
]

# Create a list of possible answers for each question
rights_answers = [
    "The right to education is the right to go to school and learn.",
    "The right to play is the right to have fun and be creative.",
    "The right to be protected from violence is the right to be safe from harm.",
    "The right to express your opinion is the right to say what you think, even if others don't agree.",
    "The right to be treated with respect is the right to be treated fairly and with dignity.",
]

def play_game():
    # Choose a random question
    question = random.choice(rights_questions)

    # Set the question label text
    question_label.config(text=question)

    # Clear the answer entry box
    answer_entry.delete(0, tk.END)

    # Focus the answer entry box
    answer_entry.focus()

def check_answer():
    # Get the player's answer
    answer = answer_entry.get()

    # Check if the answer is correct
    if answer == rights_answers[rights_questions.index(question)]:
        feedback_label.config(text="Correct!")
    else:
        feedback_label.config(text="Incorrect. The correct answer is: " + rights_answers[rights_questions.index(question)])

# Create the Tkinter window
window = tk.Tk()
window.title("Children's Rights Game")

# Create the game frame
game_frame = tk.Frame(window)
game_frame.pack()

# Create the question label
question_label = tk.Label(game_frame, text="Question:")
question_label.pack()

# Create the answer entry box
answer_entry = tk.Entry(game_frame)
answer_entry.pack()

# Create the submit button
submit_button = tk.Button(game_frame, text="Submit", command=check_answer)
submit_button.pack()

# Create the feedback label
feedback_label = tk.Label(game_frame, text="")
feedback_label.pack()

# Start the game
play_game()

# Start the mainloop
window.mainloop()