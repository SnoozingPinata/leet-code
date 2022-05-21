
# Runtime: 87 ms, faster than 57.04% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 18.9 MB, less than 5.59% of Python3 online submissions for Longest Substring Without Repeating Characters.
class Solution:
    def __init__(self):
        pass

    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = self.findSubstrings(s)
        longest_string = self.longestStringInList(substrings)
        return len(longest_string)

    def findSubstrings(self, s):
        substrings = []
        used_letters = ""
        for letter in s:
            if letter in used_letters:
                substrings.append(used_letters)
                breakpoint = used_letters.index(letter)
                used_letters = used_letters[breakpoint + 1:]
            used_letters += letter
        if len(used_letters) > 0:
            substrings.append(used_letters)
        return substrings
    
    def longestStringInList(self, string_list):
        biggest_string = ""
        for string in string_list:
            if len(string) > len(biggest_string):
                biggest_string = string
        return biggest_string


if __name__ == '__main__':
    problem = "ab"
    solver = Solution()
    print(solver.lengthOfLongestSubstring(problem))