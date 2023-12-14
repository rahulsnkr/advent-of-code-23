patterns = []
total = 0

def get_horizontal_lor(pattern):
    lor = 0
    
    while lor < len(pattern) - 1:
        lor += 1
        up = pattern[:lor]
        up.reverse()
        down = pattern[lor:]
        is_found = True
        for up_line, down_line in zip(up, down):
            if up_line != down_line:
                is_found = False
                break
        if is_found:
            return lor
    return -1

def get_vertical_lor(pattern):
    pattern_t = list(zip(*pattern))
    return get_horizontal_lor(pattern_t)
        

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
            h = get_horizontal_lor(pattern)
            if h == -1:
                v = get_vertical_lor(pattern)
                total += v
            else:
                total += 100*h
    print(total)
        
