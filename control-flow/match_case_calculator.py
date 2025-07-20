num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
   case a if operation == "+":
      print(f"The result is {num1 + num2}.")
   case a if operation == "-":
      print(f"The result is {num1 - num2}.")
   case a if operation == "*":
      print(f"The result is {num1 * num2}.")
   case a if operation == "/":
      if num2 == 0 or num1 == 0:
         print("Cannot divide by zero.")
      else:
         print(f"The result is {num1 / num2}.")
   case _:
      print("Invalid selection")
   