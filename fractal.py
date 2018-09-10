from PIL import Image
from colorsys import *
import time

_iteration = abs(eval(input("iteration")))
_zoom = abs(eval(input("zoom")))
Resolution = abs(eval(input("image size")))
_moveX = eval(input("position x"))
_moveY = eval(input("position y"))

HalfResolution = Resolution/2
imageResult = Image.new('RGB', (Resolution, Resolution), 'black')
pixels = imageResult.load()

class Complex:
    def __init__(self, real, img):
        self.r = real
        self.i = img

def Map(value, start1, stop1, start2, stop2):
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))

StartTime = time.time()
prevPercentage = -1
for x in range(Resolution):
    percentage = round(x/Height * 100)
    if percentage % 10 == 0 and prevPercentage != percentage:
        prevPercentage = percentage
        print(round(x/Height * 100), "%")
        
    for y in range(Resolution):
        c_f = Complex(Map((x - HalfResolution) / _zoom + _moveX, 0, Resolution, -2.5, 2.5), Map((y - HalfResolution) / _zoom + _moveY, 0, Resolution, -2.5, 2.5))
        c_s = Complex(0, 0)
        iterationDone = 0

        for z in range(_iteration):
            iterationDone +=1
            temp = pow(c_s.r, 2) - pow(c_s.i, 2) + c_f.r
            c_s = Complex(temp, 2.0 * c_s.r * c_s.i + c_f.i)

            if pow(c_s.r, 2) + pow(c_s.i, 2) > 4:
                break

        pcolor = [0,0,0]
        if iterationDone != _iteration:
            pcolor = [iterationDone-round(iterationDone/360)*iterationDone, 360, round(Map(iterationDone*6, 1, _iteration, 0, 360))]
            
        
        pcolor = hsv_to_rgb(pcolor[0]/360, pcolor[1]/360, pcolor[2]/360)
        pcolor = [round(pcolor[0] * 255), round(pcolor[1] * 255), round(pcolor[2] * 255)]

        pixels[x, y] = (pcolor[0], pcolor[1], pcolor[2])

FinalTime = time.time() - StartTime
imageResult.save('img_fractal_' + str(FinalTime) + '.png')
imageResult.show()
print("Fractale done in " + str(FinalTime) + ' ms')
