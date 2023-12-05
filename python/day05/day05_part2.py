import sys
from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class MapRange:
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

    def get_destination(self, source: int) -> int:
        if not self.source_start <= source <= self.source_end:
            return source

        return source - self.source_start + self.dest_start


@dataclass
class Map:
    map_ranges: list[MapRange] = field(default_factory=list)

    def map_source_range(self, source_ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        dests = []
        for begin, end in source_ranges:
            for source_range in self.map_ranges:
                overlap_start = max(begin, source_range.source_start)
                overlap_end = min(end, source_range.source_end)

                if overlap_start <= overlap_end:
                    if begin <= overlap_start - 1:
                        dests.append((begin, overlap_start - 1))

                    dests.append((source_range.get_destination(overlap_start), source_range.get_destination(overlap_end)))

                    if overlap_end + 1 <= end:
                        begin = overlap_end + 1
                    else:
                        begin = sys.maxsize
                        break

            if begin <= end:
                dests.append((begin, end))

        return dests


@dataclass
class SeedRange:
    seed_start: int
    seed_end: int

    def __init__(self, seed_start, seed_length):
        self.seed_length = seed_length
        self.seed_start = seed_start
        self.seed_end = self.seed_start + self.seed_length - 1

    def is_valid(self, seed: int) -> bool:
        return self.seed_start <= seed <= self.seed_end

seeds = []
maps = {}
with open('day05_input.txt') as f:
    chunks = f.read().split("\n\n")
    for chunk in chunks:
        lines = chunk.split("\n")
        if len(lines) == 1:
            seed_list = [int(i) for i in lines[0].split(":")[1].split()]
            for seed_start, seed_length in [seed_list[i:i + 2] for i in range(0, len(seed_list), 2)]:
                seeds.append(SeedRange(seed_start, seed_length))
            seeds.sort(key=lambda x: x.seed_start)
        else:
            map, _ = lines[0].split()
            new_map = Map()
            for line in lines[1:]:
                dest, source, length = line.split()
                new_map.map_ranges.append(MapRange(dest, source, length))
            new_map.map_ranges.sort(key=lambda x: x.source_start)
            maps[map] = new_map

min_location = sys.maxsize
for seed_range in seeds:
    soil = maps["seed-to-soil"].map_source_range([(seed_range.seed_start, seed_range.seed_end)])
    fertilizer = maps["soil-to-fertilizer"].map_source_range(soil)
    water = maps["fertilizer-to-water"].map_source_range(fertilizer)
    light = maps["water-to-light"].map_source_range(water)
    temperature = maps["light-to-temperature"].map_source_range(light)
    humidity = maps["temperature-to-humidity"].map_source_range(temperature)
    location = maps["humidity-to-location"].map_source_range(humidity)
    for l in location:
        min_location = min(min_location, l[0])

print(min_location)