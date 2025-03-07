import heapq

heap = []

heapq.heappush(heap,10)
heapq.heappush(heap,1)
heapq.heappush(heap,5)

print(heapq.heappop(heap))

print(heap)


nums = [2,3,5,1,54,23,132]
heapq.heapify(nums)
print(nums)

print(heapq.nlargest(3,nums))

print(heapq.nsmallest(3,nums))