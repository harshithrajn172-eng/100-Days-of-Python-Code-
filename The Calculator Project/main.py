from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operands={"+":add, "-":subtract, "*":multiply, "/":divide}

n1 = int(input("Enter the first number: "))
nex=True
while nex==True:
    operand=input("Enter the operation: ")
    n2 = int(input("Enter the second number: "))

    def calculator(n1, n2):
        if operand in operands:
            return operands[operand](n1, n2)
    print("")
    result=(calculator(n1, n2))
    print(result)
    nex=True
    while nex==True:

        cont=input("Do you want to calculate another number?(Y/N): ").upper()
        if cont == "Y":
            operand = input("Enter the operation: ")
            n2 = int(input("Enter the second number: "))
            n1 =result
            print(calculator(n1, n2))
        else:
            nex=False
            n1!=result
            print("\n"*20)




