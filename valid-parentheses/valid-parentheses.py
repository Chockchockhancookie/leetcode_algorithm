class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        
        data = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                data.append(i)

            else:
                if len(data) == 0:
                    return False
                tmp = data.pop()
                if i == ")":
                    if tmp != "(":
                        return False
                if i == "}":
                    if tmp != "{":
                        return False
                if i == "]":
                    if tmp != "[":
                        return False
        if len(data) != 0:
            return False
        
        return True