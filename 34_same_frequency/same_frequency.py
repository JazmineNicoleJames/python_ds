def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    result = False
    new_num1 = [int(n) for n in str(num1)]  
    new_num1.sort()

    new_num2 = [int(n) for n in str(num2)]
    new_num2.sort()
    
    if new_num1 == new_num2:
        result = True
    return result    