def classify(number):
    if number <= 0 :
        raise ValueError("Classification is only possible for positive integers.")

    factors = []
    for i in range(1, int(number**0.5)+1) :
        if number % i == 0 :
            factors.append(i)
    
    print(factors)
    
    if sum(factors) == number :
        return "perfect"
    elif sum(factors) > number :
        return "abundant"
    else :
        return "deficient"
    
    
print(classify(33550335))
