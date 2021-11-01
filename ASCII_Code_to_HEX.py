# Program to convert picture in any format to ASCII art
from PIL import Image
import numpy as np

# open picture and read out the information of all the pixels
im = Image.open("my-face-when-she-text-me-first.jpg", "r")
width, height = im.size
pixel_values = list(im.getdata())

list_2d_of_ASCII_chars = []
buffer_list_to_transfer_values = []
counter = 1
for pixel in pixel_values: 
    luminosity = 0.2126*pixel[0] + 0.7152*pixel[1] + 0.0722*pixel[2]
    if luminosity <= 20:
        buffer_list_to_transfer_values.append("###")
    elif 20 < luminosity <= 40:
        buffer_list_to_transfer_values.append("@@@")
    elif 40 < luminosity <= 60:
        buffer_list_to_transfer_values.append("GGG")
    elif 60 < luminosity <= 80:
        buffer_list_to_transfer_values.append("CCC")
    elif 80 < luminosity <= 100:
        buffer_list_to_transfer_values.append("LLL")
    elif 100 < luminosity <= 120:
        buffer_list_to_transfer_values.append("GGG")
    elif 120 < luminosity <= 140:
        buffer_list_to_transfer_values.append("fff")
    elif 140 < luminosity <= 160:
        buffer_list_to_transfer_values.append("ttt")
    elif 160 < luminosity <= 180:
        buffer_list_to_transfer_values.append(";;;")    
    elif 180 < luminosity <= 200:
        buffer_list_to_transfer_values.append(",,,")  
    elif 200 < luminosity <= 220:
        buffer_list_to_transfer_values.append(":::")
    elif 220 < luminosity <= 240:
        buffer_list_to_transfer_values.append("...")
    elif 240 < luminosity :
        buffer_list_to_transfer_values.append("   ")  

    if width == counter:
        list_2d_of_ASCII_chars.append(buffer_list_to_transfer_values)
        buffer_list_to_transfer_values = []
        counter = 0

    counter += 1

# write result to text file
text_art_file = open("Text_art", "w+")
for sublist in list_2d_of_ASCII_chars:
    text_art_file.write("\n")
    for element in sublist:
        text_art_file.write(element)

text_art_file.close()
