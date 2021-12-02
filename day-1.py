def get_amount_of_increased_measurements():
    with open('inputs/day-1.txt') as input:
        number_of_increases = 0
        last_depth = -1

        for line in input:
            if int(line) > last_depth and last_depth != -1:
                number_of_increases = number_of_increases + 1
            last_depth = int(line)
        
        print(number_of_increases)

def get_amount_of_increased_measurements_in_sliding_window():
    with open('inputs/day-1.txt') as input:
        number_of_increases = 0
        last_sum = 0
        depths_list = []

        for line in input:
            current_sum = 0
            depths_list.append(int(line))

            if len(depths_list) == 3:
                for i in depths_list:
                    current_sum += i
                del depths_list[0]
            if current_sum > last_sum and last_sum != 0:
                number_of_increases = number_of_increases + 1
            last_sum = current_sum
        
        print(number_of_increases)

def main():
    get_amount_of_increased_measurements()
    get_amount_of_increased_measurements_in_sliding_window()

if __name__ == "__main__":
    main()