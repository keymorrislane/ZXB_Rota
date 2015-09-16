import numpy
import os
from PIL import Image
from PIL import ImageDraw


def edge_detection(filepath=""):
    if filepath == "":
        print("File path is empty.\n")
        return
    img_file = Image.open(filepath)
    l_img = Image.new('L', img_file.size)
    draw = ImageDraw.Draw(l_img)
    width = img_file.size[0]
    height = img_file.size[1]
    img_file = img_file.convert('L')
    for row in range(0, width):
        for col in range(0, height):
            brightness = img_file.getpixel((row, col))
            # print(brightness)
            draw.point([row, col], brightness)
    l_img.save(os.path.join(os.path.dirname(filepath), "temp.png"), "PNG")


def border_generate(img=None):
    if img == None:
        print("Binary image is missing.\n")
        return


if __name__ == '__main__':
    file_path = input('Input img:\n')
    edge_detection(file_path)
