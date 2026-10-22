from PIL import Image, ImageFilter
import os
path = os.path.join(os.path.dirname(__file__),"costume1.jpeg")
def main():
    with Image.open(path) as img:
        print(img.size)
        print(img.format)
        img = img.rotate(180)
        img = img.filter(ImageFilter.BLUR)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save(os.path.dirname(__file__) + "/out.jpeg")
    

main()