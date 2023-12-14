patterns = []
total = 0

def get_lor(pattern):
    for i in range(len(pattern)):
        smudges = []
        for up, down in zip(pattern[i-1::-1], pattern[i:]):
            for up_c, down_c in zip(up, down):
                if up_c != down_c:
                    smudges.append(1)
                else:
                    smudges.append(0)
        if sum(smudges) == 1:
            return i
    return 0

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        pattern = []
        for line in f:
            line = line.strip()
            if line == '':
                patterns.append(pattern)
                pattern = []
            else:
                pattern.append(line)
        patterns.append(pattern)
        
        for pattern in patterns:
           total += (100 * get_lor(pattern)) + (get_lor([*zip(*pattern)]))

    print(total)