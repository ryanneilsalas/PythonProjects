import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
data_state = data.state.tolist()
data_x = data.x.tolist()
data_y = data.y.tolist()
label = turtle.Turtle()
label.color("black")
label.penup()
label.hideturtle()
no_of_state = len(data_state)
correct_state = 0
already_guess = []

while correct_state < no_of_state:
    answer_state = screen.textinput(f"Correct State {correct_state}/{no_of_state}", "Name a State").title()
    if answer_state in already_guess:
        print(f"You have already guess {answer_state}. Guess another State")
    else:
        if answer_state in data_state:
            st_data = data_state.index(answer_state)
            label.goto(x=data_x[st_data], y=data_y[st_data])
            label.write(answer_state, align="center", font=("Courier", 8, "bold"))
            correct_state += 1
            already_guess.append(answer_state)

        else:
            print("No Such State")

print("Congratulations you guessed all the states!")

screen.exitonclick()
