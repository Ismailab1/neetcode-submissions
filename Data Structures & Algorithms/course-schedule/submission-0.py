class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prevMap[course].append(prereq)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            
            if prevMap[course] == []:
                return True

            visiting.add(course)
            for pre in prevMap[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            prevMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                    return False
        return True