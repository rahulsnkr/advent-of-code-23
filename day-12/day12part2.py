from functools import lru_cache

@lru_cache(maxsize=None)
def num_confs(spring, nums, consuming_group):
    func = lambda x: (x[0] - 1,) + x[1:]

    # base cases
    if not nums:
        return 0 if "#" in spring else 1
    elif not spring:
        return 0 if sum(nums) else 1
    
    elif nums[0] == 0:
        return num_confs(spring[1:], nums[1:], False) if spring[0] in ["?", "."] else 0
    
    elif consuming_group:
        return num_confs(spring[1:], func(nums), True) if spring[0] in ["?", "#"] else 0
    
    elif spring[0] == "#":
        return num_confs(spring[1:], func(nums), True)
    elif spring[0] == ".":
        return num_confs(spring[1:], nums, False)
    else: #?
        return num_confs(spring[1:], nums, False) + num_confs(spring[1:], func(nums), True)

total = 0
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            nums = [int(x) for x in line.split(' ')[1].split(',')*5]
            spring = '?'.join([line.split(' ')[0]]*5)

            total += num_confs(spring, tuple(nums), False)

        print(total)