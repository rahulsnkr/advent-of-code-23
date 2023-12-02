id_sum = 0
max_cnts = {
    "red": 12,
    "green": 13,
    "blue": 14
}

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            game_id = int(line.split(":")[0].split(" ")[1])
            sets = line.split(":")[1].split(';')
            is_possible = True

            for set in sets:
                balls = set.strip().split(',')
                for ball in balls:
                    ball_cnt = int(ball.strip().split(" ")[0])
                    ball_type = ball.strip().split(" ")[1]
                    is_possible &= (False if ball_cnt > max_cnts[ball_type] else True)
            id_sum = (id_sum + game_id) if is_possible == True else id_sum
            is_possible = True

    print(id_sum)