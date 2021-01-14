def isPrime(number):
    i = 2
    while i < number:
        if number%i == 0:
            return 0
        i+=1
    return 1

def primeFactors(number):
    ans = []
    if (isPrime(number) == 1 ):
        ans = [1,number]
        print(ans)
    i = number - 1
    while(i!=1):
        if (isPrime(i)):
            if(number%i == 0):
                ans.append(i)
        i-=1
    return ans


while(1):
    inp = int(input("enter a number: "))
    result = primeFactors(inp)
    print("the prime factors are: ")
    print(result)
