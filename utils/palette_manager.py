def load_palettes(source):
    '''Import palettes from the text file'''
    source_file = open(source)
    palettes = {}
    for line in source_file:
        # Skips comments and lines that are not long enough in the source file
        if line[0] == "#" or len(line)<3:
            continue
        # Import palettes
        palette_name = line.split("=")[0]
        palette_characters = line[len(palette_name)+1:].replace("\n", "").replace("◊", "")
        palettes[palette_name.strip()] = palette_characters
    # Return palette catalogue
    return palettes

def select_palette(catalogue):
    '''Select a palette from a give catalogue'''
    print("Type in the name of the palette you would like to use:")
    for key in catalogue:
        print("-", key)
    choice = input("Your choice: ")
    while choice not in catalogue:
        print("Sorry, that palette is not available. Try again:")
        choice = input("Your choice: ")
    return catalogue[choice], choice
