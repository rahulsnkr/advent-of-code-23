import multiprocessing

input = []
seeds = []
seed_soil_vals = []
soil_fertilizer_vals = []
fertilizer_water_vals = []
water_light_vals = []
light_temp_vals = []
temp_humidity_vals = []
humidity_loc_vals = []

def get_seed_loc(seed_num_start, seed_num_range, min_seed_locs, idx):
    print('start: ' + str(seed_num_start))
    min_seed_loc = -1
    for j in range(seed_num_range):
        seed_soil = get_val_from_list(seed_num_start+j, seed_soil_vals)
        seed_fertilizer = get_val_from_list(seed_soil, soil_fertilizer_vals)
        seed_water = get_val_from_list(seed_fertilizer, fertilizer_water_vals)
        seed_light = get_val_from_list(seed_water, water_light_vals)
        seed_temp = get_val_from_list(seed_light, light_temp_vals)
        seed_humidity = get_val_from_list(seed_temp, temp_humidity_vals)
        seed_loc = get_val_from_list(seed_humidity, humidity_loc_vals)
        min_seed_loc = min(seed_loc, min_seed_loc)
    min_seed_locs[idx] = min_seed_loc
    print('end: ' + str(seed_num_start))


def get_vals_from_inp(lines, idx, map):
    while idx < len(lines) and lines[idx] != '\n':
        vals = [int(x) for x in lines[idx].strip().split(" ")]
        map.append(vals)
        idx += 1

def get_val_from_list(query, map):
    res = query
    for (dest, src, length) in map:
        if query >= src and query < src + length:
            res = query - src + dest
    return res

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            input.append(line)
        seed_nums = [int(x) for x in input[0].split(":")[1].strip().split(" ")]
        
        get_vals_from_inp(input, input.index("seed-to-soil map:\n")+1, seed_soil_vals)
        get_vals_from_inp(input, input.index("soil-to-fertilizer map:\n")+1, soil_fertilizer_vals)
        get_vals_from_inp(input, input.index("fertilizer-to-water map:\n")+1, fertilizer_water_vals)
        get_vals_from_inp(input, input.index("water-to-light map:\n")+1, water_light_vals)
        get_vals_from_inp(input, input.index("light-to-temperature map:\n")+1, light_temp_vals)
        get_vals_from_inp(input, input.index("temperature-to-humidity map:\n")+1, temp_humidity_vals)
        get_vals_from_inp(input, input.index("humidity-to-location map:\n")+1, humidity_loc_vals)

        min_seed_locs = [float("inf")] * (len(seed_nums) // 2)
        procs = []
        
        for i in range((len(seed_nums) // 2)):
            procs.append(multiprocessing.Process(target=get_seed_loc, args=(seed_nums[2*i], seed_nums[(2*i)+1], min_seed_locs, i)))    
            procs[i].start()

        for i in range((len(seed_nums) // 2)):
            procs[i].join()
        print(min(min_seed_locs))    
        
