import turtle

'''
Check the commands in the file and evaluate based on the first character
of the command.
Splits the commands with reference to the whitespace character
'''


def evaluate(commands):
    splitcommands = commands.split(" ")
    i = 0
    while i < len(splitcommands):
        command = splitcommands[i]
        c = command[0]
        # executes if command is F i.e., Forward
        if c == 'F':
            d = command[1:]
            distance = int(d)
            print("forward(" + d + ")")
            turtle.forward(distance)
        # executes if command is B i.e., Backward
        elif c == 'B':
            d = command[1:]
            distance = int(d)
            print("backward(" + d + ")")
            turtle.back(distance)
        # executes if command is L i.e., Left
        elif c == 'L':
            d = command[1:]
            angle = int(d)
            print("left(" + d + ")")
            turtle.left(angle)
        # executes if command is R i.e., Right
        elif c == 'R':
            d = command[1:]
            angle = int(d)
            print("right(" + d + ")")
            turtle.right(angle)
        # executes if command is C i.e., Circle
        elif c == 'C':
            d = command[1:]
            radius = int(d)
            print("circle(" + d + ")")
            turtle.circle(radius)
        # executes if command is U i.e., penup
        elif c == 'U':
            print("up()")
            turtle.up()
        # executes if command is D i.e., pendown
        elif c == 'D':
            print("down()")
            turtle.down()
        # executes if command is P i.e., Polygon
        elif c == 'P':
            num_of_sides_str = command[1]
            length1 = splitcommands[i + 1]
            length = int(length1)
            print(length)
            no_of_sides = int(num_of_sides_str)
            angle = 360 / no_of_sides
            for _ in range(no_of_sides):
                turtle.forward(length)
                turtle.left(angle)
        # executes if command is I i.e., Iteration
        elif c == 'I':
            iteration_times = int(command[1])
            j = i
            # while loop runs till character @ is found
            while splitcommands[j] != "@":
                j = j + 1
            sequence_list = splitcommands[i + 1:j]
            print(sequence_list)
            new_string = ""
            '''
            for loop iterates till the
            number of iteration times will be reached
            '''
            for _ in range(iteration_times):
                for sub_sequence in sequence_list:
                    new_string += sub_sequence
                    new_string += " "
            print(new_string)

            evaluate(new_string.rstrip())
            i = j

        i = i + 1
    turtle.exitonclick()


# enter the input sequence

inputString = input("Enter Sequence:")
print("Evaluating....")

# function call
evaluate(inputString)
