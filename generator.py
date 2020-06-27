import turtle as t
# sigil generator.
# input the phrase you are making the sigil for and it will give you a sigil

# initialize variables
STRING_SET = 'swkcgzpmqjfxldrnthvb'
COORDINATES = [(-150, 200), (-50, 200), (50, 200), (150, 200),
               (-150, 100), (-50, 100), (50, 100), (150, 100),
               (-150, 00), (-50, 00), (50, 00), (150, 00),
               (-150, -100), (-50, -100), (50, -100), (150, -100),
               (-150, -200), (-50, -200), (50, -200), (150, -200)]
win = t.Screen()
sheldon = t.Turtle()
sheldon.penup()


# make a turtle draw the list of coordinates and display the image
def draw_sigil():
    string = ''
    coords = []

    # collect input
    print("Please type what you would like to turn into a sigil.")
    sigil = input('>>> ')
    sigil.lower()

    # process the input
    for c in sigil:
        if (c in STRING_SET) and (c not in string):
            string += c

    # switch the characters to designated coordinates
    for c in string:
        coords.append(COORDINATES[STRING_SET.find(c)])

    # start drawing
    sheldon.goto(coords[0])
    sheldon.pendown()
    for i in range(1, len(coords)):
        sheldon.goto(coords[i])
    t.done()

# main loop
def main():
    draw_sigil()


if __name__ == '__main__':
    main()
