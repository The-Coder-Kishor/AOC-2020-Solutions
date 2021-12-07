file = open('input.txt', 'r')
inputs = file.readlines()
values = []
for line in inputs:
    values.append(int(line))
values.sort()
start = 0
end = len(values) - 1
sum = values[start] + values[end]
while(True):
    if sum == 2020:
        print(values[start] * values[end])
        break
    elif sum < 2020:
        start += 1
        sum = values[start] + values[end]
    elif sum > 2020:
        end -= 1
        sum = values[start] + values[end]
