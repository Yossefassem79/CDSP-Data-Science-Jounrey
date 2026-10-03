import numpy as np

# ============================================================
# NUMPY CHALLENGES
# ============================================================


# ============================================================
# CHALLENGE 1 — Array Basics
# ============================================================

numbers = [10, 20, 30, 40, 50]

arr = np.array(numbers)

print("Challenge 1")
print("Array:", arr)
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Size:", arr.size)
print("Data type:", arr.dtype)

arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(arr_2d)
print("Shape:", arr_2d.shape)
print("Dimensions:", arr_2d.ndim)
print("Size:", arr_2d.size)
print("Data type:", arr_2d.dtype)


# ============================================================
# CHALLENGE 2 — Indexing and Slicing
# ============================================================

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("\nChallenge 2")
print("First:", arr[0])
print("Last:", arr[-1])
print("Third:", arr[2])
print("20 to 50:", arr[1:5])
print("First 4:", arr[:4])
print("Last 3:", arr[-3:])
print("Reverse:", arr[::-1])
print("Every 2:", arr[::2])

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nMatrix:")
print(matrix)
print("5:", matrix[1, 1])
print("9:", matrix[2, 2])
print("First row:", matrix[0, :])
print("Second column:", matrix[:, 1])
print("Top-left 2x2:")
print(matrix[:2, :2])


# ============================================================
# CHALLENGE 3 — Boolean Indexing
# ============================================================

arr = np.array([5, 12, 18, 23, 30, 7, 40, 15])

print("\nChallenge 3")
print("Greater than 20:", arr[arr > 20])
print("Even numbers:", arr[arr % 2 == 0])
print("Between 10 and 30:", arr[(arr >= 10) & (arr <= 30)])
print("Greater than 15 and less than 40:",
      arr[(arr > 15) & (arr < 40)])

mask = arr > 20
print("Mask:", mask)
print("Using mask:", arr[mask])


# ============================================================
# CHALLENGE 4 — Array Arithmetic / Vectorization
# ============================================================

arr = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])

print("\nChallenge 4")
print("arr + 5:", arr + 5)
print("arr * 2:", arr * 2)
print("arr / 10:", arr / 10)
print("arr ** 2:", arr ** 2)

print("arr + arr2:", arr + arr2)
print("arr * arr2:", arr * arr2)
print("arr - arr2:", arr - arr2)


# ============================================================
# CHALLENGE 5 — Broadcasting
# ============================================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

row = np.array([1, 2, 3])

column = np.array([
    [10],
    [20],
    [30]
])

print("\nChallenge 5")
print("Array + 5:")
print(arr + 5)

print("\nArray * 2:")
print(arr * 2)

print("\nArray + row:")
print(arr + row)

print("\nArray + column:")
print(arr + column)

mean = arr.mean()
centered = arr - mean

print("\nMean:", mean)
print("Mean-centered array:")
print(centered)


# ============================================================
# CHALLENGE 6 — Universal Functions (ufunc)
# ============================================================

arr = np.array([1, 4, 9, 16, 25])
negative_arr = np.array([-5, -10, 15, -20])
powers = np.array([1, 2, 3, 4, 5])
log_values = np.array([1, np.e, np.e**2, np.e**3])
exp_values = np.array([1, 2, 3, 4, 5])

print("\nChallenge 6")
print("Square root:", np.sqrt(arr))
print("Absolute:", np.abs(negative_arr))
print("Power:", np.power(powers, 2))
print("Log:", np.log(log_values))
print("Exponential:", np.exp(exp_values))


# ============================================================
# CHALLENGE 7 — Statistics
# ============================================================

scores = np.array([55, 70, 82, 90, 65, 75, 88, 95, 60, 78])

print("\nChallenge 7")
print("Sum:", np.sum(scores))
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Standard deviation:", np.std(scores))
print("Variance:", np.var(scores))
print("Maximum:", np.max(scores))
print("Minimum:", np.min(scores))

high_scores = scores[scores >= 80]

print("Scores >= 80:", high_scores)
print("Count >= 80:", high_scores.size)

manual_mean = np.sum(scores) / scores.size
print("Manual mean:", manual_mean)


# ============================================================
# CHALLENGE 8 — Linear Algebra
# ============================================================

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

vector_1 = np.array([3, 4])
vector_2 = np.array([1, 2, 3])
vector_3 = np.array([4, 5, 6])

print("\nChallenge 8")

print("A + B:")
print(A + B)

print("\nA - B:")
print(A - B)

print("\nElement-wise A * B:")
print(A * B)

print("\nTranspose of A:")
print(A.T)

print("\nMatrix multiplication using np.dot:")
print(np.dot(A, B))

print("\nMatrix multiplication using @:")
print(A @ B)

print("\nNorm of [3, 4]:")
print(np.linalg.norm(vector_1))

print("\nDot product:")
print(np.dot(vector_2, vector_3))

print("\nDeterminant of A:")
print(np.linalg.det(A))

print("\nInverse of A:")
print(np.linalg.inv(A))
