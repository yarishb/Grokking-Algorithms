def elements_counter(arr):
     if not arr:
          return 0
     else:
      return 1 + elements_counter(arr[1:])

print(elements_counter([1,2,3,4,5]))
