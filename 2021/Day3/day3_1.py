positions =  [0,0,0,0,0,0,0,0,0,0,0,0]
gamma_binary = [0,0,0,0,0,0,0,0,0,0,0,0]
line_count = 0

with open("3input.txt") as file:
    for line in file:
        for i, char in enumerate(line.strip()):
            positions[i] += int(char)

        line_count += 1

for i, pos in enumerate(positions):
    gamma_binary[i] = int(pos > (line_count - pos))


string_gamma = "".join([str(e) for e in gamma_binary])
string_epsilon = "".join([str(int(not e)) for e in gamma_binary])

fuel_consumption = int(string_gamma, 2) * int(string_epsilon, 2)
print(string_gamma)
print(fuel_consumption)