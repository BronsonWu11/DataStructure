def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j- gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def main():
    try:
        user_input = input("Input the original array, seperate with space")
        arr = list(map(int,user_input.split()))
        print("Original array:", arr)
        sorted_arr = shell_sort(arr)
        print("Sorted array:", sorted_arr)

    except ValueError as e:
        print("Input error")

if __name__ == "__main__":
    main()