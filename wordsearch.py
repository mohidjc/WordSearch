
"""

@author:Mohid Javed Chaudhry

"""



def wordsearch(puzzle: list, wordlist: list) -> None:
    if valid_puzzle(puzzle) == False:  # Function checks if puzzle is valid
        return print("ValueError, invalid puzzle")
    # Function checks if the wordlist is valid
    elif valid_wordlist(wordlist) == False:
        return print("ValueError, invalid puzzle")
    else:
        final_list = []  # Will hold coordinates of all the words
        for word in wordlist:
            word = word.upper()  # Makes the word uppercase
            # For each word, function returns all possible coordinates in the grid
            temp = get_positions(puzzle, word)
            if temp is not None:
                # A string of coordinate tuple is appended inside the main string
                final_list.append(temp)
        # Function displays grid with words found as coloured
        coloured_display(puzzle, final_list)


def valid_puzzle(puzzle: list) -> bool:
    len_0 = len(puzzle[0])
    for i in range(0, len(puzzle)):  # Checking for each word in the list

        if isinstance(puzzle[i], str):  # Every element of the list needs to be an element
            # Every string element of the list has to be of the same size
            if len(puzzle[i]) != len_0:
                print("not the right length!")
                return False
            else:
                if i == len(puzzle):
                    return True
        else:
            print("not a string")
            return False


def valid_wordlist(wordlist: list) -> bool:
    for i in range(0, len(wordlist)):
        if isinstance(wordlist[i], str):  # Checking if each word in the list a string
            if i == len(wordlist):
                return True
        else:
            return False


def get_positions(puzzle: list, word: str) -> list:
    all_locations_grid = []  # Coordinates of words in all locations

    for y in range(0, len(puzzle)):
        for x in range(0, len(puzzle[y])):
            if word[0] == puzzle[y][x]:

                if len(word) <= (x+1) and (y+1):  # diagonal left up
                    e = x  # To keep the value of x the same, assign value of x to variable e
                    r = y  # To keep the value of y the same, assign value of y to variable r
                    puzzle_word = []  # List that will hold all the letters in the range
                    list_of_tupleCoord = []  # List which holds all the coordinates as tuple
                    # Checks if there is enough space for the word to fit on the left and up
                    for z in range(e, (e)-len(word), -1):
                        # Appends the letter for comparing later on
                        puzzle_word.append(puzzle[r][z])
                        # Coorddinates into tuple and appended to a list
                        list_of_tupleCoord.append(tuple((r, z)))
                        r -= 1  # Allows to go up in grid each time index goes left
                    # Function comopares the word with the appended letters
                    if compare_letter(word, puzzle_word,):
                        # List is appended in another list
                        all_locations_grid.append(list_of_tupleCoord)

                if len(word) <= len(puzzle[0])-x and (y+1):  # diagonal right up
                    e = x
                    r = y
                    puzzle_word = []
                    list_of_tupleCoord = []
                    # Checks if enough space on the right and up for the word to fit diagonally
                    for z in range(e, e+len(word)):
                        puzzle_word.append(puzzle[r][z])
                        list_of_tupleCoord.append(tuple((r, z)))
                        r -= 1  # moves the index up by one
                    if compare_letter(word, puzzle_word,):
                        all_locations_grid.append(list_of_tupleCoord)

                # Diagnoal right down
                if len(word) <= len(puzzle[0])-x and len(puzzle)-y:
                    e = x
                    r = y
                    puzzle_word = []
                    list_of_tupleCoord = []
                    # Checks if enough space on the right and below for the word to fit diagnoally
                    for z in range(e, e + len(word)):
                        if r == len(puzzle):
                            r -= 1  # Because r goes to 11 it is out of range
                        puzzle_word.append(puzzle[r][z])
                        list_of_tupleCoord.append(tuple((r, z)))
                        r += 1  # Each iteration makes the vertical coordinate to go down by one
                    if compare_letter(word, puzzle_word,):
                        all_locations_grid.append(list_of_tupleCoord)

                if len(word) <= (x+1) and len(puzzle)-y:  # Diagonal left down
                    e = x
                    r = y
                    puzzle_word = []
                    list_of_tupleCoord = []
                    # If there is enough space on the left and down for the word to fit diagnoally
                    for z in range(e, (e)-len(word), -1):
                        if r == len(puzzle):
                            r -= 1
                        puzzle_word.append(puzzle[r][z])
                        list_of_tupleCoord.append(tuple((r, z)))
                        r += 1  # Horizontal coordinate goes down by one
                    if compare_letter(word, puzzle_word,):
                        all_locations_grid.append(list_of_tupleCoord)

                if len(word) <= (len(puzzle[0]) - x):  # Right side
                    e = x
                    r = y
                    puzzle_word = []
                    list_of_tupleCoord = []
                    # If enough space on right for the word to fit
                    for z in range(e, e + len(word)):
                        puzzle_word.append(puzzle[r][z])
                        list_of_tupleCoord.append(tuple((r, z)))
                    if compare_letter(word, puzzle_word,):
                        all_locations_grid.append(list_of_tupleCoord)

                if len(word) <= (x+1):  # check left
                    e = x
                    r = y
                    puzzle_word = []
                    list_of_tupleCoord = []
                    # If enough space on the left for the word to fit
                    for z in range(e, (e)-len(word), -1):
                        puzzle_word.append(puzzle[r][z])
                        list_of_tupleCoord.append(tuple((r, z)))
                    if compare_letter(word, puzzle_word,):
                        all_locations_grid.append(list_of_tupleCoord)

                if len(word) <= (y+1):  # check up
                    e = x
                    r = y
                    puzzle_word = []
                    list_of_tupleCoord = []
                    # If enough space above the first letter for the word to fit
                    for z in range(r, (r)-len(word), -1):
                        puzzle_word.append(puzzle[z][e])
                        list_of_tupleCoord.append(tuple((z, e)))
                    if compare_letter(word, puzzle_word,):
                        all_locations_grid.append(list_of_tupleCoord)

                if len(word) <= len(puzzle)-y:  # check down
                    e = x
                    r = y
                    puzzle_word = []
                    list_of_tupleCoord = []
                    # If enough space below the first character for the word to fit
                    for z in range(r, r+len(word)):
                        puzzle_word.append(puzzle[z][e])
                        list_of_tupleCoord.append(tuple((z, e)))
                    if compare_letter(word, puzzle_word,):
                        all_locations_grid.append(list_of_tupleCoord)
    if len(all_locations_grid) != 0:
        return all_locations_grid


