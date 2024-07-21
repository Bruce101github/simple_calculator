class Operation:
    """Manages operation"""

    def __init__(self):
        "Initializing"
        self.addition = "+"
        self.subtraction = "-"
        self.multiplication = "x"
        self.division = "/"
        self.remainder = "%"

    def check_operation(self, equation):
        """check for the type of operation"""
        for sign in equation:
            if sign == self.addition:
                return "addition"
            elif sign == self.subtraction:
                return "subtraction"
            elif sign == self.multiplication:
                return "multiplication"
            elif sign == self.division:
                return "division"
            elif sign == self.remainder:
                return "remainder"

 

