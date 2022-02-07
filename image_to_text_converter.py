import sys
from PIL import Image
import utils.palette_manager as PM
from utils.utility import *

# Palette catalogue setup
palette_source_text_file = "palettes.txt"
palette_catalogue = PM.load_palettes(palette_source_text_file)

def default_ascii_art_conversion(image_path):
    '''Convert an image to its representation in text characters'''

    # Load the image from the given path
    img = Image.open(image_path, "r")
    print("Imported:", image_path)

    # Resize the image
    resize, w, h = image_resize_prompt(img.size)
    if resize:
        img = img.resize((w,h), Image.ANTIALIAS)
    print("Image succesfully resized.")

    # Select the text palette
    palette, palette_name = PM.select_palette(palette_catalogue)

    # Convert the pixels to grayscale
    pixels_rgb = list(img.getdata())
    pixels_gs = [int(sum(pixel[:3])/3) for pixel in pixels_rgb]
    print(" - Converting RGB values into ASCII characters...")
    final_string = ""

    # rgb to gs to text conversion
    for pixel_value in pixels_gs:
        index = grayscale_value_to_palette_index(pixel_value, len(palette))
        final_string += palette[index]
    print("Done. Now writing the output file.")

    # Dividing the generated text in lines
    output_text = [final_string[i:i+w] for i in range(0, len(final_string), w)]

    # Creating the file
    output_file_name = f"results/{image_path}_{palette_name}_{w}x{h}.txt"
    file = open(output_file_name, "w")
    for line in output_text:
        file.write(line)
        file.write("\n")
    file.close()
    print("Done. The file has been saved in the results folder.")

def braille_alphabet_conversion(image_path):
    '''Convert an image to its representation in ASCII characters'''

    # Load the image from the given path
    img = Image.open(image_path, "r")
    print("Imported:", image_path)

    # Resize the image
    resize, w, h = image_resize_prompt(img.size)

    # Make sure that w = 2*k and h = 4*j -> image must be divisible in 2x4 chunks
    if w % 2 != 0:
        w -= 1
    if h % 4 != 0:
        h -= (h%4)
    img = img.resize((w,h), Image.ANTIALIAS)
    print("Image succesfully resized.")

    # Select brightness treshold
    treshold = int(input("Brightness treshold (0-255): "))
    if treshold > 255:
        treshold = 255
    elif treshold < 0:
        treshold = 0

    # Image brightness logic array
    pixels = [( 1 if (int(sum(pixel[:3])/3) <= treshold) else 0) for pixel in list(img.getdata())]

    # Loop through the chunks and get characters
    horizontalChunks = int(w / 2)
    verticalChunks = int(h / 4)
    final_string = ""
    for y in range(verticalChunks):
        top = y * 4
        for x in range(horizontalChunks):
            left = x * 2
            # get pixel pos in 1D array and compute chunk byte value
            bit_1 = w * top + left
            bit_2 = bit_1 + w
            bit_3 = bit_2 + w
            bit_4 = bit_1 + 1
            bit_5 = bit_2 + 1
            bit_6 = bit_3 + 1
            bit_7 = bit_3 + w
            bit_8 = bit_7 + 1
            chunk_value = 1 * pixels[bit_1] + 2 * pixels[bit_2] + 4 * pixels[bit_3] + 8 * pixels[bit_4] + 16 * pixels[bit_5] + 32 * pixels[bit_6] + 64 * pixels[bit_7] + 128 * pixels[bit_8]
            final_string += get_braille_character(chunk_value)

    # Creating the file
    output_file_name = f"results/{image_path}_braille_{w}x{h}.txt"
    file = open(output_file_name, "w")
    last_character = 0
    for y in range(verticalChunks):
        for x in range(horizontalChunks):
            file.write(final_string[last_character])
            last_character += 1
        file.write("\n")
    file.close()
    print("Done. The file has been saved in the results folder.")

# MAIN
if __name__ == "__main__":

    # Argument exception handler
    if len(sys.argv) < 2:
        print("Error: arguments missing.")
        exit("Input at least the path to one image.")

    # Get image paths
    image_paths = sys.argv[1:]

    # Select conversion mode
    if prompt_conversion_type_selection() == 1:
        convert = default_ascii_art_conversion
    else:
        convert = braille_alphabet_conversion

    for image in image_paths:
        print(f"Now attempting to convert {image}...")
        convert(image)
