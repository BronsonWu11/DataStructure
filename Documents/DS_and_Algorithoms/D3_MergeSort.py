def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    n = len(arr)
    left_arr = arr[0: n//2]
    right_arr = arr[n//2: n]
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    merged_arr = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            merged_arr.append(left_arr[i])
            i += 1
        else:
            merged_arr.append(right_arr[j])
            j += 1
    merged_arr.extend(left_arr[i:])
    merged_arr.extend(right_arr[j:])
    return merged_arr

def main():
    try:
        user_input = input("Input the original array, seperate with space")
        arr = list(map(int,user_input.split()))
        print("Original array:", arr)
        sorted_arr = merge_sort(arr)
        print("Sorted array:", sorted_arr)

    except ValueError as e:
        print("Input error")

if __name__ == "__main__":
    main()