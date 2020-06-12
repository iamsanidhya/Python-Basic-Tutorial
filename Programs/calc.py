from math import*
n1 = float(input("Enter the number1: "))
n2 = float(input("Enter the number2: "))
op = input("Choose the opeartion: \n 1. Addition \n 2. Subtraction \n 3. Multiply \n 4. Division ")

if op == 1:
     sum = n1 + n2
     print()
elif op == "-":
     print(n1-n2)

elif op == "*":
     print(n1*n2)
elif op == "/":
      print(n1/n2)
else:
	 print("invalid opeartor")

