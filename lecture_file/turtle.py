'''this is a turtle program that takes in a command and moves the turtle in the direction of the command'''
x=1
y=1
orient = str(input("Enter the command(up,down,left,right): "))

while True:
    if orient == "up":
        y += 1
    elif orient == "down":
        y -= 1
    elif orient == "left":
        x -= 1
    elif orient == "right":
        x += 1
    else:
        print("Invalid command")
        orient = str(input("Enter the command(up,down,left,right): "))
        continue
    print("New turtlr position:[",x,",",y,"]")
    orient = str(input("Enter the command(up,down,left,right): "))

    
