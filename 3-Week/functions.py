# 1. Large Power
# Create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000. We will use a conditional statement to return True if the result is greater than 5000 or return False if it is not. In order to accomplish this, we will need the following steps:
# Define the function to accept two input parameters called base and exponent
# Calculate the result of base to the power of exponent
# Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False.


# Coding Question
# Create a function named large_power() that takes two parameters named base and exponent.
# If base raised to the exponent is greater than 5000, return True, otherwise return False

# 1. function(base,exponent)
# 2. if result of base**exponent >5000
# 3. if true print true else return false
def large_power(base,exponent):
    result= base ** exponent
    print(result)
    if result >5000:
        return True
    else:
        return False

base=int(input("Enter the Base Number: ")) 
exponent= int(input ("Enter the Exponent: "))  
print(f"The final Boolean Value is : ", large_power(base,exponent)) 
# print(large_power(20,5))    


# 2.Divisible By Ten
# Create a function that determines whether or not a number is divisible by ten. A number is divisible by ten if the remainder of the number divided by 10 is 0. Using this, we can complete this function in a few steps:
# Define the function header to accept one input num
# Calculate the remainder of the input divided by 10 (use modulus)
# Use an if statement to check if the remainder was 0. If the remainder was 0, return True, otherwise, return False.

#function (num)
#2.if num%10=0 return true else false
# Coding question

# Create a function called divisible_by_ten() that has one parameter named num.
# The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.

def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

print (divisible_by_ten(450))    
