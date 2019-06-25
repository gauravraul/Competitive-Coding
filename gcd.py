# program to find GCD of two numbers

def gcd(x,y):
    
    # gcd will always be less than or equal to the smallest of the given inputs,
    # dividing numbers by each other and checking the remainder
    #the remainder is GCD if nos are not divisible by each other
    while(y):
        x,y = y,x%y
    return x

print(gcd(9,12))