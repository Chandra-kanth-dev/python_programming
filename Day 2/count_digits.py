def count_digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

print(count_digits(int(input("enter a number"))))