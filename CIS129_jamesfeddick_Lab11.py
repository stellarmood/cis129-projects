# Open the file in write mode
with open('grades.txt', 'w') as file:
    while True:
        grade = input("Enter a grade (or -1 to stop): ")
        if grade == '-1':
            break
        if grade.isdigit():
            file.write(f"{grade}\n")
        else:
            print("Please enter a valid integer grade.")
# Initialize variables
total = 0
count = 0

# Open and read the file
with open('grades.txt', 'r') as file:
    print("Grades:")
    for line in file:
        grade = int(line.strip())
        print(grade)
        total += grade
        count += 1

# Calculate average
average = total / count if count != 0 else 0

# Display results
print(f"\nTotal of the {count} grades is {total}")
print(f"Class average is {average:.2f}")
import csv

# Open CSV file for writing
with open('grades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    while True:
        first = input("Enter student's first name (or 'done' to finish): ")
        if first.lower() == 'done':
            break
        last = input("Enter student's last name: ")
        try:
            exam1 = int(input("Enter exam 1 grade: "))
            exam2 = int(input("Enter exam 2 grade: "))
            exam3 = int(input("Enter exam 3 grade: "))
            writer.writerow([first, last, exam1, exam2, exam3])
        except ValueError:
            print("Please enter valid integer grades.")
