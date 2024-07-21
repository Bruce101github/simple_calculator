from operation import Operation


class Equation(Operation):
    """Handles and checks all equations"""

    def __init__(self):
        "Initializing"
        super().__init__()

    def equation_type(self, equation):
        """Checks if an equation is one step or multi-step"""
        signs = 0
        for sign in equation:
            if (sign == self.addition or
                sign == self.subtraction or 
                sign == self.multiplication or 
                sign == self.division or
                sign == self.remainder):
                signs += 1
        if signs == 1:
            return "One-step"
        elif signs > 1:
            return "Multi-step"

    def seperate_equation(self, equation, sign):
        """This would seperate the two digits in an equation"""
        if sign == "addition":
            num = equation.split(self.addition)
            return num
        if sign == "subtraction":
            num = equation.split(self.subtraction)
            return num
        if sign == "multiplication":
            num = equation.split(self.multiplication)
            return num
        if sign == "division":
            num = equation.split(self.division)
            return num
        if sign == "remainder":
            num = equation.split(self.remainder)
            return num

    def solve(self, digits, sign):
        "solves one step equation"
        if sign == "addition":
            return (int(digits[0]) + int(digits[1]))
        if sign == "subtraction":
            return (int(digits[0]) - int(digits[1]))
        if sign == "multiplication":
            return (int(digits[0]) * int(digits[1]))
        if sign == "division":
            return round((int(digits[0]) / int(digits[1])), 3)
        if sign == "remainder":
            return (int(digits[0]) % int(digits[1]))

        





