records = {}


def read_roll(prompt="Enter roll number: "):
    """Read a roll number and make sure it is a valid integer."""
    value = input(prompt).strip()
    if not value.isdigit():
        print("Roll number must be a number.")
        return None
    return int(value)


def read_marks(prompt="Enter marks: "):
    """Read marks and make sure they are a number between 0 and 100."""
    value = input(prompt).strip()
    if not value.lstrip("-").isdigit():
        print("Marks must be a number.")
        return None
    marks = int(value)
    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        return None
    return marks


def add_student():
    """CREATE: add a new student record."""
    roll = read_roll()
    if roll is None:
        return
    if roll in records:
        print(f"Roll number {roll} already exists.")
        return
    name = input("Enter name: ").strip()
    course = input("Enter course: ").strip()
    if name == "" or course == "":
        print("Name and course cannot be empty.")
        return
    marks = read_marks()
    if marks is None:
        return
    records[roll] = (name, course, marks)
    print(f"Record added: {roll} | {name} | {course} | {marks}")


def view_students():
    """READ: display all records in a neat table."""
    if not records:
        print("No records found.")
        return
    rows = sorted(records.items())  # list of (roll, (name, course, marks))
    line = "+" + "-" * 8 + "+" + "-" * 22 + "+" + "-" * 12 + "+" + "-" * 8 + "+"
    print(line)
    print(f"| {'Roll':<6} | {'Name':<20} | {'Course':<10} | {'Marks':<6} |")
    print(line)
    for roll, (name, course, marks) in rows:
        print(f"| {roll:<6} | {name:<20} | {course:<10} | {marks:<6} |")
    print(line)


def search_student():
    """READ: search one student by roll number."""
    roll = read_roll()
    if roll is None:
        return
    if roll not in records:
        print(f"Roll number {roll} not found.")
        return
    name, course, marks = records[roll]
    print(f"{roll} | {name} | {course} | {marks}")


def update_student():
    """UPDATE: change the marks of a student."""
    roll = read_roll()
    if roll is None:
        return
    if roll not in records:
        print(f"Roll number {roll} not found.")
        return
    marks = read_marks("Enter new marks: ")
    if marks is None:
        return
    name, course, _ = records[roll]
    records[roll] = (name, course, marks)  # tuples are immutable, so make a new one
    print(f"Marks updated: {marks}")


def delete_student():
    """DELETE: remove a student record."""
    roll = read_roll()
    if roll is None:
        return
    if roll not in records:
        print(f"Roll number {roll} not found.")
        return
    del records[roll]
    print(f"Record deleted: {roll}")


def show_menu():
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")


def main():
    actions = {
        "1": add_student,
        "2": view_students,
        "3": search_student,
        "4": update_student,
        "5": delete_student,
    }
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()