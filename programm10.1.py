nums = [int(x) for x in input().split()]
data, data2 = [], []
cheker = False
def romb_cheker(num, i, j):
    for k in range(1, num):
        if data[i + k][j - k] == '1' and data[i + k][j + k] == '1':
            print("True")
            break

for i in range(nums[0]):
    data.append(input())
for i in range(nums[0]):
    if cheker:
        cheker = False
        break
    for j in range(nums[1]):
        if data[i][j] == '1':
            data2.append([i,j])
            cheker = True

for i in range(-1, -nums[0], -1):
    if cheker:
        cheker = False
        break
    for j in range(-1, -nums[1], -1):
        if data[i][j] == '1':
            data2.append([i,j])
            cheker = True
# print(data2)
# print((data2[1][1] + nums[1]), data[0][1])
if (data2[1][1] + nums[1]) == data2[0][1]:
    cheker = True
if not cheker:
    print("False")
else:
    # print(nums[0] - data2[1][0] -1 )
    if nums[0] - data2[1][0] - 1 == 3:
        romb_cheker(2, data2[0][0], data2[0][1])
    elif nums[0] - data2[1][0] - 1 == 5:
        romb_cheker(3, data2[0][0], data2[0][1])
    elif nums[0] - data2[1][0] - 1 == 7:
        romb_cheker(4, data2[0][0], data2[0][1])
    else:
        print("False")

