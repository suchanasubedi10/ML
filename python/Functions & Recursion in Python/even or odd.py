# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
number = int(input("Enter a number: "))
result = check_even_odd(number)
print(f"The number  is {result}.")
# print("The number {} is {}.".format(number, result))
#print("The number %d is %s." % (number, result)) 
