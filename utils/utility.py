def prompt_conversion_type_selection():
    choice = int(input("What kind of convertion do you wnat to use? ( 1: ascii-art, 2: braille)\n>>> "))
    while choice < 1 or choice > 2:
        print("Invalid answer, please, try again.")
        choice = int(input("What kind of convertion do you wnat to use? ( 1: ascii-art, 2: braille)\n>>> "))
    return choice

def grayscale_value_to_palette_index(grayscale, palette_length):
    '''Scale the pixel gray rgb value to fit into the palette and pick the correspondig color'''
    rgb_position = grayscale / 255
    palette_index = int((palette_length - 1) * rgb_position)
    return palette_index

def image_resize_prompt(original_size):
    '''Prompt the user to resize the image and calculate new size'''
    print("Current image size is: ", original_size)
    width, height = original_size
    do_resize = False
    if input("Do you want to scale down the image? [Y/N]") in ["Y","y"]:
        new_scale_factor = int(input("Downsizing factor: 1/"))
        width = int(width/new_scale_factor)
        height = int(height/new_scale_factor)
        do_resize = True
    return do_resize, width, height

def get_braille_character(chunk_Value):
    unicode_value = int(0x2800) + chunk_Value
    return chr(unicode_value)
