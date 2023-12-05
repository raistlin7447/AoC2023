from dataclasses import dataclass, field

@dataclass
class Range:
    dest_start: int
    dest_end: int
    source_start: int
    source_end: int

    def __init__(self, dest_start: int, source_start: int, length: int) -> None:
        self.length = int(length)
        self.dest_start = int(dest_start)
        self.dest_end = self.dest_start + self.length - 1
        self.source_start = int(source_start)
        self.source_end = self.source_start + self.length - 1

    def is_included(self, source: int) -> bool:
        return self.source_start <= source <= self.source_end

    def get_destination(self, source: int) -> int:
        if not self.is_included(source):
            raise IndexError

        return source - self.source_start + self.dest_start


@dataclass
class Map:
    ranges: list[Range] = field(default_factory=list)

    def get_destination(self, source: int) -> int:
        for range in self.ranges:
            try:
                return range.get_destination(source)
            except IndexError:
                continue
        else:
            return source

seeds = []
maps = {}
with open('day05_input.txt') as f:
    chunks = f.read().split("\n\n")
    for chunk in chunks:
        lines = chunk.split("\n")
        if len(lines) == 1:
            seeds = [int(i) for i in lines[0].split(":")[1].split()]
        else:
            map, _ = lines[0].split()
            new_map = Map()
            for line in lines[1:]:
                dest, source, length = line.split()
                new_map.ranges.append(Range(dest, source, length))
            maps[map] = new_map

locations = []
for seed in seeds:
    soil = maps["seed-to-soil"].get_destination(seed)
    fertilizer = maps["soil-to-fertilizer"].get_destination(soil)
    water = maps["fertilizer-to-water"].get_destination(fertilizer)
    light = maps["water-to-light"].get_destination(water)
    temperature = maps["light-to-temperature"].get_destination(light)
    humidity = maps["temperature-to-humidity"].get_destination(temperature)
    location = maps["humidity-to-location"].get_destination(humidity)
    locations.append(location)

print(min(locations))