numbers = [11,22,34,54,23]
even = list(filter(lambda x:x % 2 == 0 and x>30,numbers))
print("Even numbers greater than 30:",even)