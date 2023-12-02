import re
sum = 0
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            numbers = re.findall('\d+', line)
            first_num = int(str(numbers[0])[0])
            last_num = int(str(numbers[-1])[-1])
            cur_num = first_num * 10 + last_num
            sum += cur_num

    print(sum)     

