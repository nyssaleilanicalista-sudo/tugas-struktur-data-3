import random
import time

# ==========================================
# SOAL 1: Modified Binary Search
# ==========================================
def countOccurrences(sortedList, target):
    def find_left(arr, t):
        left, right = 0, len(arr) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == t:
                res = mid
                right = mid - 1  # Cari ke kiri untuk batas paling kiri
            elif arr[mid] < t:
                left = mid + 1
            else:
                right = mid - 1
        return res

    def find_right(arr, t):
        left, right = 0, len(arr) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == t:
                res = mid
                left = mid + 1   # Cari ke kanan untuk batas paling kanan
            elif arr[mid] < t:
                left = mid + 1
            else:
                right = mid - 1
        return res

    left_idx = find_left(sortedList, target)
    if left_idx == -1:
        return 0
    
    right_idx = find_right(sortedList, target)
    return right_idx - left_idx + 1

# ==========================================
# SOAL 2: Bubble Sort dengan Analisis Langkah
# ==========================================
def bubbleSort(arr):
    n = len(arr)
    total_comparisons = 0
    total_swaps = 0
    passes_used = 0
    arr_copy = arr[:] # Copy agar list asli tidak berubah
    
    for i in range(n):
        swapped = False
        passes_used += 1
        for j in range(0, n - i - 1):
            total_comparisons += 1
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                total_swaps += 1
                swapped = True
        
        # Cetak state array setelah setiap pass
        print(f"Pass {passes_used}: {arr_copy}")
        
        # Early termination
        if not swapped:
            break
            
    return (arr_copy, total_comparisons, total_swaps, passes_used)

