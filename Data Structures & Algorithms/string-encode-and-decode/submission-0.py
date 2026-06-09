class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            # Format: [length of string] + [#] + [string itself]
            # Example: "neet" -> "4#neet"
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Find the delimiter to know where the length ends
            while s[j] != "#":
                j += 1
            
            # Get the length of the next string
            length = int(s[i:j])
            
            # Move the pointer to the start of the actual string
            i = j + 1
            # Extract the string based on the length we found
            res.append(s[i : i + length])
            
            # Move the pointer to the start of the next encoded segment
            i += length
            
        return res