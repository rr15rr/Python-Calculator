#Python Calculator 

print("Welcome to my calculator, choose an option: ")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division\n")
option = int(input("My option is: "))

if option == 1:
    add = float(input("\nPick the first number for addition: "))
    add1 = float(input("Pick the second number for addition: "))
    addResult = str(add + add1)
    print("The result is: " + addResult + "\n")

if option == 2: 
    sub = float(input("\nPick the first number for substracting: "))
    sub2 = float(input("Pick the second number for substracting: "))
    subResult = str(sub - sub2)
    print("The result is: " + subResult + "\n")

if option == 3:
    mult = float(input("\nPick the first number for multiplication: "))
    mult2 = float(input("Pick the second number for multiplication: "))
    multResult = str(mult * mult2)
    print("The result is: " + multResult + "\n")

if option == 4: 
    div = float(input("\nPick the first number for dividing: "))
    div1 = float(input("Pick the second number for dividing: "))
    divResult = str(div/div1)
    print("The result is: " + divResult + "\n")