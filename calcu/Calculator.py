def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def lambda_handler(event, context):
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        print("Enter choice(1/2/3/4): ")
        choice = event['choice']

        if choice in ('1', '2', '3', '4'):
            print("Enter first number : ")
            num1 = int(event['f_num'])
            print("Enter second number : ")
            num2 = int(event['s_num'])

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            break
        else:
            print("Invalid Input")