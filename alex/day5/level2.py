with open('input.txt', 'r') as file:
    content = file.read()

parts = content.split("\n\n")

seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []

if parts[1].startswith("seed-to-soil map:"):
    for line in parts[1].split("\n")[1:]:
        destinationStart, sourceStart, length = map(int, line.split())
        seedToSoil.append((destinationStart, sourceStart, length))

if parts[2].startswith("soil-to-fertilizer map:"):
    for line in parts[2].split("\n")[1:]:
        destinationStart, sourceStart, length = map(int, line.split())
        soilToFertilizer.append((destinationStart, sourceStart, length))

if parts[3].startswith("fertilizer-to-water map:"):
    for line in parts[3].split("\n")[1:]:
        destinationStart, sourceStart, length = map(int, line.split())
        fertilizerToWater.append((destinationStart, sourceStart, length))

if parts[4].startswith("water-to-light map:"):
    for line in parts[4].split("\n")[1:]:
        destinationStart, sourceStart, length = map(int, line.split())
        waterToLight.append((destinationStart, sourceStart, length))

if parts[5].startswith("light-to-temperature map:"):
    for line in parts[5].split("\n")[1:]:
        destinationStart, sourceStart, length = map(int, line.split())
        lightToTemperature.append((destinationStart, sourceStart, length))

if parts[6].startswith("temperature-to-humidity map:"):
    for line in parts[6].split("\n")[1:]:
        destinationStart, sourceStart, length = map(int, line.split())
        temperatureToHumidity.append((destinationStart, sourceStart, length))

if parts[7].startswith("humidity-to-location map:"):
    for line in parts[7].split("\n")[1:]:
        destinationStart, sourceStart, length = map(int, line.split())
        humidityToLocation.append((destinationStart, sourceStart, length))

def getOuput(x, list):
    for f in list:
        destinationStart, sourceStart, length = map(int, f)

        if int(sourceStart) <= int(x) and int(x) <= int(sourceStart) + int(length):
            return int(destinationStart) + int(x) - int(sourceStart)
    return int(x)

def get_all_seeds():
    seeds = list(map(int, parts[0].split()[1:]))  # Extract seed values from the line
    unique_seeds = set()

    for i in range(0, len(seeds), 2):
        start, length = seeds[i], seeds[i + 1]
        seed_range = range(start, start + length)
        unique_seeds.update(seed_range)

    return sorted(list(unique_seeds))

def merge_overlapping_pairs(pair_list):
    pair_list.sort()

    merged_pairs = [pair_list[0]]

    for current_pair in pair_list[1:]:
        previous_pair = merged_pairs[-1]

        if current_pair[0] <= previous_pair[0] + previous_pair[1]:
            merged_pairs[-1] = (previous_pair[0], max(previous_pair[0] + previous_pair[1], current_pair[0] + current_pair[1]) - previous_pair[0])
        else:
            merged_pairs.append(current_pair)

    return merged_pairs

#def combine_overlapping_ranges():
#    seeds = list(map(int, parts[0].split()[1:]))
#    ranges = list(zip(seeds[::2], seeds[1::2]))  # Create pairs of start and length
#
#    merged_ranges = []
#
#    # Sort the ranges based on their starting values
#    sorted_ranges = sorted(ranges, key=lambda x: x[0])
#
#    current_range = sorted_ranges[0]
#
#    for start, length in sorted_ranges[1:]:
#        # Check for overlap
#        if start <= current_range[0] + current_range[1] - 1:
#            # Merge overlapping ranges
#            current_range = (current_range[0], max(current_range[1], start + length - current_range[0]))
#        else:
#            # Add non-overlapping range to the result
#            merged_ranges.append(current_range)
#            current_range = (start, length)
#
#    merged_ranges.append(current_range)  # Add the last range
#
#    # Generate the combined list of seeds
#    combined_seeds = [seed for start, length in merged_ranges for seed in range(start, start + length)]
#
#    return combined_seeds

seeds = list(map(int, parts[0].split()[1:]))
ranges = list(zip(seeds[::2], seeds[1::2]))

minimum = 2**31 - 1
for start, r in merge_overlapping_pairs(ranges):
    for seed in range(r):
        seed += start
        #print(seed)
        seed = getOuput(seed, seedToSoil)
        seed = getOuput(seed, soilToFertilizer)
        seed = getOuput(seed, fertilizerToWater)
        seed = getOuput(seed, waterToLight)
        seed = getOuput(seed, lightToTemperature)
        seed = getOuput(seed, temperatureToHumidity)
        seed = getOuput(seed, humidityToLocation)
        minimum = min(seed, minimum)

print("Result = " + str(minimum))