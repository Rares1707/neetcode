class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [
            (car_position, car_speed)
            for (car_position, car_speed) in zip(position, speed)
        ]
        cars.sort(reverse=True)

        stack = []
        for car_position, car_speed in cars:
            time_to_target = (target - car_position) / car_speed
            if stack and time_to_target <= stack[-1]:
                continue
            stack.append(time_to_target)

        return len(stack)
