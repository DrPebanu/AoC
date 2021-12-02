depth = 0 
pos = 0

with open("2input.txt") as file:
    
    for line in file:

        x = [int(s) for s in line.split() if s.isdigit()]
        if line[0] == "f":
            pos += x[0]
        elif line[0] == "d":
            depth += x[0]
        elif line[0] == "u":
            depth -= x[0]

    print(depth * pos)
            
