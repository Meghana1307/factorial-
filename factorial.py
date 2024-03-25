num: int
n: int
def factorial(n):
    return 1 if (n==1) else n * factorial(n - 1) 
if __name__== '__main__':
    while True:
        try:
            num = int(input("Enter a non-negative integer to calculate its factorial: "))
            if num <= 0:
                print("Factorial is not defined for negative numbers nor zero.")
            else:
                result = factorial(num)
                print(f"The factorial of {num} is {result}")
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
