class Solution:

    @staticmethod
    def average_waiting_time(customers: list[list[int]]) -> float:
        order_served_time: int = 0
        waiting_times: list[int] = []

        for customer in customers:
            arrival_time: int = customer[0]
            cooking_duration: int = customer[1]

            if order_served_time <= arrival_time:
                order_served_time = arrival_time + cooking_duration
            else:
                order_served_time += cooking_duration

            waiting_time: int = order_served_time - arrival_time
            waiting_times.append(waiting_time)

        average_waiting_time: float = sum(waiting_times) / len(waiting_times)

        return average_waiting_time


solution = Solution()
example_1 = solution.average_waiting_time(customers=[[1, 2], [2, 5], [4, 3]])
example_2 = solution.average_waiting_time(
    customers=[[5, 2], [5, 4], [10, 3], [20, 1]]
)

print(f'Example 1 output (should be 5.0): {example_1}')
print(f'Example 1 output (should be 3.25): {example_2}')
