class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        we need to attach all strings to single string but to separate the each string we need a delimeter.
        """
        final_str = ""
        for s in strs:
            s = s.replace("_", "__")
            final_str = final_str + " _ " + s 
        return final_str

    def decode(self, s: str) -> List[str]:

        decoded = []
        for i in s.split(" _ "):
            decoded.append(i.replace("__", "_"))
        return decoded[1:]
