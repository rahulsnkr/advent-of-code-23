from collections import defaultdict

sum = 0

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            sets = line.split(":")[1].split(';')

            min_ball_cnt = defaultdict(int)
            for set in sets:
                balls = set.strip().split(',')
                for ball in balls:
                    ball_cnt = int(ball.strip().split(" ")[0])
                    ball_type = ball.strip().split(" ")[1]
                    min_ball_cnt[ball_type] = max(min_ball_cnt[ball_type], ball_cnt)
            print(min_ball_cnt)
            sum += (min_ball_cnt['red'] * min_ball_cnt['green'] * min_ball_cnt['blue'])

    print(sum)