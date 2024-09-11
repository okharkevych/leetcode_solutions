import re
from collections import defaultdict, deque


class Solution:

    @staticmethod
    def parse_element(formula, i):
        match = re.match(r'([A-Z][a-z]*)(\d*)', formula[i:])
        element = match.group(1)
        i += len(element)
        return element, i

    @staticmethod
    def parse_multiplicity(formula, i):
        match = re.match(r'(\d+)', formula[i:])
        if match:
            multiplicity = int(match.group(1))
            i += len(match.group(1))
        else:
            multiplicity = 1
        return i, multiplicity

    def count_of_atoms(self, formula: str) -> str:
        stack = deque([defaultdict(int)])
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i, multiplicity = self.parse_multiplicity(formula, i)
                for element, count in top.items():
                    stack[-1][element] += count * multiplicity
            else:
                element, i = self.parse_element(formula, i)
                i, multiplicity = self.parse_multiplicity(formula, i)
                stack[-1][element] += multiplicity

        final_count = stack.pop()
        elements = sorted(final_count.keys())
        result = []
        for element in elements:
            result.append(element)
            if final_count[element] > 1:
                result.append(str(final_count[element]))
        return ''.join(result)


solution = Solution()
example_1 = solution.count_of_atoms(formula='H2O')
example_2 = solution.count_of_atoms(formula='Mg(OH)2')
example_3 = solution.count_of_atoms(formula='K4(ON(SO3)2)2')

print(f'Example 1 output (should be H2O): {example_1}')
print(f'Example 2 output (should be H2MgO2): {example_2}')
print(f'Example 3 output (should be K4N2O14S4): {example_3}')
