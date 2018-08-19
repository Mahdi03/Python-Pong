def rgbColor(rgb):
    #Locally Global Vars
    r = g = b = a = 0
    #Prepping the RGB String
    rgb = rgb.strip('rgb')
    rgb = rgb.strip('(')
    rgb = rgb.strip(')')
    rgb = rgb.split(', ')
    #(Getting Each R G B and A Value)
    #Also Removing Unnecessary .0 (Floating Decimals) For Simplicity
    if int(rgb[0]) % 255 == 0:
        r = round(int(rgb[0]) / 255, None)
    else:
        r = round(int(rgb[0]) / 255, 1)
    if int(rgb[1]) % 255 == 0:
        g = round(int(rgb[1]) / 255, None)
    else:
        g = round(int(rgb[1]) / 255, 1)
    if int(rgb[2]) % 255 == 0:
        b = round(int(rgb[2]) / 255, None)
    else:
        b = round(int(rgb[2]) / 255, 1)
    #If Alpha Is Included, Acknowledge it
    if len(rgb) == 4:
        a = round(float(rgb[3]), 1)
        RGB = RGB = "rgb(" + str(r) + ", " + str(g) + ", " + str(b) + ", " + str(a) + ")"
    #If not, stick to normal procedure
    else:
        RGB = "rgb(" + str(r) + ", " + str(g) + ", " + str(b) + ")"
    return RGB
print("\nRGB(255, 255, 255) [White] in Python is:\n" + rgbColor("rgb(255, 255, 255)") + "\n")
print("RGB(128, 128, 128) [Gray] in Python is:\n" + rgbColor("rgb(128, 128, 128)") + "\n")
print("RGB(255, 255, 255, 0.5) [Half-Transparent] in Python is:\n" + rgbColor("rgb(255, 255, 255, 0.5)") + "\n")
print("RGB(0, 0, 0, 0.5) [Gray] in Python is:\n" + rgbColor("rgb(0, 0, 0, 0.5)") + "\n")
print("\n\n\nTry It Yourself:")
print("To exit this endless loop, simply input something other than an RGB Code. An error will be thrown and then you will be saved!!\n")
while(True):
    inputRGB = input("Write a RBG color code such as rgb(10, 20, 40) and press Enter: ")
    print(rgbColor(inputRGB))
    del inputRGB
