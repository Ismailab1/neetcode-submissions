class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseList = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            courseList[course].append(prereq)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            
            if courseList[crs] == []:
                return True
            
            visiting.add(crs)

            for pre in courseList[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            courseList[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True




