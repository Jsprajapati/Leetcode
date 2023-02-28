

from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        wordList = 0
        for _sent in sentences:
            words = _sent.split(" ")
            if wordList == 0 or wordList < len(words):
                wordList = len(words)

        return wordList
            


s = Solution()
print(s.mostWordsFound(["alice and bob love leetcode","i think so too","this is great thanks very much"]))
print(s.mostWordsFound(["please wait","continue to fight","continue to win"]))
print(s.mostWordsFound(["please continue to fight wait continue to fight","continue to so tooso too fight","so too continue to win"]))