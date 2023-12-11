input = []
galaxies = []
row_idx = []
col_idx = []
sum = 0

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if all(c == '.' for c in line):
                row_idx.append(len(input))
            input.append(line)

        for i,col in enumerate(zip(*input)): 
            if all(c == '.' or c == '-' for c in col):
                col_idx.append(i)

        for i,line in enumerate(input):
            for j,c in enumerate(line):
                if c == '#':
                    galaxies.append((i,j))

        for i in range(len(galaxies) - 1):
            for j in range(i+1, len(galaxies)):
                a_x = galaxies[i][0]
                a_y = galaxies[i][1]
                b_x = galaxies[j][0]
                b_y = galaxies[j][1]
                
                mil_count = 0
                dx = abs(a_x - b_x)
                dy = abs(a_y - b_y)

                for r_i in row_idx:
                    if r_i > min(a_x, b_x) and r_i < max(a_x, b_x):
                        mil_count += 1

                for c_i in col_idx:
                    if c_i > min(a_y, b_y) and c_i < max(a_y, b_y):
                        mil_count += 1

                sum += dx + dy + (999999*mil_count)
        
        print(sum)
        
