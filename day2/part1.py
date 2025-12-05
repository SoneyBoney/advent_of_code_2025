
filename = "input.txt"

with open(filename, 'r') as f:
    raw_input = f.read().split(',')
    ranges = [tuple(x.split('-')) for x in raw_input]

    invalids = []
    for r in ranges:
        low,high = tuple(int(x) for x in r)
        for num in range(low,high+1):
            if len(str(num)) % 2 != 0:
                continue
            num_str = str(num)
            midpoint = len(num_str) // 2
            if num_str[:midpoint] == num_str[midpoint:]:
                invalids.append(num)

    print(sum(invalids))
