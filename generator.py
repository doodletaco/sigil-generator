# sigil generator.
# input the phrase you are making the sigil for and it will give you a sigil


# receive the input
def get_input():
    print("Please type what you would like to turn into a sigil.")
    sigil = input(">>> ")
    return sigil


# process the input and remove spaces, vowels, punctuation, and repeating characters
def process_input():
    string_set = 'swkcgzpmqjfxldrnthvb'
    string = ''
    for c in get_input():
        if (c in string_set) and (c not in string):
            string += c
    return string


# assign each character in the processed input to coordinates
def coordinates():
    pass


# make a turtle draw the list of coordinates and display the image
def draw_sigil():
    pass

# main loop
def main():
    print(process_input())


if __name__ == '__main__':
    main()
