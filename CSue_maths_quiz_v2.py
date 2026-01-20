# Name: CSue_maths_quiz_v2
# Purpose: Math Game For Primary Students
# Version: 2
# Author: Carlos Sue
# Date: 17/01/2026

"""
Using Tkinter to create a maths game with a GUI.

The game is aimed towards primary students, so it
needs to be aesthetically pleasing.

User will be greeted by a login screen and asked for their name.
Followed by the game difficulty level mode selection.
And finally the maths game will begin, as 5 questions are generated.

At the end of the game, results and score will be displayed.
The user may choose to play again.

PLayers named and score will be written to an external file.
"""

# Import libraries.
from tkinter import *
from random import randint

# Set up list to store answers and track game rounds.
list_answers = []
list_user_answers = []
list_game_rounds = []

# Commonly used headings and subheading text.
CON_SUBHEADING = "TeKura | Primary Mathematics"
h1 = ("Lexend", 14, "normal")
h2 = ("Lexend", 15, "bold")


def quit():
    """Close tkinter window."""
    root.destroy()


def quit_button():
    """Generate a quit button.

    Helps to limit and reduce repetitive code.
    """
    return Button(root, text="Quit", bg="#dd3d3d", fg="white",
                  activebackground="#9b111e", activeforeground="white",
                  font=h2, command=quit)


def instructions():
    """Display the maths game instructions."""
    h3 = ("Lexend", 18, "normal")  # Commonly used font style

    canvas1.delete("all")

    canvas1.create_text(1180, 30,
                        text=CON_SUBHEADING, font=h1)  # Subheading text

    # Quit and Play buttons.
    canvas1.create_window(170, 820, width=150, height=70, window=quit_button())

    canvas1.create_window(1180, 820, width=150, height=70,
                          window=(Button(root, text="Play",
                                         bg="#459843",
                                         fg="white",
                                         activebackground="#035718",
                                         activeforeground="white",
                                         font=h2,
                                         command=questions)))
    # Bind keys to buttons (questions, quit)
    root.bind("<Return>", lambda event: questions())
    root.bind("<F4>", lambda event: quit())

    # Instructions text
    canvas1.create_text(675, 170,
                        text="Instructions", font=("Lexend", 22, "bold"))
    canvas1.create_text(675, 280,
                        text="1. Start the game and you will be asked a series\
 of 5 simple addition questions.", font=h3)
    canvas1.create_text(675, 380,
                        text="2. For each question, take your time and double\
 check your answers before clicking next or hitting enter.", font=h3)
    canvas1.create_text(675, 480,
                        text="3. Continue answering the questions until\
 you've completed all 5.", font=h3)
    canvas1.create_text(675, 580, text="4. Once you have completed all the\
 questions, hit the submit button or enter to check answers.", font=h3)
    canvas1.create_text(675, 680, text="You may quit the game anytime\
 by hitting F4 on your keyboard.", font=("Lexend", 18, "bold"))


def questions():
    """Ask the player 5 addition maths questions."""
    global str_name

    # Convert user_name so it can be used as a string.
    user_name = str_name.get().title()

    # Find the number of rounds played by looking at the number of answers.
    game_round = len(list_user_answers)

    # Later used to calculate margins and spacing.
    list_game_rounds.append(game_round)

    # Generate the numbers and calculate the question answer.
    int_random_1 = randint(1, 500)
    int_random_2 = randint(1, 500)
    int_answer = int_random_1 + int_random_2

    # Clear canvas and entry box.
    canvas1.delete("all")
    question_entry.delete(0, END)

    canvas1.create_text(1180, 30,
                        text=CON_SUBHEADING, font=h1)  # Subheading text

    canvas1.create_text(500, 380, text="{}, what is {}\
 + {}?".format(user_name, int_random_1, int_random_2),
                        font=("Lexend", 18, "bold"))

    # Quit Button and entry box.
    canvas1.create_window(820, 380, width=320,
                          height=70, window=question_entry)
    canvas1.create_window(170, 820, width=150,
                          height=70, window=quit_button())

    # Repeatedly ask questions until game_round is 5.
    # If condition is not met, take user to process_answer defintion.
    if game_round != 5:
        # Bind enter key to next button (process_answer).
        root.bind("<Return>", lambda event: process_answer(int_answer))
        (canvas1.create_window(1180, 820, width=150, height=70,
                               window=(Button(root,
                                              text="Next", bg="#459843",
                                              fg="white",
                                              activebackground="#035718",
                                              activeforeground="white",
                                              font=h2,
                                              command=lambda:
                                              process_answer(int_answer)))))

    # If condition is met, the next button will take user to results.
    else:
        # Bind enter key to results button (results)
        root.bind("<Return>", lambda event: results())
        canvas1.create_window(1180, 820, width=150, height=70,
                              window=(Button(root,
                                             text="Results", bg="#459843",
                                             fg="white",
                                             activebackground="#035718",
                                             activeforeground="white",
                                             font=h2,
                                             command=results)))
    root.bind("<F4>", lambda event: quit())
    canvas1.update()


