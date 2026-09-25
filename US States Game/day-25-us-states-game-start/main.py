import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S.States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.screensize()

data=pandas.read_csv("50_states.csv")
state_list=data.state.to_list()
guessed_state=[]
while len(guessed_state)<50:
    answer_state=screen.textinput(title=f"{len(guessed_state)}/50 states guessed",
                                  prompt="Whats the next state?").title()
    if answer_state == "Exit":
        missing_state=[state for state in state_list if state not in guessed_state]
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("missing_states.csv")
        break
    if answer_state in state_list:
        t=turtle.Turtle()
        t.color("black")
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        print(state_data)
        t.goto(state_data.x.iat[0], state_data.y.iat[0])
        t.write(answer_state)
        guessed_state.append(answer_state)

