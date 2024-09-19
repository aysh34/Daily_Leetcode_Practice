import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for i in nums:
            map[i] = map.get(i, 0) + 1

        minHeap = []

        for num, freq in map.items():
            heapq.heappush(minHeap, (freq, num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)  # Remove the element with the smallest frequency
        
        res = []
        for freq, num in minHeap:
            res.append(num)

        return res   # TC : o(n log k)

        # for i in nums:
        #     map[i] = map.get(i, 0) + 1

        # #  sorting dictionary keys by values
        # sortedKeysList = sorted(map.keys(), key = lambda x: map[x], reverse=True) # descending order

        # return sortedKeysList[:k] # TC : o(n log n)
