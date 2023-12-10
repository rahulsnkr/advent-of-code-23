sum = 0
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            sequence = [int(x) for x in line.split(' ')]
            # print(sequence)

            sequences = [sequence]
            while not all(num == 0 for num in sequence):
                new_sequence = []
                for i in range(1, len(sequence)):
                    new_sequence.append(sequence[i] - sequence[i-1])
                sequences.append(new_sequence)
                sequence = sequences[-1]
            
            sequences[-1].insert(0, 0)
            for i in range(len(sequences) - 2, -1, -1):
                sequences[i].insert(0, sequences[i][0] - sequences[i+1][0])
            sum += sequences[0][0]
        print(sum)
            

        