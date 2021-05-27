# programm for changing file format of images
# made by In2Darkenz
from PIL import Image
import os
import shutil
def wahlFormat():
    temp = str()
    print("\nPlease enter the input format: ")
    temp = input()
    inFormat = temp
    print("Input format: " + temp)
    print("\nPlease enter the output format: ")
    temp = input()
    outFormat = temp
    print("Output format: " + temp)
    return (inFormat, outFormat)
inFormat, outFormat = wahlFormat()
print(inFormat + " to " + outFormat)
path = os.getcwd()
print("Current dir: %s" % path)
os.mkdir(path + "/old")
os.mkdir(path + "/new")
# moving all
for file in os.listdir(path):
    if file.endswith("." + inFormat):
        im = Image.open(file)
        print("\nconvertet " + file + " to ")
        file = file.removesuffix("." + inFormat)
        newName = file + "." + outFormat
        im.save(newName)
        print(newName)
for file in os.listdir(path):
    if file.endswith("." + inFormat):
        shutil.move(path + "/" + file, path + "/old")
        print("\n" + file + " moved to " + path + "/old")
for file in os.listdir(path):
    if file.endswith("." + outFormat):
        shutil.move(path + "/" + file, path + "/new")
        print("\n" + file + " moved to " + path + "/new")
print("---------------------------Process completed!---------------------------")








