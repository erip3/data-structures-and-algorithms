class Sort:

    @staticmethod
    def merge_sort(arr):
        if len(arr) <= 1: return arr

        midpoint = len(arr) // 2
        left = Sort.merge_sort(arr[:midpoint])
        right = Sort.merge_sort(arr[midpoint:])

        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result
