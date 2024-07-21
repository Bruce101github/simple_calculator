from equation import Equation


active = True
calculator = Equation()
while active:
    equation = input(">>> ")
    type = calculator.equation_type(equation)
    if type == "One-step":
        sign = calculator.check_operation(equation)
        digits = calculator.seperate_equation(equation, sign)
        answer = calculator.solve(digits, sign)
        print(answer)
    elif type == "Multi-step":
        print("This app only supports one step equations for now")
    elif equation == "off":
        break






