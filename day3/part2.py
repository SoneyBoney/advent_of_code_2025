
def max_ind(num_list):
    temp_max = num_list[0]
    temp_ind = 0
    
    for i,n in enumerate(num_list):
        if i == 0:
            continue
        if n > temp_max:
            temp_max = n
            temp_ind = i
    
    return temp_max,temp_ind
filename = "input.txt"

with open(filename, 'r') as f:
    raw_input = [x for x in f.read().split('\n') if x]

    joltages = []
    for bank in raw_input:
        bank_ints = [int(x) for x in bank]

        temp_list = []
        start_ind = 0
        for j in range(11,0,-1):
            check_region = bank_ints[start_ind:-j]
            region_max,temp_ind = max_ind(check_region)
            start_ind += temp_ind+1
            temp_list.append(region_max)

        region_max,_ = max_ind(bank_ints[start_ind:])
        temp_list.append(region_max)

        joltages.append(int(''.join([str(x) for x in temp_list])))

    print(joltages)
    print(sum(joltages))



