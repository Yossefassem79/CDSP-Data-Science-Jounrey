import numpy as np

# ============================================================
# NUMPY MINI PROJECT — STUDENT PERFORMANCE ANALYSIS
# ============================================================
# Dataset columns:
# Python, SQL, Statistics, ML
#
# Goal:
# Analyze student performance using NumPy only.
# No Pandas.
# No loops.
# ============================================================


# ============================================================
# DATASET
# ============================================================

students = np.array([
    [85, 78, 92, 88],
    [70, 65, 75, 80],
    [95, 90, 93, 96],
    [60, 72, 68, 70],
    [88, 85, 90, 87],
    [76, 80, 79, 82],
    [45, 55, 50, 48],
    [91, 89, 94, 92],
    [67, 73, 70, 75],
    [82, 77, 85, 80]
])

subjects = np.array(["Python", "SQL", "Statistics", "ML"])


# ============================================================
# PART 1 — BASIC DATASET INFORMATION
# ============================================================

print("=" * 60)
print("PART 1 — BASIC DATASET INFORMATION")
print("=" * 60)

print("Dataset:")
print(students)

print("\nShape:", students.shape)
print("Number of students:", students.shape[0])
print("Number of subjects:", students.shape[1])
print("Total elements:", students.size)


# ============================================================
# PART 2 — SUBJECT STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("PART 2 — SUBJECT STATISTICS")
print("=" * 60)

subject_means = np.mean(students, axis=0)
subject_max = np.max(students, axis=0)
subject_min = np.min(students, axis=0)
subject_std = np.std(students, axis=0)

print("Subject means:", subject_means)
print("Subject maximums:", subject_max)
print("Subject minimums:", subject_min)
print("Subject standard deviations:", subject_std)


# ============================================================
# PART 3 — STUDENT PERFORMANCE
# ============================================================

print("\n" + "=" * 60)
print("PART 3 — STUDENT PERFORMANCE")
print("=" * 60)

student_averages = np.mean(students, axis=1)

print("Student averages:")
print(student_averages)

top_student_index = np.argmax(student_averages)
lowest_student_index = np.argmin(student_averages)

print("\nTop student index:", top_student_index)
print("Top student average:", student_averages[top_student_index])

print("\nLowest student index:", lowest_student_index)
print("Lowest student average:", student_averages[lowest_student_index])


# ============================================================
# PART 4 — STUDENTS WITH AVERAGE >= 80
# ============================================================

print("\n" + "=" * 60)
print("PART 4 — HIGH PERFORMING STUDENTS")
print("=" * 60)

high_performers = student_averages >= 80

print("Boolean mask:")
print(high_performers)

print("\nAverages >= 80:")
print(student_averages[high_performers])

number_of_high_performers = np.sum(high_performers)

print("Number of students with average >= 80:",
      number_of_high_performers)


# ============================================================
# PART 5 — BEST AND WORST SUBJECT
# ============================================================

print("\n" + "=" * 60)
print("PART 5 — BEST AND WORST SUBJECT")
print("=" * 60)

best_subject_index = np.argmax(subject_means)
worst_subject_index = np.argmin(subject_means)

best_subject = subjects[best_subject_index]
worst_subject = subjects[worst_subject_index]

print("Best subject:", best_subject)
print("Best subject average:", subject_means[best_subject_index])

print("\nWorst subject:", worst_subject)
print("Worst subject average:", subject_means[worst_subject_index])


# ============================================================
# PART 6 — MIN-MAX NORMALIZATION
# ============================================================

print("\n" + "=" * 60)
print("PART 6 — MIN-MAX NORMALIZATION")
print("=" * 60)

X_min = np.min(students)
X_max = np.max(students)

X_normalized = (students - X_min) / (X_max - X_min)

print("Original minimum:", X_min)
print("Original maximum:", X_max)

print("\nNormalized dataset:")
print(X_normalized)

print("\nNormalized minimum:", np.min(X_normalized))
print("Normalized maximum:", np.max(X_normalized))
print("Normalized shape:", X_normalized.shape)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("FINAL SUMMARY")
print("=" * 60)

print("1. Highest average subject:", best_subject)
print("2. Lowest average subject:", worst_subject)
print("3. Top student index:", top_student_index)
print("4. Students with average >= 80:", number_of_high_performers)
print("5. Normalized dataset shape:", X_normalized.shape)


# ============================================================
# EXTRA CHALLENGE
# ============================================================

print("\n" + "=" * 60)
print("EXTRA CHALLENGE")
print("=" * 60)

# 1. Students with Python >= 80 AND SQL >= 80
python_sql_high = students[
    (students[:, 0] >= 80) &
    (students[:, 1] >= 80)
]

print("Students with Python >= 80 AND SQL >= 80:")
print(python_sql_high)


# 2. Students with at least one score < 60
students_with_low_score = students[
    np.any(students < 60, axis=1)
]

print("\nStudents with at least one score < 60:")
print(students_with_low_score)


# 3. Overall average of the entire dataset
overall_average = np.mean(students)

print("\nOverall average:", overall_average)


# 4. Student with highest ML score
highest_ml_index = np.argmax(students[:, 3])

print("\nStudent with highest ML score index:", highest_ml_index)
print("Highest ML score:", students[highest_ml_index, 3])


# 5. Python >= 80 AND Statistics >= 80
python_statistics_mask = (
    (students[:, 0] >= 80) &
    (students[:, 2] >= 80)
)

print("\nPython >= 80 AND Statistics >= 80:")
print(python_statistics_mask)

print("\nMatching students:")
print(students[python_statistics_mask])
