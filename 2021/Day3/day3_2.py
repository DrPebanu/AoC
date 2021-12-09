input_list = []
ogr = []
co2 = []

def find_the_code(code_list, i, rating):
    if len(code_list) == 1:
        return
    
    number_of_ones = 0
    line_count = 0
    for e in code_list:
        number_of_ones += int(e[i])
        line_count += 1
 
    if number_of_ones >= line_count - number_of_ones:
        save_bit = True
    else:
        save_bit = False

    if rating == "ogr":
        ogr.clear()
        for e in code_list:
            if int(e[i]) == int(save_bit):
                ogr.append(e)
        find_the_code(ogr.copy(), i+1, rating)

    elif rating == "co2":
        co2.clear()
        for e in code_list:
            if number_of_ones == line_count - number_of_ones:
                save_bit == False
            if int(e[i]) == int(not save_bit):
                co2.append(e)
        find_the_code(co2.copy(), i+1, rating)



with open("3input.txt") as file:
    for e in file:
        input_list.append(e.strip())

find_the_code(input_list, 0, "ogr")
oxy_gen = int(ogr[0], 2)

find_the_code(input_list, 0, "co2")
co2_scr = int(co2[0], 2)

life_support_rating = oxy_gen * co2_scr
print(life_support_rating)