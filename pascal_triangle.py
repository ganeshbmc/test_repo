def pascal(n):
    pattern = [[1], [1, 1]]
    for i in range(2, n):
        prev = pattern[-1]
        curr = [ ]
        for i in range(len(prev) - 1):
            curr.append(prev[i] + prev[i + 1])
        curr = [1] + curr + [1]
        pattern.append(curr)
    return pattern

def printPascal(pattern, n):
    for line in pattern:
        line_str = [str(word) for word in line]
        line_str = ' '.join(line_str)
        print(f'{line_str:^{5 * n}s}')

n = 10
pattern = pascal(n)
printPascal(pattern, n)