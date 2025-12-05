
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
        first_half = bank_ints[:-1]
        first,first_ind = max_ind(first_half)
        
        second_half = bank_ints[first_ind+1:]
        second,_ = max_ind(second_half)
        joltages.append(int(f'{first}{second}')) 

    print(joltages)
    print(sum(joltages))



