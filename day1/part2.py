filename = 'input.txt'
with open(filename, 'r') as f:
    raw_input = [x for x in f.read().split('\n') if x]
    count = 50
    ans = 0
    for x in raw_input:
        distance = int(x[1:])
        if x[0] == 'L':
            count = 100-count
            d,r = divmod(count+distance,100)
            ans+=d if count != 100 else d-1
            count=(100-r)%100
        else:
            d,r = divmod(count+distance,100) 
            ans+=d
            count=r
    print(ans) 
