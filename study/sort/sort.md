# 排序算法

## 冒泡排序

### 一般冒泡排序

最好、最坏、平均时间复杂度都为O(n^2)

```python
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

### 冒泡排序优化1

在排序过程中增加一个标志位记录有没有交换过位置，如果这一趟没有交换位置，则代表这组数据已经有序，后面的遍历不需要再进行下去

例如[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，第一趟遍历发现没有交换位置，则直接结束

例如[1, 2, 3, 4, 5, 6, 7, 8, 10, 9]，第一趟交换位置后已经有序，第二趟发现不交换位置，则结束

最好时间复杂度提升到O(n)，最好、最坏、平均时间复杂度分别为O(n)，O(n^2)，O(n^2)

```python
def bubble_sort2(arr):
    for i in range(len(arr) - 1):
        flag = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1
        if not flag:
            break
    return arr
```

### 冒泡排序优化2

优化1对于后面大部分有序前面小部分无序的情况，排序效率并不乐观

例如[2, 3, 1, 4, 5, 6, 7, 8, 9, 10]，第一趟之后为[2, 1, 3, 4, 5, 6, 7, 8, 9, 10]，第二趟又要遍历所有数据，但其实后面的大部分数据已经有序的了

优化2会记录最后一次交换的位置，后面没有交换过的必然是有序的，从下一趟开始从第一个比较到上一趟记录的位置结束即可

最好、最坏、平均时间复杂度分别为O(n)，O(n^2)，O(n^2)

```python
def bubble_sort3(arr):
    i = len(arr) - 1
    while i:
        pos = 0
        for j in range(i):
            if arr[j] > arr[j + 1]:
                pos = j
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        i = pos
    return arr
```

### 鸡尾酒排序

鸡尾酒排序是一种双向的冒泡排序，不进行优化的算法效率较差

最好、最坏、平均时间复杂度都为O(n^2)

```python
def cocktail_sort(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        for i in range(low, high):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        high -= 1
        for i in range(high, low, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        low += 1
    return arr
```

### 鸡尾酒排序优化1

对于前面大部分有序，效率较高，例如[2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

最好、最坏、平均时间复杂度分别为O(n)，O(n^2)，O(n^2)

```python
def cocktail_sort1(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        for i in range(low, high):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        high -= 1
        flag = 0
        for i in range(high, low, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                flag = 1
        low += 1
        if not flag:
            break
    return arr
```

### 鸡尾酒排序优化2

具有冒泡排序优化2和鸡尾酒排序优化1的优点

最好、最坏、平均时间复杂度分别为O(n)，O(n^2)，O(n^2)

```python
def cocktail_sort2(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        pos = low
        for i in range(low, high):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                pos = i
        high = pos
        pos = high
        for i in range(high, low, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                pos = i
        low = pos
    return arr
```

