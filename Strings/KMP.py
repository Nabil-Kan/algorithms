class KMP:
    def __init__(self):
        pass

    def compute_lps(self, pattern: str) -> list[int]:

        lps, left, right = [0] * len(pattern), 0, 1
        while right < len(pattern):

            if pattern[right] == pattern[left]:
                left += 1
                lps[right] = left
                right += 1
            else:
                if left == 0:
                    lps[right] = 0
                    right += 1
                else:
                    left = lps[left - 1]
            
        return lps
    

    # Search for pattern in text
    def search(self, text: str, pattern: str) -> int:
        m = len(text)
        n = len(pattern)

        lps, i, j = self.compute_lps(pattern), 0, 0 # i for text and j for patten

        while i < m:

            if text[i] == pattern[j]:
                i += 1
                j += 1
                if j == n:
                    return i - j # return the index of match if found
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]

        return -1
    
param1 = "abxabcabcaby"
param2 = "abcaby"

kmp = KMP()
print(kmp.search(param1, param2))