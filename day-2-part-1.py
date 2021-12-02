def follow_planned_course():
    horizontal_position = 0
    depth = 0

    with open('inputs/day-2.txt') as input:
        for line in input:
            direction, unit = line.strip().split(' ')
            if direction == "forward":
                horizontal_position = horizontal_position + int(unit)
            elif direction == "down":
                depth = depth + int(unit)
            elif direction == "up":
                depth = depth - int(unit)
    
    print(horizontal_position * depth)


def follow_planned_course_with_aim():
    horizontal_position = 0
    depth = 0
    aim = 0

    with open('inputs/day-2.txt') as input:
        for line in input:
            direction, unit = line.strip().split(' ')
            if direction == "forward":
                horizontal_position = horizontal_position + int(unit)
                depth = depth + (int(unit) * aim)
            elif direction == "down":
                aim = aim + int(unit)
            elif direction == "up":
                aim = aim - int(unit)
    
    print(horizontal_position * depth)


def main():
    follow_planned_course()
    follow_planned_course_with_aim()

if __name__ == "__main__":
    main()