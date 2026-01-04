def is_prime(n):
    if n < 2:
        return "Not Prime"
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return "Not Prime"
    return "Prime"

n = int(input("Enter a number : "))
print(f'{n} is {is_prime(n)}')