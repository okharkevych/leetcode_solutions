class Solution:

    @staticmethod
    def is_isomorphic(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping_s_to_t: dict[str, str] = {}
        mapping_t_to_s: dict[str, str] = {}

        for char_s, char_t in zip(s, t):
            if char_s in mapping_s_to_t:
                if mapping_s_to_t[char_s] != char_t:
                    return False
            else:
                mapping_s_to_t[char_s] = char_t

            if char_t in mapping_t_to_s:
                if mapping_t_to_s[char_t] != char_s:
                    return False
            else:
                mapping_t_to_s[char_t] = char_s

        return True


solution = Solution()
example_1 = solution.is_isomorphic(s='egg', t='add')
example_2 = solution.is_isomorphic(s='foo', t='bar')
example_3 = solution.is_isomorphic(s='paper', t='title')

print(f'Example 1 output (should be True): {example_1}')
print(f'Example 2 output (should be False): {example_2}')
print(f'Example 3 output (should be True): {example_3}')
