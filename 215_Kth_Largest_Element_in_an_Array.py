class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []

        for x in nums:
            heappush(heap, x)
            if len(heap) > k:
                heappop(heap)

        return heap[0]
        
