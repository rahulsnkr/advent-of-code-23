input = []
total = 0

def sums(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation

def get_pos_configs(spring_len, nums):
    total_nums = sum(nums)
    total_dots = spring_len - total_nums
    confirmed_dots = len(nums) - 1
    all_perms = []

    initial_spring = ['#'*num for num in nums]

    buckets = len(nums) + 1
    dots_to_ins = total_dots - confirmed_dots
    perms = sums(buckets, dots_to_ins)
    for perm in perms:
        s = ''
        s = '.'*perm[0]
        for i in range(len(initial_spring) - 1):
            s += initial_spring[i]
            s += '.'*perm[i+1] + '.'
        s += initial_spring[-1] + '.'*perm[-1]
        all_perms.append(s)

    return all_perms

def get_total_ways(spring, pos_configs):
    if pos_configs == []:
        return 1
    sum = 0
    for config in pos_configs:
        is_possible = True
        
        for s_c, p_c in zip(spring, config):
            if p_c == '.' and s_c == '#' or p_c == '#' and s_c == '.':
                is_possible = False
                break
        sum += 1 if is_possible else 0
    return sum

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            nums = [int(x) for x in line.split(' ')[1].split(',')]
            spring = line.split(' ')[0]
            
            pos_configs = get_pos_configs(len(spring), nums)
            total += get_total_ways(spring, pos_configs)

        print(total)