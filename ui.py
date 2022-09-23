from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # WINDOW CREATION
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # CANVAS CREATION
        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Some question text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # SCORE LABEL CREATION
        self.score_label = Label(text=self.quiz.score, highlightthickness=0, bg=THEME_COLOR, fg="white",
                                 font=("Arial", 16, "bold"))
        self.score_label.grid(column=1, row=0)

        # BUTTON CREATION
        self.true_image = PhotoImage(file="./images/true.png")
        self.false_image = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_command)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_command)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        # MAIN LOOP
        self.window.mainloop()

    def get_next_question(self):
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz game.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_command(self):
        self.return_feedback(self.quiz.check_answer("True"))

    def false_command(self):
        is_false = self.quiz.check_answer("False")
        self.return_feedback(is_false)

    def return_feedback(self, is_false):
        if is_false:
            self.canvas.config(bg="green")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        else:
            self.canvas.config(bg="red")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.window.after(3000, self.get_next_question)
