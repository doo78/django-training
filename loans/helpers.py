def is_prime(number):
    if number == 1 or number == 0:
        return False
    if number == 2:
        return True
    if number < 0:
        raise ValueError
    
    for x in range (2, number):
        if number%x == 0:
            return False
        
    return True
        