def compare_letter(word: str, puzzle_word: list, ) -> bool:

    # Goes through each letter of word and word in the list and compares each letter
    for l in range(0, len(word)):
        if word[l] != puzzle_word[l]:
            return False
    return True


def basic_display(grid: list) -> None:
    new2dlst = []  # Outer list in the 2d list
    for x in range(0, len(grid)):  # Outer loop that iterates through each element in the grid list
        # Append a list inside a list for each iteration for element
        new2dlst.append([])

        # Inner loop that iterates through each character of string
        for i in range(0, len(grid[x])):
            # Appends each letter in the 2d list for each string index
            new2dlst[x].append(" "+grid[x][i]+" ")
            # Printing each letter for each strign spaced out
            print(" "+grid[x][i]+" ", end="")
        print(sep="")  # Separating the lines


def coloured_display(grid: list, positions: list) -> None:
    for j in range(0, len(grid)):  # Outer loop that iterates through each element in the grid list
        # Inner loop that iterates through each character of string
        for i in range(0, len(grid[j])):
            lst_coord = ["ajkh"]  # Keep the list populated
            for a in range(0, len(positions)):
                for b in range(0, len(positions[a])):
                    for c in range(0, len(positions[a][b])):
                        # the letter at every coordinate made a tuple to compare to coordinate tuples of the words found
                        t = tuple((j, i))
                        if t == positions[a][b][c]:
                            # Set pre-populated list with the current letter
                            lst_coord[0] = grid[j][i]

            # if the letter in list the same as the current letter in the list, print green background
            if lst_coord[0] == grid[j][i]:
                print("\033[42m" + " "+grid[j][i]+" " + "\033[0m", end='')

            else:
                print(" "+grid[j][i]+" ", end="")  # Else we print normal
        print(sep="")
    #print (positions)



def test_valid_wordlist():
    """
    Test function valid_wordlist()
    """
    good_wordlist = ["scalar", "tray", "blew", "sevruc", "testing"]
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    bad_wordlist2 = ["scalar", "tray", "blew", "sevruc", 59]

    print("wordlist is", valid_wordlist(good_wordlist))
    print("wordlist is", valid_wordlist(good_wordlist2))
    print("wordlist is", valid_wordlist(bad_wordlist2))


def test_valid_puzzle():
    good_puzzle = ['RUNAROUNDD1', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle1 = ['RUNAROUNDDL', 'EDCITOAHC', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle2 = ['RUNAROUNDDL', ['EDCITOAHCYV'], ('ZYUWSWEDZYA'),
                   'AKOTCONVOYV', 'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL',
                   'ISTREWZLCGY', 'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    print("puzzle is", valid_puzzle(good_puzzle))
    print("puzzle is", valid_puzzle(bad_puzzle1))
    print("puzzle is", valid_puzzle(bad_puzzle2))


def test_basic_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    basic_display(puzzle1)
    basic_display([['a', 'b', 'c', 'd', 'e'], ['h', 'l', 'j', 'k', 'l']])


def test_get_positions():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    get_positions(puzzle1, "TESTING")
    print(get_positions(puzzle1, "TRAY"))


def test_coloured_display():
   # puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
    #    'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
    # 'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    #good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]

    puzzle1 = ["BXHPBLACK", "BGOIEFWFI", "NYQNPDHAQ",
               "QGTKGREEN", "WHITEBLUE", "ORANGEGUY",
               "UBLYELLOW", "KXMGZPDRR", "BROWNTRED"]
    good_wordlist2 = ["yellow"]

    final_list = []
    for word in good_wordlist2:
        word = word.upper()
        temp = get_positions(puzzle1, word)
        if temp is not None:
            final_list.append(temp)
    #coloured_display (puzzle1, final_list)
    coloured_display(puzzle1, good_wordlist2)


def test_wordsearch():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    wordsearch(puzzle1, good_wordlist2)


if __name__ == "__main__":
    # uncomment the test function individually
    # basic solution
p    test_valid_puzzle()
# test_valid_wordlist()
# test_basic_display()

# full solution
# test_coloured_display()
# test_get_positions()
# test_wordsearch()
