class Complex(object):
    import cmath

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imag = self.imaginary + no.imaginary
        return Complex(real, imag)

    def __sub__(self, no):
        real = self.real - no.real
        imag = self.imaginary - no.imaginary
        return Complex(real, imag)

    def __mul__(self, no):
        real = (self.real * no.real) - (self.imaginary * no.imaginary)
        imag = (self.real * no.imaginary) + (self.imaginary * no.real)
        return Complex(real, imag)

    def __truediv__(self, no):
        real_numerator = (self.real*no.real + self.imaginary*no.imaginary)
        imag_numerator = (self.imaginary*no.real - self.real*no.imaginary)
        divisor = no.real**2 + no.imaginary**2
        return Complex(real_numerator/divisor, imag_numerator/divisor)

    def mod(self):
        c = complex(math.sqrt(self.real**2 + self.imaginary**2))
        return Complex(c.real, c.imag)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
