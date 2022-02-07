This program takes an image as an input and outputs a text file which can either be:
	(1) an ASCII-art representation of the image, built on a palette the user can choose among the ones in the "palettes.txt" file
	(2) a more "stylized" representation built using braille characters

Usage:
The program can be executed both in interactive mode and from the command line
If called from the command line please provide at least ONE path to an image to convert. More can be provided and they will be converted in the same order as they are provided.
If executed interactively, the two conversion functions can be called and used independently. They both take the path to an image as their sole argument.

The pillow module must be installed on your computer in order to use the program