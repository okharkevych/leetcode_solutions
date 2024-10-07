from collections import deque


class Solution:

    def predict_party_victory(self, senate: str) -> str:
        radiant_queue = deque()
        dire_queue = deque()

        for i, s in enumerate(senate):
            if s == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        while radiant_queue and dire_queue:
            radiant_index = radiant_queue.popleft()
            dire_index = dire_queue.popleft()

            if radiant_index < dire_index:
                radiant_queue.append(radiant_index + len(senate))
            else:
                dire_queue.append(dire_index + len(senate))

        return 'Radiant' if radiant_queue else 'Dire'


solution = Solution()
example_1 = solution.predict_party_victory(senate='RD')
example_2 = solution.predict_party_victory(senate='RDD')

print(f'Example 1 output (should be "Radiant"): {example_1}')
print(f'Example 2 output (should be "Dire"): {example_2}')
