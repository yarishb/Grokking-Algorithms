def biggest_num(arr):
     num = 0
     
     if not arr:
          return 0
     else:
          m = biggest_num(arr[1:])
          return m if m > arr[0] else arr[0]
     return num

print(biggest_num([1,2,3,4,12,54]))