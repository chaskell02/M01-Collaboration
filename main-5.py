def binarysearch(arr, N, K):
  low, high = 0, N - 1

  while low <= high:
      mid = (low + high) // 2

      if arr[mid] == K:
          return mid  # Element found, return its index
      elif arr[mid] < K:
          low = mid + 1  # Search in the right half
      else:
          high = mid - 1  # Search in the left half

  return -1  # Element not found

# Example usage:
arr1 = [1, 2, 3, 4, 5]
N1 = len(arr1)
K1 = 4
print(binarysearch(arr1, N1, K1))  # Output: 3

arr2 = [11, 22, 33, 44, 55]
N2 = len(arr2)
K2 = 445
print(binarysearch(arr2, N2, K2))  # Output: -1

