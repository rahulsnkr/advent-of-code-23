input = []
res = 1
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            input.append(line)
        times = [int(x) for x in input[0].split(':')[1].strip().split(' ') if x.isdigit()]
        dists = [int(x) for x in input[1].split(':')[1].strip().split(' ') if x.isdigit()]
        
        for time,dist in zip(times, dists):
            num_times_record_broken = 0
            for i in range(time):
                rem_time = time - i
                boat_speed = i
                num_times_record_broken += 1 if boat_speed * rem_time > dist else 0
            res *= num_times_record_broken
        print(res)
        
