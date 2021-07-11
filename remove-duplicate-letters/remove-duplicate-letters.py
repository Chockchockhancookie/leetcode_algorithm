class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        stack = []
        seen = set()
        
        for word in s:
            counter[word] -= 1
            if word in seen:
                continue
            
            while stack and word < stack[-1] and counter[stack[-1]] > 0:
                print(stack)
                print(word, stack[-1], word < stack[-1])
                seen.remove(stack.pop())
            stack.append(word)
            seen.add(word)
        
        return "".join(stack)