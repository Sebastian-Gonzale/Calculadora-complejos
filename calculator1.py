def cplxsum(a,b):
    real = a[0] + b[0]
    imag = a[1] + b[1]
    return (real, imag)

def cplxrest(a,b):
    real = a[0] - b[0]
    imag = a[1] - b[1]
    return (real, imag)

def clpxmult(a,b):
    real = (a[0]*b[0])-(a[1]*b[1])
    imag = (a[0]*b[1])+(a[1]*b[0])
    return (real,imag)

def clpxmdiv(a,b):
    real = ((a[0]*b[0])+(a[1]*b[1]))/((b[0])**2+(b[1])**2)
    imag = ((a[1]*b[0])-(a[0]*b[1]))/((b[0])**2+(b[1])**2)
    return (real,imag)
    
def clpxmou(a):
    modulo= (((a[0])**2)+((a[1])**2))**0.5
    return (modulo)

def clpxconj(a):
    real=(a[0])
    imaginario=(-a[1])
    return (real,imaginario)
