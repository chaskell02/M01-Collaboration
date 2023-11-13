def sort012(arr, N):
  low, mid, high = 0, 0, N - 1

  while mid <= high:
      if arr[mid] == 0:
          arr[low], arr[mid] = arr[mid], arr[low]
          low += 1
          mid += 1
      elif arr[mid] == 1:
          mid += 1
      else:
          arr[mid], arr[high] = arr[high], arr[mid]
          high -= 1

# Example usage:
arr = [0, 1, 0]
N = len(arr)

sort012(arr, N)

print(arr)
