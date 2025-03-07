import heapq

nums = [25,12,6,8,14,16]

heapq._heapify_max(nums) #listeyi ters çevirmeden ya da negatifini almadan max heap'e çevirme
print(nums)

largest_three = [heapq._heappop_max(nums) for _ in range(3)]

print("En büyük üç eleman:", largest_three)