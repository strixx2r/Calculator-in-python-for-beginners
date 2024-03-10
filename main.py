def mult(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Duch Null ist nicht erlaubt")
    else:
        return x / y

print("Wähle eine Operation:")
print("1. Addieren")
print("2. Subtrahieren")
print("3. Multiplizieren")
print("4. Teilen")

while True:
    choice = input("Gib deine Wahl (1/2/3/4) ein: ")

    if choice in ('1', '2', '3','4'):
        num1 = float(input("Gib die erste Zahl ein: "))
        num2 = float(input("Gib die zweite Zahl ein: "))

        if choice == 1:
            print(num1, "+", num2, "=", mult(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Ungültige Eingabe")


