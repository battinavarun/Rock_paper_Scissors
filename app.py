from flask import Flask, render_template, request
import random

app = Flask(__name__)

game_images = {
    "rock": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "paper": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    "scissors": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
}

choices = ["rock", "paper", "scissors"]

@app.route("/", methods=["GET", "POST"])
def game():
    user_choice = None
    computer_choice = None
    result = None

    if request.method == "POST":
        user_choice = request.form["choice"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a Draw!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You Win! 🎉"
        else:
            result = "You Lose! 😢"

    return render_template("index.html", user_choice=user_choice, computer_choice=computer_choice, result=result, game_images=game_images)

if __name__ == "__main__":
    app.run(debug=True)
