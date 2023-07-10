def elevator_floor(enter, exit):
    floor=enter
    elevator_direction=""
    if enter>exit:
        elevator_direction="Going Down: "
        while floor >= exit:
            elevator_direction += str(floor)
            if floor>exit:
                elevator_direction += " | "
            floor -= 1
    elif enter<exit:
        elevator_direction="Going Up: "
        while floor <= exit:
            elevator_direction += str(floor)
            if floor<exit:
                elevator_direction += " | "
            floor += 1        
    else:
        print("You are already on the same floor")
    return elevator_direction

print(elevator_floor(6,1))