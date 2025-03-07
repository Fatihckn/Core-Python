import heapq

nums = [25,12,6,8,14,16]

max_heap = [-num for num in nums] # Bu modül varsayılan olarak min-heap yapısını desteklediği için maks heap yapısına çevirirken elemanların negatifini alıyoruz
print(max_heap)

heapq.heapify(max_heap) # Verilen bir iterable nesneyi (genellikle bir liste) bir min-heap yapısına dönüştürür
print(max_heap)

largest_three = [-heapq.heappop(max_heap) for _ in range(3)]
print("En büyük üç eleman:",largest_three)