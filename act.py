filename = "shop.txt"
try:
    with open(filename,"x") as file:
        print("File Created Successfully")
        file.write("Welcom to your inventory ")

except:
    print("File Already exist")

