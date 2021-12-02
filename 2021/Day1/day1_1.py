with open("1_1codeinput.txt") as file:
    count = 0
    prev = 143
    for line in file:
        count += prev < int(line)
        prev = int(line)
        
    print(count)
