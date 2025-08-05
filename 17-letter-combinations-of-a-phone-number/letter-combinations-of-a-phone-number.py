# Mapping digits to letters
mapping = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}

# Recursive function to generate combinations
def solve(s, idx, output, ans):
    if idx == len(s):
        ans.append(output)
        return

    digit = int(s[idx])
    letters = mapping[digit]

    for letter in letters:
        solve(s, idx + 1, output + letter, ans)

# Main class
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        ans = []
        solve(digits, 0, "", ans)
        return ans

# Test example
sol = Solution()
print(sol.letterCombinations("23"))
