# Name: Shruti Subramanyam
# USC NetID: 3541420114
import math


# Assignment 1
# Please refer to assignment description for more details.

# The following function definitions are provided to you.
# Replace the placeholder code with your own and run the grading script
# to make sure your code runs as expected.

# Include your imports here.

def degrees_to_radians(degree: float) -> float:
    # calculate radians from degrees by multiplying degrees  by π and dividing by 180
    radians = (degree * math.pi) / 180
    return radians
    pass


def vowel_count(s: str) -> int:
    # make sure the code works for uppercase and lowercase strings
    s=s.upper()
    count=0
    for i in range (len(s)):
        if s[i] == 'A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
            count=count+1
    return count
    pass


def triangle_hypotenuse(base: float, height: float) -> float:
    # find hypotenuse of the triangle
    hypotenuse = (((base*base)+(height*height))**(1/2))
    return hypotenuse
    pass
