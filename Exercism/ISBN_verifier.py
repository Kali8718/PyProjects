def is_valid(isbn):
    new_isbn = list(isbn)
    while "-" in new_isbn :
        new_isbn.remove("-")

    if len(new_isbn) != 10 :
        return False
    if new_isbn[-1].isdigit() == False and new_isbn[-1].upper() != "X" :
        return False
    
    i = 10
    sum = 0
    for digit in new_isbn[0:-1] :
        digit = int(digit)
        sum += digit * i
        i -= 1

    if new_isbn[-1].upper() == "X" :
        sum += 10 * i
    else :
        sum += int(new_isbn[-1]) * i

    if sum % 11 == 0 :
        return True
    return False

print(is_valid("3-598-21507-A"))