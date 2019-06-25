# Program to get the lcm of two numbers

def lcm(x,y) : 
    
    #take the greater number
    if x>y:
        greater = x
    else:
        greater = y
    
    #if greater is divisible by any of the inputs , greater is the lcm
    #else increment greater by one until it is divisible by both the inputs
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater +=1
    
    return lcm

print(lcm(10,45))

    