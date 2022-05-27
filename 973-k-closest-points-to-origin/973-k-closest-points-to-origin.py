class Solution:
    def Euclidean(self, points: List[int]):
        x, y = points
        return (x**2 + y**2)**0.5
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        sortedLists = []
        
        for point in points:
            heapq.heappush(sortedLists, (self.Euclidean(point), point[0], point[1]))
        
        # print(sortedLists)
        
#         minNum = float('inf') 
#         while sortedLists:
#             if minNum < sortedLists[0][0]:
#                 break
                
#             tmp = heapq.heappop(sortedLists)
#             result.append(tmp[1])
#             minNum = tmp[0]
            
        for _ in range(k):
            _, x, y = heapq.heappop(sortedLists)
            result.append([x,y])
            
        return result