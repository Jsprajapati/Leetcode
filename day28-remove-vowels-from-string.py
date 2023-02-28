"""
1119. Remove Vowels from a String
Level: Easy

Description: Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

Example 1
Input: “leetcodeisacommunityforcoders”
Output: “ltcdscmmntyfrcdrs”

Example 2:
Input: “aeiou”
Output: “”

Note:
S consists of lowercase English letters only.
1 <= S.length <= 1000

Day: 28
Date: 11-02-2023 
Source: https://leetcode.ca/2018-12-23-1119-Remove-Vowels-from-a-String

Time Complexity = 5 * ( (n * x) + n ) => O(n*x)
Space Complexity = 5 + n
"""
# size of str = n
# size of vowelMatchCount = x


class Solution():
    def removeVowelsFromString(self, str):
        vowels = 'leetcodecoder'  # 1

        for vowel in vowels:  # 5
            vowelMatchCount = self.countChars(str, vowel)  # n
            if vowelMatchCount == 0:  # 1
                continue  # 1
            while vowelMatchCount > 0:  # x
                vowelIndex = self.indexOf(str, vowel)  # n
                if vowelIndex != -1:  # 1
                    str = str[:vowelIndex]+str[vowelIndex+1:]  # 1
                vowelMatchCount -= 1  # 1
        return str

    def countChars(self, str, char):
        charCount = 0
        for index in range(0, len(str)):
            if str[index] == char:
                charCount += 1
        return charCount

    def indexOf(self, str, char):
        for index in range(0, len(str)):
            if str[index] == char:
                return index
        return -1

        # if v in s:
s = Solution()
str1 = "aeiou"
str2 = "leetcodeisacommunityforcoders"
# Output: “ltcdscmmntyfrcdrs”
output = s.removeVowelsFromString(str2)
print(output)


class OptimisedSolution():
    """
    Time: O(N)
    Space: O(1) extra space
    """
    def removeVowelsFromString(self, str):
        strWithoutVowels = "" # 1 1
        for char in str: # n n
            if not self.isVowel(char): # 1
                strWithoutVowels += char # 1
        return strWithoutVowels

    def isVowel(self, char):
        vowels = "aeiou"
        if char in vowels: # 1
            return True # 1
        return False # 1

optS = OptimisedSolution()
str1 = "aeiou"
str2 = "leetcodeisacommunityforcoders"
print(optS.removeVowelsFromString(str1))
print(optS.removeVowelsFromString(str2))