import PIL
from PIL import Image
import numpy as np

ASCII_CHARS = ['@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ']

def resize_image(image, new_width=100):
    width, height = image.size

    asp_ratio = height/width
    new_height = int(new_width*asp_ratio)

    resized_image = image.resize((new_width, new_height))

    return resized_image

def cvt_to_grayscale(image):
    grayscale_img = image.convert("L")

    return grayscale_img

def pixel_to_ascii(image):
    pixels = image.getdata()
    chars = "".join([ASCII_CHARS[pixel//50] for pixel in pixels])
    return chars

def cvt_ascii_to_img(arr: list, filename='image'):
    array = np.array(arr, np.uint8)
    data = Image.fromarray(array)
      
    # saving the final output 
    # as a PNG file
    data.save(filename+'.png')