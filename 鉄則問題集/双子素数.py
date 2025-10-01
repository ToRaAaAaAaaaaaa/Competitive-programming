def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(limit):
    sosu_list = []
    i = 1
    while len(sosu_list) < limit:
        if is_prime(i) and is_prime(i + 2):
            sosu_list.append(i)
        i += 1
    return sosu_list

N = int(input("双子素数の数: "))
twin_list = find_twin_primes(N)
print(' '.join(map(str, twin_list)))