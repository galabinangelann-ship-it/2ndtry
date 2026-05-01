filename = "shop.txt"
try:
    with open(filename,"x") as file:
            print("File Created Successfully")

except:
    print("File Already exist")

def add():
        with open(filename,"a") as file:
            additem = input("Enter item to add: ") 
            file.write(additem + "\n")
            
    