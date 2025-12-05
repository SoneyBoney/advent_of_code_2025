


filename = 'input.txt'

with open(filename, 'r') as f:
    raw_input = [x for x in f.read().split('\n') if x]
    print(raw_input)

    count = 50
    ans = 0

    for x in raw_input:
        num = int(x[1:])
        if x[0] == 'L':
            count -= num
        else:
            count += num
        count %= 100
        if count == 0:
            ans += 1
        print(count)
    print(ans) 
