with open("1_2codeinput.txt") as file:
    code_input =[]

    for line in file:
        code_input.append(int(line))

new_values = []
for i, code in enumerate(code_input):
    if i == len(code_input) - 2:
        break
    
    new_values.append(code+code_input[i+1]+code_input[i+2])




prev = new_values[0]
increasedcount = 0
for value in new_values:
    increasedcount += prev < value
    prev = value

print(increasedcount)
        