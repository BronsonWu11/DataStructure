def insertion_sort(arr):
    for i in range(1, len(arr)):  # 从第二个元素开始
        key = arr[i]  # 当前要插入的值
        j = i - 1
        # 找到插入位置并移动元素
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # 向后移动
            j -= 1
        arr[j + 1] = key  # 插入到正确位置
    return arr
            
def main():
    try:
        # Get array from user's input
        user_input  = input("Please enter array and seperate it with space")
        array = list(map(int, user_input.split()))
        print("The original Array:", array)
        sorted_array = insertion_sort(array)
        print("The sorted Array:", sorted_array)

    except ValueError as e:
        print("The input error")

if __name__ == "__main__":
    main()