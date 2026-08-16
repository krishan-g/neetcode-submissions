class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        fleets = len(position)

        # print(sorted_cars)

        curr_car = None
        curr_car_time = None

        for car in sorted_cars:
            if curr_car is None:
                curr_car = car
                curr_car_time = (target - car[0]) / car[1]
            else:
                time = (target - car[0]) / car[1]
                if time <= curr_car_time:
                    fleets -= 1
                else:
                    curr_car = car
                    curr_car_time = time

            # print(curr_car, curr_car_time, fleets)
        return fleets