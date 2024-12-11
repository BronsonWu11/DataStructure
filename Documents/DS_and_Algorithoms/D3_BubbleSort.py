def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swap = False
        for i in range(0, n - i - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
        if not swap:
            break
    return arr

def main():
    try:
        user_input = input("Input the original array, seperate with space")
        arr = list(map(int,user_input.split()))
        print("Original array:", arr)
        sorted_arr = bubble_sort(arr)
        print("Sorted array:", sorted_arr)

    except ValueError as e:
        print("Input error")

if __name__ == "__main__":
    main()