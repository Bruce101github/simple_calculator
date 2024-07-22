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
        signs = []
        for sign in equation:
            if (sign == "+" or
                sign == "-" or
                sign == "x" or
                sign == "/" or 
                sign == "%"):
                signs.append(sign)
        digits = []
        for sign in signs:
            x = equation.split(sign, 1)
            if ("+" in x[-1] or
                "-" in x[-1] or
                "x" in x[-1] or
                "/" in x[-1] or
                "%" in x[-1]):    
                equation = x[-1]
                y = x.pop(0)
                digits.append(y)
            else:
                while x:
                    for i in x:
                        digits.append(x.pop(0))
        print(calculator.solve_multi_step(digits,signs))
    elif equation == "off":
        break






