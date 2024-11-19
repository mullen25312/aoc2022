from dxx.superDailyPuzzle import SuperDailyPuzzle

# advent of code 2022 day 12
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        # read and parse input data
        self.parsed = self.data

    def part_one(self, **kwargs):
        self.part_one_result = 0

    def part_two(self, **kwargs):
        self.part_two_result = 0
