input = []
steps = 0
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            input.append(line.strip())
        dirs = input[0]
        nodes = {}
        for i in range(2, len(input)):
            start = input[i].split('=')[0].strip()
            left = input[i].split('=')[1].split(',')[0].strip()[1:]
            right = input[i].split('=')[1].split(',')[1].strip()[:-1]
            nodes[start] = (left,right)
        
        cur_node = 'AAA'
        idx = 0
        while cur_node != 'ZZZ':
            cur_dir = dirs[idx]
            cur_node = nodes[cur_node][0] if cur_dir == 'L' else nodes[cur_node][1]
            steps += 1
            idx += 1
            if idx == len(dirs):
                idx = 0
        print(steps)
