from pprint import pprint

filename = "input.txt"


def get_neighbor_inds(inds, rows, cols):
    i,j = inds
    candidates = [(i-1,j),(i+1,j),(i,j-1),(i,j+1),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]
    ret = [(x,y) for x,y in candidates if 0 <= x < rows and 0 <= y < cols]
    return ret

def new_grid(old, remove_list):
    old = [list(x) for x in old]
    rows = len(old)
    cols = len(old[0])
    
    for i in range(rows):
        for j in range(cols):
            if (i,j) not in remove_list: continue
            old[i][j] = '.'
    return [''.join(x) for x in old]

with open(filename,'r') as f:
    raw_input = [x for x in f.read().split('\n') if x]

    ans = 0
    
    rows = len(raw_input)
    cols = len(raw_input[0])


    while True:
        temp_list = []
        for i in range(rows):
            for j in range(cols):
                if raw_input[i][j] == '.':
                    continue
                temp_count = 0
                for nb in get_neighbor_inds((i,j), rows, cols):
                    ii,jj = nb
                    if raw_input[ii][jj] == '@': 
                        temp_count += 1
                if temp_count < 4:
                    ans += 1
                    temp_list.append((i,j))
        if not temp_list:
            break
        raw_input = new_grid(raw_input, temp_list)
        
      
    print(ans)
