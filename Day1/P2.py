file = open('input.txt', 'r')
inputs = file.readlines()
values = []
for line in inputs:
    values.append(int(line))
values.sort()
flag = 0
for i in range(len(values)):
    check = 2020 - values[i]
    start = 0
    end = len(values) - 1
    sum = values[start] + values[end]
    while start < end:
        if(start == i):
            start += 1
            sum = values[start] + values[end]
        elif(end == i):
            end +- 1
            sum = values[start] + values[end]
        elif(sum == check):
            print(values[start] * values[end] * values[i])
            flag = 1
            break
        elif(sum < check):
            start += 1
            sum = values[start] + values[end]
        elif(sum > check):
            end -= 1
            sum = values[start] + values[end]
    if flag == 1:
        break