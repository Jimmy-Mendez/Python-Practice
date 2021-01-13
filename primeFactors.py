
def isPrime(number):
    i = 2
    while i < number:
        if number%i == 0:
            return 0
        i+=1
    return 1

while(1):

    num = int (input("Enter a number: "))

    if (isPrime(num) == 1):
        print("prime!")
    else:
        print("not prime!")
