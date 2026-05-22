def square_root(number):
    lower_bound = 0
    upper_bound = 1



    while lower_bound * lower_bound <= number :
        median = (lower_bound + upper_bound) // 2

        if median * median > number :
            upper_bound = median

        else :
            lower_bound = median

        print(median)
        return median
    

square_root(2356)