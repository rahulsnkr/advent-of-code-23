engine = []
sum = 0

def get_number(x,y,cols):
    cur_num = engine[x][y]
    idx = y-1
    while idx >= 0 and engine[x][idx].isdigit():
        cur_num = engine[x][idx] + cur_num
        idx -= 1

    idx = y+1
    while idx < cols and engine[x][idx].isdigit():
        cur_num = cur_num + engine[x][idx]
        idx += 1
    
    return int(cur_num)

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
          engine.append(line.strip())
        
        rows = len(engine)
        cols = len(engine[0])
        for i in range(rows):
            for j in range(cols):
                if engine[i][j] == '*':
                    adjacent_nums = set()
                    for x in [-1,0,1]:
                        for y in [-1,0,1]:
                            if i+x >= 0 and i+x < rows and j+y >=0 and j+y < cols:
                                if(engine[i+x][j+y].isdigit()):
                                    adjacent_nums.add(get_number(i+x,j+y,cols))
                    if len(adjacent_nums) == 2:
                        gear_ratio = 1
                        for adjacent_num in adjacent_nums:
                            gear_ratio *= adjacent_num
                        sum += gear_ratio
        print(sum)