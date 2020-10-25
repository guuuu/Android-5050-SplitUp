from ppadb.client import Client
adb = Client(host="127.0.0.1", port=5037)
devices = adb.devices()

if len(devices) == 0:
    print("No phone is connected to the computer...")
    quit()

device = devices[0]
width = int(str(device.shell("wm size").split(":")[1].split("x")[0]).strip()) / 2
device.shell(f"input touchscreen swipe {width} 100 {width} 1600 2000")