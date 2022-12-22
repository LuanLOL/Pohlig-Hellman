import numpy

def crt(a, m):

    if numpy.any(len(a) != len(m)):
        return "a and m should be the same length!"

    r = len(a)

    prodM = numpy.prod(m)

    x = 0

    for j in range(0,r):
        x = x + a[j] * (prodM // m[j]) * invmodn(prodM // m[j], m[j])
        x = x % prodM

    return x

def powermod(a,z,n):
    a = a % n
    if (z < 0):
        z = -z
        a = invmodn(a, n)
    
    x = 1
    a1 = a
    z1 = z
    while (z1 != 0):
        while (z1 % 2 == 0):
            z1 = (z1 // 2)
            a1 = (a1 * a1) % n
        
        z1 = z1 - 1
        x = x * a1
        x = x % n
    return x

def invmodn(b, n):

    n0 = n
    b0 = b
    t0 = 0
    t = 1

    q = n0 // b0
    r = n0 - q * b0
    while r > 0:
        temp = t0 - q * t
        if (temp >= 0):
            temp = temp % n
        
        if (temp < 0):
            temp = n - (-temp % n)
        
        t0 = t
        t = temp
        n0 = b0
        b0 = r
        q = n0 // b0
        r = n0 - q * b0
    

    if b0 != 1:
        return "No inverse"
    else:
        return t % n
