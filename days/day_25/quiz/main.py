import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

map = "blank_states_img.gif"

screen.addshape(map)

turtle.shape(map)

screen.tracer(0)

data = pandas.read_csv("50_states.csv")

states_list = data.state.to_list()

print(states_list)

score = 0

score_text = turtle.Turtle()

score_text.hideturtle()
score_text.penup()
score_text.goto(0, 250)


while score < 50:
    screen.update()
    score_text.clear()
    score_text.write(f"{str(score)}/50", font=('Courier', 24, 'normal'))
    answer_state = screen.textinput(title="Guess a state", prompt="Enter a state").title()

    if answer_state == "Exit":
        break

    if answer_state in states_list:
        index = states_list.index(answer_state)
        state_data = data[data.state == answer_state]
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(int(state_data.x), int(state_data.y))
        text.write(state_data.state.item(), align="center")
        score += 1
        states_list.remove(answer_state)

new_data = pandas.DataFrame(states_list)
new_data.to_csv("missing_states.csv")

turtle.mainloop()
