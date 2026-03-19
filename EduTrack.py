class Student:
    def __init__(self, name, usn, marks):
        self.name = name
        self.usn = usn
        self.marks = marks

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"

    def display(self):
        print("\n---------------------------")
        print("Name:", self.name)
        print("USN:", self.usn)
        print("Marks:", self.marks)
        print("Average:", round(self.average(), 2))
        print("Grade:", self.grade())
        print("---------------------------")


class StudentAnalyzer:
    def __init__(self):
        self.students = []

    
    def add_student(self):
        name = input("Enter Name: ")
        usn = input("Enter USN: ")

        marks = {}

        
        while True:
            try:
                n = int(input("Enter number of subjects: "))
                if n <= 0:
                    print("Number must be positive.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        for _ in range(n):
            subject = input("Subject name: ")

            
            while True:
                try:
                    mark = float(input("Marks: "))
                    if mark < 0 or mark > 100:
                        print("Marks must be between 0 and 100.")
                        continue
                    break
                except ValueError:
                    print("Please enter valid numeric marks.")

            marks[subject] = mark

        self.students.append(Student(name, usn, marks))
        print("Student added successfully!")

    
    def display_all(self):
        if not self.students:
            print("No students available.")
            return

        for student in self.students:
            student.display()

   
    def update_student(self):
        usn = input("Enter USN to update: ")
        for student in self.students:
            if student.usn == usn:
                subject = input("Enter subject to update: ")
                if subject in student.marks:
                    while True:
                        try:
                            new_mark = float(input("Enter new marks: "))
                            if new_mark < 0 or new_mark > 100:
                                print("Marks must be between 0 and 100.")
                                continue
                            break
                        except ValueError:
                            print("Enter valid numeric marks.")

                    student.marks[subject] = new_mark
                    print("Marks updated successfully.")
                else:
                    print("Subject not found.")
                return
        print("Student not found.")

    
    def remove_student(self):
        usn = input("Enter USN to remove: ")
        for student in self.students:
            if student.usn == usn:
                self.students.remove(student)
                print("Student removed successfully.")
                return
        print("Student not found.")

    
    def find_topper(self):
        if not self.students:
            print("No students available.")
            return

        topper = max(self.students, key=lambda s: s.average())
        print("\nClass Topper:")
        topper.display()

    def rank_students(self):
        if not self.students:
            print("No students available.")
            return

        ranked = sorted(self.students, key=lambda s: s.average(), reverse=True)

        print("\nStudent Rankings:")
        for i, student in enumerate(ranked, start=1):
            print(f"Rank {i}: {student.name} - Avg: {round(student.average(),2)}")

    def search_student(self):
        usn = input("Enter USN to search: ")
        for student in self.students:
            if student.usn == usn:
                print("Student Found:")
                student.display()
                return
        print("Student not found.")

    def grade_distribution(self):
        if not self.students:
            print("No students available.")
            return

        grades = {"A": 0, "B": 0, "C": 0, "Fail": 0}

        for student in self.students:
            grades[student.grade()] += 1

        print("\nGrade Distribution:")
        for grade, count in grades.items():
            print(f"{grade}: {count}")

    def subject_analysis(self):
        if not self.students:
            print("No students available.")
            return

        subject_totals = {}

        for student in self.students:
            for subject, mark in student.marks.items():
                if subject not in subject_totals:
                    subject_totals[subject] = []
                subject_totals[subject].append(mark)

        print("\nSubject Analysis (Average Marks):")
        for subject, marks in subject_totals.items():
            avg = sum(marks) / len(marks)
            print(f"{subject} - {round(avg,2)}")

    def class_statistics(self):
        if not self.students:
            print("No students available.")
            return

        total_avg = sum(s.average() for s in self.students) / len(self.students)
        pass_count = sum(1 for s in self.students if s.grade() != "Fail")
        fail_count = sum(1 for s in self.students if s.grade() == "Fail")

        print("\nClass Statistics")
        print("Class Average:", round(total_avg, 2))
        print("Pass Students:", pass_count)
        print("Fail Students:", fail_count)



def main():
    system = StudentAnalyzer()

    while True:
        print("\n========= MENU =========")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Marks")
        print("4. Remove Student")
        print("5. Find Class Topper")
        print("6. Rank Students")
        print("7. Search Student")
        print("8. Grade Distribution")
        print("9. Subject Analysis")
        print("10. Class Statistics")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.display_all()
        elif choice == "3":
            system.update_student()
        elif choice == "4":
            system.remove_student()
        elif choice == "5":
            system.find_topper()
        elif choice == "6":
            system.rank_students()
        elif choice == "7":
            system.search_student()
        elif choice == "8":
            system.grade_distribution()
        elif choice == "9":
            system.subject_analysis()
        elif choice == "10":
            system.class_statistics()
        elif choice == "11":
            print("Program exited.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()