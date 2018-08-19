# Main Function
def tempConvert():
    # Get Input Temperature String
    inputTempStr = input("Enter your temperature: ")
    # Split The String Into A List By Word
    inputTempLs = inputTempStr.split(" ")
    if inputTempLs[0] == "exit":
        import sys
        sys.exit()
    else:
        #Set Each "Argument" As A Variable For Easier Later Access
        inputTemp = float(inputTempLs[0])
        fromScale = str(inputTempLs[1])
        toScale = str(inputTempLs[2])
        
        # If The Starting Scale Is Fahrenheit...
        if fromScale == "--F":  
            if toScale == "--toF":
                outputTemp = str(inputTemp) + "°F"
            elif toScale == "--toC":
                outputTemp = str(int(float((inputTemp - 32) * 5 / 9))) + "°C"
            elif toScale == "--toK":
                outputTemp = str(int(float((inputTemp - 32) * 5 / 9) + 273.15)) + " K"
        # If The Starting Scale Is Celsius...
        elif fromScale == "--C":
            if toScale == "--toC":
                outputTemp = str(inputTemp) + "°C"
            elif toScale == "--toF":
                outputTemp = str(int(float((inputTemp + 32) * 9 / 5))) + "°F"
            elif toScale == "--toK":
                outputTemp = str(int(float(inputTemp + 273.15))) + " K"
        # If The Starting Scale Is  Kelvin...
        elif fromScale == "--K":
            if toScale == "--toK":
                outputTemp = str(inputTemp) + " K"
            elif toScale == "--toF":
                outputTemp = str(int(float(((inputTemp - 273.15) * 9 / 5) + 32))) + "°F"
            elif toScale == "--toC":
                outputTemp = str(int(float(inputTemp - 273.15))) + "°C"
    
    print(outputTemp)

# Intro
print("Hi! Welcome to Temperature Converter!!!\nTo get started, there will be some basic things that you will need to know.")
# Step 1
print("1. Enter your numbers plain.\nExample: 84\n")
# Step 2
print("2. Use attributes to define which scale you want to convert from.\n")
print("Fahreinheit                    --F")
print("Celsius                        --C")
print("Kelvin                         --K")
print("Example: 84 --F\n")
# Step 3
print("3. Also use attributes to define which scale you want to convert to.\n")
print("Fahreinheit                    --toF")
print("Celsius                        --toC")
print("Kelvin                         --toK")
print("Example: 84 --F --toK\n")
# Step 4
print("4. Press Enter and let the magic begin!!! Have Fun!!\n")
print("5. Type 'exit' to exit")
while(True):
    tempConvert()