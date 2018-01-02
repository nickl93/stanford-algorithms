def merge_sort(unsorted):
    output = []
    # Base Case
    if len(unsorted) <= 1:
        return unsorted
    # Recursive Case
    left = merge_sort(unsorted[0:len(unsorted)//2])
    right = merge_sort(unsorted[len(unsorted)//2:])
    return merge(left, right)

def merge(left, right): 
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(right) == 0:
            result.append(left[0])
            left = left[1:]
        elif len(left) == 0:
            result.append(right[0])
            right = right[1:]
        elif left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
        print("result "+str(result))
    return result

unsorted_array = [12, 15, 25, 1, 2, 5, 8, 11]
out = merge_sort(unsorted_array)
print(out)
