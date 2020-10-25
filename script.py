from ppadb.client import Client
from PIL import Image
import numpy

adb = Client(host="127.0.0.1", port=5037)
devices = adb.devices()

if len(devices) == 0:
    print("No phone is connected to the computer...")
    quit()

device = devices[0]
width = int(str(device.shell("wm size").split(":")[1].split("x")[0]).strip()) / 2
device.shell(f"input touchscreen swipe {width} 100 {width} 1600 2000")

# image = device.screencap()

# with open("screen.png", "wb") as f:
#     f.write(image)

# image = Image.open("screen.png")
# image = numpy.array(image, dtype=numpy.uint8)
# pixels = [list(i[:3]) for i in image[1000]]

# white = True
# pos = []

# for i, pixel in enumerate(pixels):
#     r, g, b = [int(i) for i in pixel]

#     if white and (r+g+b) != 765:
#        white = not white
#        pos.append(i)
#        continue

#     if not white and (r+g+b) == 765:
#        white = not white
#        pos.append(i)
#        continue

# pos = [pos[1], pos[-1]]
# pos = pos[1] - pos[0] + 20
