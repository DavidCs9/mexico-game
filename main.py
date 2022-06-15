import turtle
import pandas

screen = turtle.Screen()
screen.title("Mexico Game")
image = "mexico.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("mexico-x-y.csv")
state_names = data.estado.to_list()
guessed_states = []
missing_states = []

while len(guessed_states) < 32:
    answer = screen.textinput(
        f"{len(guessed_states)}/32 Adivina el estado", "Cual es el nombre del estado?"
    ).title()
    if answer == "Exit":
        for state in state_names:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States to learn.csv")
        break
    if answer in state_names:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.estado == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer, font=("Arial", 9, "normal"))
