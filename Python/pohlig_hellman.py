import helper_functions
import sympy

def pohlig_hellman(p, a, b):
    factorMap = sympy.factorint(p-1)
    qlist = list(factorMap.keys())
    counterlist = list(factorMap.values())
    masterx = []
    for index in range(len(qlist)):
        q = qlist[index]
        xlist = []
        prevb = helper_functions.powermod(b, (p-1)//q, p)
        currx = prevb
        for k in range(q):
            if helper_functions.powermod(a, k * ((p-1)//q), p) == currx:
                xlist.append(k)
                break
        prevb = b
        counter = 1
        while counter < counterlist[index]:
            prevb = (prevb * helper_functions.powermod(helper_functions.invmodn(helper_functions.powermod(a, xlist[-1], p), p), (q**(counter - 1)), p) % p)
            currx = helper_functions.powermod(prevb, (p - 1) // (q**(counter + 1)), p)
            for k in range(q):
                if helper_functions.powermod(a, k * ((p-1)//q), p) == currx:
                    xlist.append(k)
                    break
            counter = counter + 1
        overallx = 0
        for j in range(1, counterlist[index]+1):
            overallx = (overallx + (q**(j-1))*xlist[j-1]) % (q**counterlist[index])
        masterx.append(overallx)
    xforcrt = []
    for w in range(len(masterx)):
        xforcrt.append((masterx[w], (qlist[w]**counterlist[w])))
    firstlist = []
    secondlist = []
    for tup in xforcrt:
        firstlist.append(tup[0])
        secondlist.append(tup[1])
    x = helper_functions.crt(firstlist, secondlist)
    return x
 
