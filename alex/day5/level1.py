with open('input.txt', 'r') as file:
    content = file.read()

parts = content.split("\n\n")

seeds = []
if parts[0].startswith("seeds: "):
    seeds = parts[0].split()[1:]

seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []

if parts[1].startswith("seed-to-soil map:"):
    for line in parts[1].split("\n")[1:]:
        destinationStart, sourceStart, range = map(int, line.split())
        seedToSoil.append((destinationStart, sourceStart, range))

if parts[2].startswith("soil-to-fertilizer map:"):
    for line in parts[2].split("\n")[1:]:
        destinationStart, sourceStart, range = map(int, line.split())
        soilToFertilizer.append((destinationStart, sourceStart, range))

if parts[3].startswith("fertilizer-to-water map:"):
    for line in parts[3].split("\n")[1:]:
        destinationStart, sourceStart, range = map(int, line.split())
        fertilizerToWater.append((destinationStart, sourceStart, range))

if parts[4].startswith("water-to-light map:"):
    for line in parts[4].split("\n")[1:]:
        destinationStart, sourceStart, range = map(int, line.split())
        waterToLight.append((destinationStart, sourceStart, range))

if parts[5].startswith("light-to-temperature map:"):
    for line in parts[5].split("\n")[1:]:
        destinationStart, sourceStart, range = map(int, line.split())
        lightToTemperature.append((destinationStart, sourceStart, range))

if parts[6].startswith("temperature-to-humidity map:"):
    for line in parts[6].split("\n")[1:]:
        destinationStart, sourceStart, range = map(int, line.split())
        temperatureToHumidity.append((destinationStart, sourceStart, range))

if parts[7].startswith("humidity-to-location map:"):
    for line in parts[7].split("\n")[1:]:
        destinationStart, sourceStart, range = map(int, line.split())
        humidityToLocation.append((destinationStart, sourceStart, range))

def getOuput(x, list):
    for f in list:
        destinationStart, sourceStart, range = map(int, f)

        if int(sourceStart) <= int(x) and int(x) <= int(sourceStart) + int(range):
            return int(destinationStart) + int(x) - int(sourceStart)
    return int(x)

minimum = 2**31 - 1
for seed in seeds:
    seed = getOuput(seed, seedToSoil)
    seed = getOuput(seed, soilToFertilizer)
    seed = getOuput(seed, fertilizerToWater)
    seed = getOuput(seed, waterToLight)
    seed = getOuput(seed, lightToTemperature)
    seed = getOuput(seed, temperatureToHumidity)
    seed = getOuput(seed, humidityToLocation)
    minimum = min(seed, minimum)

print("Result = " + str(minimum))