def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Aduna")
print("2.Scade")
print("3.Inmulteste")
print("4.Imparteste")

while True:
    # take input from the user
    choice = input("Alege dintre(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Introdu primul numar: "))
            num2 = float(input("Introdu al doilea numar: "))
        except ValueError:
            print("IValoare invalida. Te rugam, alege alt numar.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        

        next_calculation = input("Doresti sa facem urmatorul calcul (da/nu): ")
        if next_calculation == "nu":
          break
    else:
        print("Valoare invalida.")