# ==========================================
# SOAL 3: Hybrid Sort
# ==========================================
def insertion_sort_count(arr):
    comps = 0
    swaps = 0
    n = len(arr)
    arr_copy = arr[:]
    for i in range(1, n):
        key = arr_copy[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if arr_copy[j] > key:
                arr_copy[j + 1] = arr_copy[j]
                swaps += 1
                j -= 1
            else:
                break # Optimization: stop if already sorted
        arr_copy[j + 1] = key
    return arr_copy, comps, swaps

def selection_sort_count(arr):
    comps = 0
    swaps = 0
    n = len(arr)
    arr_copy = arr[:]
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comps += 1
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        if min_idx != i:
            arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
            swaps += 1
    return arr_copy, comps, swaps

def hybridSort(theSeq, threshold=10):
    # Sesuai soal: Insertion jika < threshold, Selection jika >= threshold
    if len(theSeq) < threshold:
        sorted_arr, c, s = insertion_sort_count(theSeq)
        return sorted_arr, c, s, "Insertion"
    else:
        sorted_arr, c, s = selection_sort_count(theSeq)
        return sorted_arr, c, s, "Selection"

# ==========================================
# SOAL 4: Merge Tiga Sorted Lists
# ==========================================
def mergeThreeSortedLists(listA, listB, listC):
    i, j, k = 0, 0, 0
    result = []
    
    # Kita gunakan infinity sebagai sentinel jika list sudah habis
    while i < len(listA) or j < len(listB) or k < len(listC):
        valA = listA[i] if i < len(listA) else float('inf')
        valB = listB[j] if j < len(listB) else float('inf')
        valC = listC[k] if k < len(listC) else float('inf')
        
        if valA <= valB and valA <= valC:
            result.append(valA)
            i += 1
        elif valB <= valA and valB <= valC:
            result.append(valB)
            j += 1
        else:
            result.append(valC)
            k += 1
            
    return result

# ==========================================
# SOAL 5: Inversions Counter
# ==========================================
def countInversionsNaive(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count

def countInversionsSmart(arr):
    # Helper function untuk merge sort
    def merge_sort_count(arr):
        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr) // 2
        left, inv_left = merge_sort_count(arr[:mid])
        right, inv_right = merge_sort_count(arr[mid:])
        
        merged = []
        i = j = 0
        inv_split = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                # Jika left[i] > right[j], maka semua elemen sisa di left
                # juga lebih besar dari right[j] (karena left sudah sorted)
                merged.append(right[j])
                j += 1
                inv_split += (len(left) - i)
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged, inv_left + inv_right + inv_split

    _, total_inv = merge_sort_count(arr)
    return total_inv

# ==========================================
# MAIN EXECUTION & TESTING
# ==========================================
if __name__ == "__main__":
    print("="*50)
    print("SOAL 1: Modified Binary Search")
    print("="*50)
    list1 = [1, 2, 4, 4, 4, 4, 7, 9, 12]
    print(f"List: {list1}")
    print(f"Count(4): {countOccurrences(list1, 4)}") # Expected: 4
    print(f"Count(5): {countOccurrences(list1, 5)}") # Expected: 0
    print()

    print("="*50)
    print("SOAL 2: Bubble Sort Analysis")
    print("="*50)
    input1 = [5, 1, 4, 2, 8]
    print(f"Input: {input1}")
    res1 = bubbleSort(input1)
    print(f"Result: {res1[0]}, Comparisons: {res1[1]}, Swaps: {res1[2]}, Passes: {res1[3]}")
    print("-" * 20)
    input2 = [1, 2, 3, 4, 5]
    print(f"Input: {input2}")
    res2 = bubbleSort(input2)
    print(f"Result: {res2[0]}, Comparisons: {res2[1]}, Swaps: {res2[2]}, Passes: {res2[3]}")
    print("Penjelasan: Input kedua sudah terurut, sehingga early termination aktif hanya dalam 1 pass.")
    print()

    print("="*50)
    print("SOAL 3: Hybrid Sort Comparison")
    print("="*50)
    sizes = [50, 100, 500]
    print(f"{'Size':<10} | {'Algo':<15} | {'Ops (Comp+Swap)':<20}")
    print("-" * 50)
    
    for size in sizes:
        random_list = [random.randint(1, 1000) for _ in range(size)]
        
        # Pure Insertion
        _, c_i, s_i = insertion_sort_count(random_list)
        print(f"{size:<10} | {'Pure Insertion':<15} | {c_i + s_i:<20}")
        
        # Pure Selection
        _, c_s, s_s = selection_sort_count(random_list)
        print(f"{size:<10} | {'Pure Selection':<15} | {c_s + s_s:<20}")
        
        # Hybrid (Threshold 10)
        _, c_h, s_h, used = hybridSort(random_list, threshold=10)
        print(f"{size:<10} | {'Hybrid ('+used+')':<15} | {c_h + s_h:<20}")
        print("-" * 50)
    print()

    print("="*50)
    print("SOAL 4: Merge Tiga Sorted Lists")
    print("="*50)
    lA = [1, 5, 9]
    lB = [2, 6, 10]
    lC = [3, 4, 7]
    print(f"List A: {lA}")
    print(f"List B: {lB}")
    print(f"List C: {lC}")
    print(f"Merged: {mergeThreeSortedLists(lA, lB, lC)}")
    print()

    print("="*50)
    print("SOAL 5: Inversions Counter")
    print("="*50)
    test_arr = [8, 4, 2, 1]
    print(f"Array: {test_arr}")
    print(f"Naive Count: {countInversionsNaive(test_arr)}")
    print(f"Smart Count: {countInversionsSmart(test_arr)}")
    
    print("\nPerformance Test (Time):")
    for size in [1000, 5000, 10000]:
        rand_arr = [random.randint(1, 100000) for _ in range(size)]
        
        # Naive (Hanya untuk ukuran kecil agar tidak terlalu lama, skip 10000)
        if size <= 5000:
            start = time.time()
            countInversionsNaive(rand_arr[:2000]) # Batasi naive agar tidak hang
            time_naive = time.time() - start
        else:
            time_naive = "Skipped (Too Slow)"

        start = time.time()
        countInversionsSmart(rand_arr)
        time_smart = time.time() - start
        
        print(f"Size {size}: Naive={time_naive}, Smart (Merge)={time_smart:.5f}s")
    
    print("\nPenjelasan: Merge Sort lebih cepat karena kompleksitasnya O(n log n), sedangkan Naive O(n^2).")
