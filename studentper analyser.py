
import matplotlib.pyplot as plt

students = ["koushik", "Bhargav", "SHIVA"]

maths = [85, 99, 99]
science = [90, 99, 100]
english = [80, 79, 45]

print("\nDATA VALIDATION")
print("-" * 40)
valid_data = True

for i in range(len(students)):
    if maths[i] < 0 or maths[i] > 100:
        print("Invalid Maths marks for", students[i])
        valid_data = False

    if science[i] < 0 or science[i] > 100:
        print("Invalid Science marks for", students[i])
        valid_data = False

    if english[i] < 0 or english[i] > 100:
        print("Invalid English marks for", students[i])
        valid_data = False

if valid_data:
    print("All student marks are valid!")
else:
    print("Please correct the invalid marks.")


totals = []
averages = []

print("=" * 40)
print("   STUDENT PERFORMANCE DATA ANALYZER")
print("=" * 40)

highest_total = 0
topper = ""

for i in range(len(students)):
    total = maths[i] + science[i] + english[i]
    average = total / 3

    totals.append(total)
    averages.append(average)

    if maths[i] >= 35 and science[i] >= 35 and english[i] >= 35:
        result = "PASS"
    else:
        result = "FAIL"

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Student:", students[i])
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Result:", result)
    print("Grade:", grade)
    print("--------------------------")

    if total > highest_total:
        highest_total = total
        topper = students[i]

print("TOPPER:", topper)
print("Highest Total:", highest_total)

print("\nSUBJECT-WISE ANALYSIS")
print("--------------------------")

subject_averages = [
    sum(maths) / len(maths),
    sum(science) / len(science),
    sum(english) / len(english)
]

subjects = ["Maths", "Science", "English"]

for i in range(len(subjects)):
    print(subjects[i], "Average:", round(subject_averages[i], 2))

best_subject = subjects[subject_averages.index(max(subject_averages))]
print("Best Performing Subject:", best_subject)

print("\nCLASS PERFORMANCE SUMMARY")
print("--------------------------")

passed = 0
failed = 0

for i in range(len(students)):
    if maths[i] >= 35 and science[i] >= 35 and english[i] >= 35:
        passed = passed + 1
    else:
        failed = failed + 1

class_average = sum(averages) / len(averages)

print("Total Students:", len(students))
print("Students Passed:", passed)
print("Students Failed:", failed)
print("Class Average:", round(class_average, 2), "%")


# Chart 1: Student-wise total marks
plt.figure(figsize=(8, 5))
plt.bar(students, totals)
plt.title("Student Total Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.ylim(0, 300)
plt.show()

# Chart 2: Subject-wise average marks
plt.figure(figsize=(8, 5))
plt.bar(subjects, subject_averages)
plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.show()
