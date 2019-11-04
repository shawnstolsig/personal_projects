# Shawn Stolsig 
# Discord Bot - WOWS Screenshots
# Date: 10/31/2019

# This bot will take a World of Warships win screen screen-cap and pull out all text on the screen ##
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Shawn\AppData\Local\Programs\Python\Python38\Lib\site-packages\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open('sample2.png')))

# import pytesseract
# from PIL import Image, ImageEnhance, ImageFilter

# im = Image.open("sample.jpg") # the second one 
# im = im.filter(ImageFilter.MedianFilter())
# enhancer = ImageEnhance.Contrast(im)
# im = enhancer.enhance(2)
# im = im.convert('1')
# im.save('temp2.jpg')
# text = pytesseract.image_to_string(Image.open('temp2.jpg'))
# print(text)