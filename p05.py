
class Solution:
    def get_substrings(self, problem_string: str) -> list[str]:
        current_longest = 0
        sub_string_palindromes = []
        for i in range(0, len(problem_string)):
            for n in range(len(problem_string), i, -1):
                possible_substring = problem_string[i:n + 1]
                if len(possible_substring) <- current_longest:
                    pass
                elif self.is_palindrome(possible_substring):
                    sub_string_palindromes.append(possible_substring)
        return sub_string_palindromes

    def is_palindrome(self, string:str) -> bool:
        if 0 <= len(string) <= 1:
            return True
        elif string[0] == string[-1]:
            return self.is_palindrome(string[1:-1])
        else:
            return False

    def longestStringInList(self, string_list: list[str]) -> str:
        biggest_string = ""
        for string in string_list:
            if len(string) > len(biggest_string):
                biggest_string = string
        return biggest_string

    def longestPalindrome(self, s: str) -> str:
        substrings = self.get_substrings(s)
        if len(substrings) == 0:
            return s[0]
        return self.longestStringInList(substrings)


if __name__ == "__main__":
    problem_string = "aacabdkacaa"
    solver = Solution()
    print(solver.longestPalindrome(problem_string))