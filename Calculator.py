# def my_function ():
#     return 3*2
# output = my_function ()

# def format_name (f_name, l_name):
#    """Take a first and last name and format it to return the title case verison 
#    of the  name. """
#    if f_name == "" or l_name == "" :
#        return "You did not provide valid inputs."
#    formatted_f_name = f_name.title()
#    formated_l_name= l_name.title()
#    return f"{formatted_f_name} {formated_l_name}"

# formated_string = format_name(input("First Name: "),input("Last Name: "))
# print(formated_string) 
#  Add

def add(n1, n2):
    return n1 + n2


#  Subtract
def minus(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": minus,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("First number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        if operation_symbol == "+" or operation_symbol == "-" or operation_symbol == "*" or operation_symbol == "/":
            num2 = float(input("What's the next number?: "))
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
            if input(
                    f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
                num1 = answer
            else:
                should_continue = False
                calculator()
        else:
            print("Please choose valid operation")
            should_continue = False


calculator()
