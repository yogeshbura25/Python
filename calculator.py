firstNumber = int(input())
secondNumber = int(input())
inputOperator = input()

if inputOperator == "+":
    print(firstNumber+(secondNumber))
elif inputOperator == "-":
    print(firstNumber-(secondNumber))
elif inputOperator == "*":
    print(firstNumber*(secondNumber))
elif inputOperator == "/":
    print(firstNumber/(secondNumber))
elif inputOperator == "**":
    print(firstNumber**(secondNumber))
else:
    print("Enter a valid Number or Operator")