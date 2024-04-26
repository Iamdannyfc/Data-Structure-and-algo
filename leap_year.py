def is_leap(year):
    leap = False

    
    
    #  # Write your logic here  
    # checking the constraints
    if (year < 1900) and (year > 10**5):
        raise Exception("Sorry, no years below 1900 and/or greater than 10^5 ")
        
    # initialising my conditions  
    div_by_4 = (year % 4 == 0)
    div_by_100 = (year % 100 == 0)
    div_by_400 = (year % 400 == 0 )  
    
    # checking the conditions 
    leap = True if ((div_by_4 and not div_by_100) or div_by_400) else False
        
    return leap

year = int(input())
print(is_leap(year))
