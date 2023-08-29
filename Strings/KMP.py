class KMP:
    # def __init__(self):

    def compute_lps(self, pattern: str) -> list[int]:

        lps, left, right = [0] * len(pattern), 0, 1

        while right < len(pattern):

            if pattern[right] == pattern[left]:
                left += 1
                lps[right] = left
                left += 1
            else:
                if left == 0:
                    lps[right] = 0
                    left += 1
                else:
                    lps[right] = lps[left - 1]
            
        return lps

    def search(self, text: str, pattern: str) -> str:
        
        print(self.compute_lps(pattern))

        return ""
    


kmp = KMP()
KMP.search("abxabcabcaby", "abcaby")