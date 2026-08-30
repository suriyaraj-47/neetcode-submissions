class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find '#'
            while s[j] != '#':
                j += 1

            # Get length
            length = int(s[i:j])

            # Move after '#'
            i = j + 1

            # Extract the string
            word = s[i:i + length]
            result.append(word)

            # Move to next encoded string
            i = i + length

        return result