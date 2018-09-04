n = int(input("Enter the length of the sequence: ")) # Do not change this line
# 1, 2, 3, 6, 11, 20, 37
# n1 + n1 = n2 =>
# n1 + n2 = n3 =>
# n3 + n2 + n1 = n4 =>
# n4 + n3 + n2 = n5 ...
sum = 0
tala1 = 1
tala2 = 2
tala3 = 3

for i in range(1, n+1): 
    if i == 1:
        print(i)
        continue
    elif i == 2:
        print(i)
        continue
    elif i == 3:
        print(i)
        continue
    sum = (tala1 + tala2 + tala3)
    tala1 = tala2
    tala2 = tala3
    tala3 = sum
    print(sum)




