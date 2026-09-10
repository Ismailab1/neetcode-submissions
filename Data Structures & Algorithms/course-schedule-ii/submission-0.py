class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseList = {i:[] for i in range(numCourses)}

        for crs, prereq in prerequisites:
            courseList[crs].append(prereq)
        
        classesToTake = []
        visit, cycle = set(), set()

        def dfs(clss):
            if clss in cycle:
                return False
            if clss in visit:
                return True
            
            cycle.add(clss)
            for pre in courseList[clss]:
                if dfs(pre) == False:
                    return False
            cycle.remove(clss)
            visit.add(clss)
            classesToTake.append(clss)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return classesToTake
