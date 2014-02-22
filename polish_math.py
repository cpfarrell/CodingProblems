class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        #ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
        if len(tokens)<0:
            return 0
        value = int(tokens[0])
        nums = []
        for token in tokens:
            try:
                token = int(token)
                nums.append(token)
            except:
                right = nums.pop()
                left = nums.pop()
                if token=="+":
                    value = left + right
                if token=="-":
                    value = left - right
                if token=="*":
                    value = left * right
                if token=="/":
                    value = left // right
                    if (bool(left<0) != bool(right<0)) and left%right!=0:
                        value -= 1
                nums.append(value)
        return value

sol = Solution()
print sol.evalRPN(["10","6","9","3","+","-11","*","/","*"])
print sol.evalRPN(["6","9","3","+","-11","*","/"])
print sol.evalRPN(["9","3","+","-11","*"])
