def is_armstrong_number(number):
    #Insert digits into list
    list_of_digits = [i for i in str(number)]
    #Variables for calculations
    sum_of_digits = 0
    exponent = (len(list_of_digits))
    #Validate we are working with positive integers
    if int(number) < 0:
        raise ValueError('Please use positive integers only')
    else:
        #Loop through list of digits and summing the values
        for i in list_of_digits:
            sum_of_digits = sum_of_digits + int(i)**exponent
    #Compare to determine if Armstrong number
    if number == sum_of_digits:
        result = True
    else:
        result = False
    return  result
            
            
            
    
