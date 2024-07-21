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

