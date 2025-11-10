class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        # result = 0
        # if b <= 0:

        # for i in range(b):
        #     if a <= 0 or b <= 0:
        #         result = self.add(result, a)
        #         return -result
        #     else :
        #         result = self.add(result, a)
        #         return result

        # return result
        result = 0

        zz = False
        if (b < 0) or (a < 0):
            zz = True
            a, b = abs(b), abs(a)

        for i in range(b):
            result = self.add(result, a)

        if zz:
            result = -result
        return result

    def divide(self, a, b):
        # result = 0
        # zz = False
        # if (b < 0) or (a < 0):
        #     zz = True
        #     a, b = abs(b), abs(a)
        # while a >= b:
        #     result = self.subtract(a, b)
        #     result += 1
        #     if zz:
        #         result = -result
        # return result
        result = 0

        zz = False;
        if(b < 0) or (a<0):
            b = abs(b)
            a = abs(a)
            zz = True

        while a >= b:
            a = self.subtract(a, b)
            result += 1
        if(zz):
            result = -result
        return result

    def modulo(self, a, b):
        x = False;
        if(b < 0) or (a<0):
            b = abs(b)
            a = abs(a)
            x= True

        while a >= b:
            a = a-b
        if(x):
            a = -a
        return a


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
