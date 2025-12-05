import itertools as it


def divisors(n):
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            j = n // i
            if j != i and j < n: 
                divs.append(j)
    return sorted(divs)

filename = "input.txt"

with open(filename, 'r') as f:
    raw_input = f.read().split(',')
    ranges = [tuple(x.split('-')) for x in raw_input]

    invalids = []
    for r in ranges:
        low,high = tuple(int(x) for x in r)
        for num in range(low,high+1):
            num_str = str(num)
            str_len = len(num_str)
            divs = divisors(str_len)
            for d in divs:
                temp = list(it.batched(num_str, d))
                if all(x == temp[0] for x in temp):
                    if str_len >= 2:
                        invalids.append(num)
                        break

    print(invalids)
    print(sum(invalids))



