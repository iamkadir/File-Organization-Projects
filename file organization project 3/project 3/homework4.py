import random
import time

# Dosyaya rastgele sayılar yazan fonksiyon
def dosyadan_rastgele_sayı_yazma(file_name, num_count):
    with open(file_name, 'w') as file:
        for _ in range(num_count):
            file.write(str(random.randint(1, 1000)) + '\n')

# Dosyadan sayıları okuyan fonksiyon
def dosyadan_numara_okuma(file_name):
    numbers = []
    with open(file_name, 'r') as file:
        for line in file:
            numbers.append(int(line))
    return numbers

# Selection Sort algoritması
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Insertion Sort algoritması
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort algoritması
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def main():
    file_name = "numbers.txt"
    num_count = 1000

    # Dosyaya rastgele sayılar yaz
    dosyadan_rastgele_sayı_yazma(file_name, num_count)

    # Dosyadan sayıları oku
    numbers = dosyadan_numara_okuma(file_name)

    # Selection Sort için sıralama süresi
    selection_start_time = time.time()
    selection_sort(numbers.copy())
    selection_end_time = time.time()
    selection_time = selection_end_time - selection_start_time

    # Insertion Sort için sıralama süresi
    insertion_start_time = time.time()
    insertion_sort(numbers.copy())
    insertion_end_time = time.time()
    insertion_time = insertion_end_time - insertion_start_time

    # Merge Sort için sıralama süresi
    merge_start_time = time.time()
    merge_sort(numbers.copy())
    merge_end_time = time.time()
    merge_time = merge_end_time - merge_start_time

    print("Selection Sort süresi:", selection_time)
    print("Insertion Sort süresi:", insertion_time)
    print("Merge Sort süresi:", merge_time)

if __name__ == "__main__":
    main()
