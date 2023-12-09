from math import gcd

input = []

def get_steps_for_node(dirs, nodes, cur_node, end_nodes):
    idx = 0
    steps = 0
    while cur_node not in end_nodes:
        cur_dir = dirs[idx]
        cur_node = nodes[cur_node][0] if cur_dir == 'L' else nodes[cur_node][1] 
        steps += 1
        idx += 1
        if idx == len(dirs):
            idx = 0
    return steps
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
        
        cur_nodes = [node for node in nodes if node[-1] == 'A']
        end_nodes = [node for node in nodes if node[-1] == 'Z']
        steps = []
        for cur_node in cur_nodes:
            steps.append(get_steps_for_node(dirs, nodes, cur_node, end_nodes))
        
        total_steps = 1
        for num_steps in steps:
            total_steps = total_steps*num_steps // gcd(total_steps, num_steps)
        print(total_steps)
