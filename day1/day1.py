# Part 1
# with open("input.txt", "r") as file:
#     lines = file.readlines()
#     left = []
#     right = []
#     diffs = []

#     for line in lines:
#         lineStr = line.strip().split("   ")
#         left.append(lineStr[0])
#         right.append(lineStr[1])

#     left.sort()
#     right.sort()

#     for i in range(len(left)):
#         diff = int(left[i]) - int(right[i])
#         diffs.append(abs(diff))

#     print(sum(diffs))


# Part 2
with open("input.txt", "r") as file:
    lines = file.readlines()
    left = []
    right = []
    diffs = []

    for line in lines:
        lineStr = line.strip().split("   ")
        left.append(int(lineStr[0]))
        right.append(int(lineStr[1]))

    left.sort()
    right.sort()

    appearRight = {}

    for num in right:
        if num in appearRight:
            appearRight[num] += 1
        else:
            appearRight[num] = 1

    for num in left:
        diffs.append(num * appearRight.get(num, 0))

    print(sum(diffs))
