def isqrt (y: int) -> int :
    l = 0
    u = y + 1
    
    while (l < u - 1) :
        m = (l+u) // 2
        if (m*m <= y) :
            l = m
        else :
            u = m 
    
    return l

print(isqrt(24363246))