def process_answer(int_answer):
    """Process user answer.

    Reintiates the questions() definition.
    """
    global question_entry

    # Get the user input as a string.
    user_answer = question_entry.get().strip()

    # Convert answer into integer and add to list.
    list_user_answers.append(int(user_answer))

    list_answers.append(int_answer)

    questions()


def results():
    """Create the last graphic results page.

    Display the users answers and the correct answers.

    Record the users name and score in the external text file.
    """
    global str_name

    # Convert user_name so it can be used as a string.
    user_name = str_name.get().title()

    # Setting up variables.
    int_score = 0

    canvas1.delete("all")

    canvas1.create_text(1180, 30,
                        text=CON_SUBHEADING, font=h1)  # Subheading text

    for i in range(len(list_answers)):
        margin_y = (list_game_rounds[i]) * 80
        pad_y = 200

        answered_x = canvas1.winfo_width() * 0.32
        correct_x = canvas1.winfo_width() * 0.53
        result_x = canvas1.winfo_width() * 0.70

        h3 = ("Lexend", 15, "normal")  # Commonly used font style
        canvas1.create_text(answered_x, margin_y + pad_y,
                            text="Your answer was: {}"
                            .format(list_user_answers[i]),
                            font=h3, fill="green")
        if list_user_answers[i] == list_answers[i]:
            fill_color = "green"
            int_score = int_score + 1
        else:
            fill_color = "red"
        canvas1.create_text(correct_x,
                            margin_y + pad_y, text="The correct answer was {}."
                            .format(list_answers[i]),
                            font=h3, fill="red")

        if list_user_answers[i] == list_answers[i]:
            canvas1.create_text(result_x, margin_y + pad_y, text="Correct",
                                font=h3, fill=fill_color)
        else:
            canvas1.create_text(result_x, margin_y + pad_y, text="Incorrect",
                                font=h3, fill="red")

    # Quit and play again button.
    canvas1.create_window(170, 820, width=150, height=70, window=quit_button())

    canvas1.create_window(1180, 820, width=150, height=70,
                          window=(Button(root,
                                         text="Play Again",
                                         bg="#459843",
                                         fg="white",
                                         activebackground="#035718",
                                         activeforeground="white",
                                         font=h2,
                                         command=play_again)))
    # Bind keys to buttons (play again, quit)
    root.bind("<Return>", lambda event: play_again())
    root.bind("<F4>", lambda event: quit())
    canvas1.update()

    # Write the players name and score on the external file.
    text_file = open("txtfile.txt", "a")
    text_file.write("{} got {} questions correct.\n\n"
                    .format(user_name, int_score))
    text_file.close()


def play_again():
    """Close and reopen the program."""
    quit()
    main()


def main():
    """Set up the canvas and window size.

    Configure the tkinter GUI.

    Define the properties of entry boxes.
    """
    global root, canvas1, str_name, question_entry

    # Reset lists for when user plays again.
    list_answers.clear()
    list_user_answers.clear()
    list_game_rounds.clear()

    root = Tk()

    # Define the window name.
    root.title("Welcome to Carlos's Primary School Mathematics")

    # Dimensions for canvas size.
    canvas1 = Canvas(root, width=1350, height=900, bg="#e9ecef")

    canvas1.create_text(1180, 30,
                        text=CON_SUBHEADING, font=h1)  # Subheading text

    # Name entry box properties.
    str_name = Entry(root, font=("Lexend", 26, "normal"))

    # Question entry box properties.
    question_entry = Entry(root, font=("Lexend", 26, "normal"))

    # Quit and Next buttons.
    canvas1.create_window(170, 820, width=150, height=70, window=quit_button())
    canvas1.create_window(1180, 820, width=150, height=70,
                          window=(Button(root, text="Next",
                                         bg="#459843",
                                         fg="white",
                                         activebackground="#035718",
                                         activeforeground="white",
                                         font=h2,
                                         command=instructions)))
    # Bind keys to buttons (instructions, quit)
    root.bind("<Return>", lambda event: instructions())
    root.bind("<F4>", lambda event: quit())

    # Ask for players name.
    canvas1.create_text(500, 380,
                        text="Please enter your name:",
                        font=("Lexend", 18, "bold"))
    canvas1.create_window(820, 380, width=320, height=70, window=str_name)
    canvas1.pack()
    root.mainloop()


main()
