from collections import defaultdict

sum = 0
copies = defaultdict(lambda:1)

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            cur_card_num = int(list(filter(None, line.split(":")[0].split(" ")))[1])

            nums = line.split(":")[1]
            winning_nums = list(filter(None, nums.split('|')[0].strip().split(" ")))
            my_nums = list(filter(None, nums.split('|')[1].strip().split(" ")))
            matches = 0
            for my_num in my_nums:
                if my_num in winning_nums:
                    matches += 1
            if matches > 0:
                for card_copy_num in range(cur_card_num+1, cur_card_num+matches+1):
                    copies[card_copy_num] += copies[cur_card_num]
    for i in range(1, cur_card_num+1):
        sum += copies[i]
    print(sum)