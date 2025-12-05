from pprint import pprint

filename = "test.txt"


def get_neighbor_inds(inds, rows, cols):
    i,j = inds
    candidates = [(i-1,j),(i+1,j),(i,j-1),(i,j+1),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]
    ret = [(x,y) for x,y in candidates if 0 <= x < rows and 0 <= y < cols]
    return ret


with open(filename,'r') as f:
    raw_input = [x for x in f.read().split('\n') if x]
    pprint(raw_input)

    ans = 0
    debug = []
    rows = len(raw_input)
    cols = len(raw_input[0])

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
                debug.append((i,j))
      
    print(debug)
    print(ans)
