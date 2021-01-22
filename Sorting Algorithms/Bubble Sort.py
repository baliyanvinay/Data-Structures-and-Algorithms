# Bubble Sort
a = [5, 4, 6, 5, 3]

# Nested loops for Bubble sort
swap_rounds = 0
for _ in a:
    for j in range(len(a)-1):
        if (a[j] > a[j + 1]):
            a[j], a[j+1] = a[j+1], a[j]
            swap_rounds += 1
print(f"Array is sorted in {swap_rounds} swaps")
