sum = 0

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            nums = line.split(":")[1]
            winning_nums = list(filter(None, nums.split('|')[0].strip().split(" ")))
            my_nums = list(filter(None, nums.split('|')[1].strip().split(" ")))
            matches = 0
            for my_num in my_nums:
                if my_num in winning_nums:
                    matches += 1
            sum += 2**(matches - 1) if matches > 0 else 0
    print(sum)