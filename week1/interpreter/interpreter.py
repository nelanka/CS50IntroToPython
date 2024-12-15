# https://cs50.harvard.edu/python/2022/psets/1/interpreter/

input = input("Expression: ").strip()
split = input.split(" ")
if (len(split) != 3):
    print("Invalid input!")
    exit(1)

x = float(split[0])
op = split[1]
y = float(split[2])

match op:
    case "+":
        print(x + y)
    case "-":
        print(x - y)
    case "*":
        print(x * y)
    case "/":
        if (y != 0):
            print(x / y)
        else:
            print("Invalid input!")
            exit(2)
    case _:
        print("Invalid input!")
        exit(2)
