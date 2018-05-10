#!/usr/bin/python
import sys

#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    #print(float(a))
    try: 
        a = float(a)
        b = float(b) 
        c = float(c) 
        x1, x2 = find_roots(a, b, c)
        print ("This is x1: %f" %x1)
        print ("This is x2: %f" %x2)
    except: 
        print("Please enter a numeric value (int or float).")
        

def find_roots(a,b,c):
    assert int(a) != 0, "Please enter a non-zero leading order coefficient" 
    mid = b**2 - 4*a*c
    assert mid > 0, "Provided values lead to imaginary roots. Panic!!!" 
    sqrt_mid = mid**(0.5)
    x1 = (-b + sqrt_mid)/(2*a)
    #assert x1 == (-b + sqrt_mid)/2*a, "Order of operations error! Panic!" 
    #assert b^2 == b**2, "Something going wrong with exponentiation..."
    #assert float(1/2) == 0.5, "Error with integer division... Stupid Python 3 :(" 
    #assert (1/2) == 0, "Python 3 is not behaving correctly"
    """
    Assert statement above reveals that there is a missing parens around 2*a in 
    each of the expressions for x1, x2. Placing these parens should make the output
    match the correct answer.
    Nevermind, that did not fix the problem :( 
    Asserting b^2 == b**2 identified the problem--the ^ operator is a bitwise XOR operator 
    according to the documentation, not exponentiation! 
    So changing b^2 --> b**2, mid^(1/2) --> mid**(1/2) should fix the problem 
    Next error: 1/2 is evaluating to 0, I believe --> change to 0.5? 
    Yes, this fixed the problem! 
    Also, in the function above, the values need to be converted into floats before being used in calculation
    """   
    x2 = (-b - sqrt_mid)/(2*a)
    return x1, x2


if __name__=="__main__":
        main()
