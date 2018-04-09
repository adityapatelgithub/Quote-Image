# decorate.py
# This file adds a colorful background image to the quote. It also makes font more interactive.

from from_brainyquote import get_quote_of_day, get_random_quote
from PIL import Image, ImageDraw, ImageFont
import os
from random import choice, shuffle, randint

if not os.path.isdir("final-image"):
    os.mkdir("final-image")

def select_random_image_location():
    """
    :return: location of a randomly selected image (for background)
    """
    folder = "images/"
    options = os.listdir(folder)
    return folder + choice(options)

def select_random_font_location():
    """
    :return: location of a randomly selected image (for background)
    """
    prefix = "fonts/"
    options = os.listdir(prefix)
    return prefix + choice(options)

def adjusted_font_size(quote):
    """
    Returns recommedned font size for given quote
    :param quote: quote (as string)
    :return: recommended size
    """
    size = 50
    size_text = len(quote)
    resize_heuristic = 0.9
    resize_actual = 0.985
    while size_text > 1:
        size_text = size_text * resize_heuristic
        size = size * resize_actual
    return int(size)

def organize_quote(quote, width = 30):
    """
    This function returns quote in a "split" form so that the quote fits in the background image
    :param quote: quote(as string)
    :param width: Width of the quote. Initialized to 30 characters
    :return: wrapped text
    """
    new_text = "-" #start new text with - so that first line of string is not empty; otherwise, there would be errors
    new_sentence = ""
    for word in quote.split(" "):
        delim = " " if new_sentence != "" else ""
        new_sentence = new_sentence + delim + word
        if len(new_sentence) > width:
            new_text += "\n" + new_sentence
            new_sentence = ""
    new_text += "\n" + new_sentence
    return new_text + "-"

def write_on_image(text, background_img, save_file_name, img_width, img_height, font, font_size, font_type, space):
    """
    This function writes quote on image and saves image in final-image directory
    :param text: quote
    :param background_img: image
    :param save_file_name: path of directory where image needs to be saved
    :param img_width: image width
    :param img_height: image height
    :param font: font type (in string)
    :param font_size: font size
    :param font_type: font type Object
    :param space: spacing between quotes
    :return:
    """
    # setup
    img = Image.new("RGBA", (img_width, img_height), (255, 255, 255))

    # background
    back = Image.open(background_img, 'r')
    img_w, img_h = back.size
    bg_w, bg_h = img.size
    offset = (int((bg_w - img_w) / 2), int((bg_h - img_h) / 2))
    img.paste(back, offset)

    # text
    font = ImageFont.truetype(font, font_size)
    draw = ImageDraw.Draw(img)
    img_w, img_h = img.size
    x = img_w / 2
    y = img_h / 2
    textsize = draw.multiline_textsize(text, font=font_type, spacing=space)
    text_w, text_h = textsize
    x -= text_w / 2
    y -= text_h / 2
    draw.multiline_text(align="center", xy=(x, y), text=text, fill=(255, 255, 255), font=font, spacing=space)
    draw = ImageDraw.Draw(img)
    img.save(save_file_name)
    return save_file_name


def create_image_with_quote():
    """Function that integrates all of the above function. This function is used in other modules to save image"""
    quote = organize_quote(get_random_quote()[0])   #get quote
    font = select_random_font_location()            #font-type
    font_type = ImageFont.truetype(font, adjusted_font_size(quote))   #font-type object
    file_name = str(randint(1, 100000))               #name of file
    save_file_name = "final-image/" + file_name + ".png"
    location = write_on_image(quote, select_random_image_location(), save_file_name, 500, 350, font, adjusted_font_size(quote), font_type, 3)
    return location

create_image_with_quote()
