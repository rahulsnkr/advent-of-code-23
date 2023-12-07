input = []

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            input.append(line)
        times = [x for x in input[0].split(':')[1].strip().split(' ') if x.isdigit()]
        dists = [x for x in input[1].split(':')[1].strip().split(' ') if x.isdigit()]

        big_time = int(''.join(times))
        big_dist = int(''.join(dists))

        num_times_record_broken = 0
        for i in range(big_time):
            rem_time = big_time - i
            boat_speed = i
            num_times_record_broken += 1 if boat_speed * rem_time > big_dist else 0
        print(num_times_record_broken)

        
