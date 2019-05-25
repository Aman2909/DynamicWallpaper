import ctypes
import time

from PIL import Image, ImageDraw, ImageFont

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

fnt200 = ImageFont.truetype('GreycliffCF-DemiBold.ttf', size=200)
fnt100 = ImageFont.truetype('GreycliffCF-Regular.ttf', size=100)

x: int = 80
while x != 0:
    time.sleep(1)
    img = Image.new(mode='RGB', size=screensize, color=(0, 0, 0))
    drawObject = ImageDraw.Draw(img)
    drawObject.text(xy=(550, 200), text="You have", fill=(255, 255, 255), font=fnt100)
    drawObject.text(xy=(300, 270), text=str(x) + " seconds", fill=(255, 255, 255), font=fnt200)
    drawObject.text(xy=(400, 500), text="remaining today", fill=(255, 255, 255), font=fnt100)
    x -= 1
    img.save('Test.bmp')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, 'D:\Coding\DynamicWallpaper\Test.bmp', 0)