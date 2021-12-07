file = open('input.txt', 'r')
inputs = file.readlines()
valid = 0
for i in range(len(inputs)):
    parts = inputs[i].split()
    min = int(parts[0].split('-')[0])
    max = int(parts[0].split('-')[1])
    letter = parts[1][0]
    password = parts[2]
    x = password.count(letter)
    if x >= min and x <= max:
        valid += 1
print(valid)