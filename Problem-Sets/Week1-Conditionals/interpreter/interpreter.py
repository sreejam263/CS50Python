def main():
    #user prompt
    expression = input('Enter your arithmetic expression:').strip().lower()
    x, y, z = expression.split(" ")

    match y:
        case "+":
            result = int(x)+int(z)
        case "-":
            result = int(x)-int(z)
        case "*":
            result = int(x)*int(z)
        case "/":
            result = int(x)/int(z)
    print(f"{result:,.1f}")

main()



