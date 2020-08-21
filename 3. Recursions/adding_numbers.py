def sum(arr):
     if len(arr) == 0:
          return 0
     else:
          return arr[0] + sum(arr[1:])
     
     
print(sum([1,2,3,1]))