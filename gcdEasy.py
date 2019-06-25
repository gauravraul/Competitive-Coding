# Easy to understand code of GCD
#please check gcd.py before/after this program 

def gcdEasy(x,y):
    
    #take the smallest of the two inputs
    if x>y:
        small = y
    else:
        small = x
        
    #check if both the numbers are divisible by any between 1 to smallest
    # if divisible then it is gcd 
    for i in range (1, small + 1) :
        if((x%i == 0) and (y % i == 0)):
            gcd = i

    return gcd   

print(gcdEasy(9,12))