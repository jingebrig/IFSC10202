def count_digits(num):
    count = 0
    temp = num
    while temp > 0:
        count += 1
        temp = temp // 10
    return count if count != 0 else 1

def special_num(num):
    num_digits = count_digits(num)
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp = temp // 10
    return total == num

start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))

print(f"Special numbers from {start} to {end}:")

for number in range(start, end + 1):
    if special_num(number):
        print(number)