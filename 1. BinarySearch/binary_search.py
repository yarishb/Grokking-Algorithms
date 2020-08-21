def binary_search(arr, num):
     start = 0
     end = len(arr) -1

     while start <= end:
          mid = (start + end) // 2
          guess = arr[mid]

          if guess == num:
               return mid
          if guess > num:
               end = mid - 1
          else:
               start = mid + 1
          
     return None

list = [1, 3, 5, 7, 8, 9]

print (binary_search(list, 8))
print (binary_search(list, -1))