n = int(input())
length = 0
while True:       #don't do this
    length += 1
    n //= 10
    if n == 0:
        break
print('Length is', length)

#It's cleaner and easier to read to rewrite this loop with a meaningful loop condition:

n = int(input())
length = 0
while n != 0:     #do this
    length += 1
    n //= 10
print('Length is', length)