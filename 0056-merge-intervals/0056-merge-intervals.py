class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort()

        now = intervals[0]
        i = 1
        while i < len(intervals):
            if now[1] >= intervals[i][0]:
                now = [now[0], max(now[1], intervals[i][1])]
            else:
                answer.append(now)
                now = intervals[i]
            i += 1
        answer.append(now)
        
        return answer
        