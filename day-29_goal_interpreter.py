"""
1678. Goal Parser Interpretation
Easy

You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

 

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"
 

Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.


Day: 29
Date: 12-02-2023 
Source: https://leetcode.com/problems/goal-parser-interpretation/description/

Time Complexity = n 
Space Complexity = 1
"""


class Solution:
    def interpret(self, command: str) -> str:
        ind = 0
        interpretedStr = ""
        for ch in command:
            if ch == "G":
                interpretedStr += "G"
            elif ch == "(" and command[ind+1] == ")":
                interpretedStr += "o"
            elif ch == "(" and command[ind+1] == "a" and command[ind+2] == "l" and command[ind+3] == ")":
                interpretedStr += "al"
            ind += 1

        return interpretedStr
        # pass


# s = Solution()
# print("Goal" == s.interpret("G()(al)"))
# print("Gooooal" == s.interpret("G()()()()(al)"))
# print("alGalooG" == s.interpret("(al)G(al)()()G"))


class Solution2:
    def interpret(self, command: str) -> str:
        ind = 0
        interpretedStr = ""
        for ch in command:
            if ch == "G":
                interpretedStr += "G"
            elif ch == "(":
                if command[ind+1] == ")":
                    interpretedStr += "o"
                elif command[ind+1:ind+4] == "al)":
                    interpretedStr += "al"
            ind += 1

        return interpretedStr


# s = Solution2()
# print(s.interpret("G()(al)"))
# print(s.interpret("G()()()()(al)"))
# print(s.interpret("(al)G(al)()()G"))

# Misleading Solution 
# bcz here modifiing the range variable i doesn't affect the loop iterations 
# still it wil iterate through 0 to len(command) 
class Solution3:
    def interpret(self, command: str) -> str:
        out = ''
        for i in range(0, len(command)):
            print(i)
            if command[i] == 'G':
                out = out+"G"
            if command[i] == '(':
                if command[i+1] == ')':
                    out = out+'o'
                    i = i+1
                if i < len(command)-1:
                    if command[i+1] == 'a':
                        out = out+'al'
                        i = i+3
        return out
# s = Solution3()
# print(s.interpret("G()(al)"))
# print(s.interpret("G()()()()(al)"))
# print(s.interpret("(al)G(al)()()G"))

# Best Solution with optimised loop iterations TC: O(N) SC: O(1)
class Solution4:
    def interpret(self, command: str) -> str:
        n = len(command)
        i = 0
        result = ""
        while i < n:
            if command[i] == "G":
                result += "G"
                i += 1
            else:
                if command[i+1] == ")":
                    result += "o"
                    i += 2
                else:
                    result += "al"
                    i += 4
        return result


s = Solution4()
print(s.interpret("G()(al)"))
print(s.interpret("G()()()()(al)"))
print(s.interpret("(al)G(al)()()G"))
