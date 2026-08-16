class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        # if n == 1:
        #     return len(tasks)
        for x in tasks:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1

        print(dic)
        
        maxheap = list(dic.values())

        print(maxheap)



        heapq.heapify_max(maxheap)
        print(maxheap)
        time = 0
        slot_size = n
        q = deque()
        while maxheap or q:
            time += 1
            
            if not maxheap:
                time = q[0][1]
            else:
                cnt = heapq.heappop_max(maxheap)
                cnt -= 1

                if cnt:
                    q.append([cnt,time + slot_size])

            while q and q[0][1] == time:
                heapq.heappush_max(maxheap,q.popleft()[0])

        
        return time
