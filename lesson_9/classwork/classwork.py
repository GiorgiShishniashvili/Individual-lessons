start = int(input("enter your starting number: "))
end = int(input("enter your ending number: "))
sum = 0

for i in range(start, end+1):
    if i % 3 == 0:
        sum = sum + i
print(sum)