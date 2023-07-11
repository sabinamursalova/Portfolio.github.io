def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b 
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a, b):
    answer = a * b 
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b 
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

def main():
    while True:
        print("A. Addition")
        print("B. Subtraction")
        print("C. Multiplication")
        print("D. Division")
        print("E. Exit")

        choice = input("Input the choice: ")

        if choice.lower() == "a":
            print("Addition")
            a = int(input("Input first number: "))
            b = int(input("Input second nummber: "))
            add(a, b)
        elif choice.lower() == "b":
            print("Subtraction")
            a = int(input("Input first number: "))
            b = int(input("Input second number: "))
            sub(a, b)
        elif choice.lower() == "c":
            print("Multiplication")
            a = int(input("Input first number: "))
            b = int(input("Input second number: "))
            mul(a, b)
        elif choice.lower() == "d":
            print("Division")
            a = int(input("Input first number: "))
            b = int(input("Input second number: "))
            div(a, b)
        elif choice.lower() == "e":
            print("Program ended")
            break
        else:
            print("Invalid choice. PLease try again.")

if __name__ == "__main__":
    main()

