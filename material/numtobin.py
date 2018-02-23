def number32( binary ):
    #Inverting binary string
    binary = binary[::-1]
    #Decimal part
    dec = 1
    for i in range(1,24):
        dec += int(binary[23-i])*2**-i
    #Exponent part
    exp = 0
    for i in xrange(0,8):
        exp += int(binary[23+i])*2**i
    #Total number
    number = (-1)**int(binary[31])*2**(exp-127)*dec
    return number