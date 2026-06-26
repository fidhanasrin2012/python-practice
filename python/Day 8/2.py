#print prime numbers from 1 to n

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
        
    return True
n = int(input("Enter the limit:"))

for i in range( 2, n +1 ):
    if is_prime(i):
        print(i)