class Solution(object):
    def wordPattern(self, pattern, s):
        t = s.split()
        return [map(pattern.index, pattern)] == [map(t.index, t)]
