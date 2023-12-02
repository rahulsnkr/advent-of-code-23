import re

sum = 0
nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            regex_pattern = '(?=(\d+|' + '|'.join(nums) + '))'
            matches = re.finditer(regex_pattern, line)
            matches_lst = [i.group(1) for i in matches]

            first_num = int(matches_lst[0][0]) if matches_lst[0].isdigit() else num_map[matches_lst[0]]
            last_num = int(matches_lst[-1][-1]) if matches_lst[-1].isdigit() else num_map[matches_lst[-1]]

            cur_num = first_num * 10 + last_num
            sum += cur_num
