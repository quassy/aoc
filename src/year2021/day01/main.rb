class BaseDay
    repeat_count = 1000

    def initialize(path)
        @test_input = File.read(path + "test_input.txt")
        @input = File.read(path + "input.txt")
        puts @test_input
    end

    def transform_input(input_list)
        return input_list
    end

    def test_part1(test_output)
        puts __method__.to_s + ": " + self.part1(@test_input).to_s
        # if test_output:
        #     assert self.part1(self.test_input) == test_output
        # end
    end

    def test_part2(test_output)
        puts __method__.to_s + ": " + self.part2(@test_input).to_s
        # if test_output:
        #     assert self.part2(self.test_input) == test_output
        # end
    end

    def main_part1(main_output)
        puts __method__.to_s + ": " + self.part1(@input).to_s
        # if main_output:
        #     assert self.part1(self.input) == main_output
        # end
    end

    def main_part2(main_output)
        puts __method__.to_s + ": " + self.part2(@input).to_s
        # if main_output:
        #     assert self.part2(self.input) == main_output
        # end
    end

    def time_part1
        self.part1(@input)
    end

    def time_part2
        self.part2(@input)
    end

    def part1(input_list)
        return 0
    end

    def part2(input_list)
        return 0
    end

end


day = BaseDay.new("src/year2021/day01/")

day.test_part1 198
day.main_part1 3895776
day.test_part2 230
day.main_part2 7928162

day.time_part1
day.time_part2
