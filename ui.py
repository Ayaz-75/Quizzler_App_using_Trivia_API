from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=20, pady=20)
        self.window.config(bg=THEME_COLOR)


        self.score_label = Label(text=f"Score: 0", foreground="white", background=THEME_COLOR, font=("Arial" ,15, "italic"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.quote_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Some text",
            fill=THEME_COLOR,
            font=("Arial" ,20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        true_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=true_image, highlightthickness=0, command=self.is_true)
        self.right_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=false_image, highlightthickness=0, command=self.is_false)
        self.wrong_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text, text=q_text)

        else:
            self.canvas.itemconfig(self.quote_text, text=f"You have reached the end of quiz")

            self.right_button.config(state="disabled")
            self.right_button.config(state="disabled")


    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)

