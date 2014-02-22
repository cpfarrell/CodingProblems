class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    seen = set()

    def match(self, s, p, start_s, start_p):
        if not s:
            return False
        if (start_s, start_p) in self.seen:
            return False

        if s[start_s:]==p[start_p:]:
            return True

        for i in xrange(start_s, len(s)):
            k = i + start_p - start_s
            if k >= len(p):
                self.seen.add((start_s, start_p))
                return False

            if p[k]=="?" or p[k]==s[i]:
                return self.match(s, p, i+1, k+1)
            elif p[k]=="*":
                if k==(len(p)-1):
                    return True
                for j in xrange(i+1, len(s)):
                    if p[k]==s[j] and self.match(s,p, j+1, k+1):
                        return True
            else:
                self.seen.add((start_s, start_p))
                return False
        self.seen.add((start_s, start_p))
        return False

    def isMatch(self, s, p):
        return self.match(s, p, 0, 0)
            
            
            
s = Solution()
print s.isMatch("aa", "a*")
