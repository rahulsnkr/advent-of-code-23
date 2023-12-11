input = []
galaxies = []
sum = 0

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if all(c == '.' for c in line):
                input.append(line)
            input.append(line)

        col_idx = []
        for i,col in enumerate(zip(*input)): 
            if all(c == '.' for c in col):
                col_idx.append(i)
        
        for i,col in enumerate(col_idx):
            for j,row in enumerate(input):
                new_row = row[:col+i] + '.' + row[col+i:]
                input[j] = new_row

        for i,line in enumerate(input):
            for j,c in enumerate(line):
                if c == '#':
                    galaxies.append((i,j))

        for i in range(len(galaxies) - 1):
            for j in range(i+1, len(galaxies)):
                galaxy_a = galaxies[i]
                galaxy_b = galaxies[j]
                dx = abs(galaxy_a[0] - galaxy_b[0])
                dy = abs(galaxy_a[1] - galaxy_b[1])
                sum += dx + dy
        
        print(sum)
        
