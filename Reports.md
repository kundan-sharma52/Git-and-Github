Student Record Management System

University: Rungta International Skills University
School: School of Computer Science and Engineering
Program: B.Tech Computer Science and Engineering
Project (PS No.): 8
Language: Python 3

Name: Kundan Kumar   Date: 15-11-2026

1. Problem Statement

Develop a console-based system to maintain student records (roll number, name, course, marks) with the ability to add, view, search, update and delete records. Roll numbers must be unique and marks must be between 0 and 100.

2. Objectives
Implement CRUD operations using Python.
Use Lists, Tuples and Dictionaries to store and handle data.
Validate input (unique roll number, marks in range 0-100).
Display records in a neat table format.

3. Concepts Used
Concept	Where it is used
Dictionary	records = {roll: (name, course, marks)}. The roll number is the key, so it stays unique.
Tuple	Stores one student's data (name, course, marks).
List	Sorted list of records used to print the table.
Functions	One separate function for each CRUD operation.
Loop and conditions	Menu loop, input validation.

4. Functions
Function	Operation	Description
add_student()	Create	Adds a record after checking duplicate roll number and valid marks.
view_students()	Read	Shows all records in a table.
search_student()	Read	Finds a student by roll number.
update_student()	Update	Changes marks of an existing student.
delete_student()	Delete	Removes a record by roll number.
main()	Menu	Shows the menu and calls the chosen function.

5. Algorithm (Steps)
Start the program and show the menu.
Take the user's choice (1-6).
Call the matching function (add / view / search / update / delete).
Validate input where needed.
Show the result message.
Repeat until the user chooses Exit.

6. How to Run
python studentRecords.py

7. Test Cases
Test	Input	Expected Output	Result
1. Normal	Add: 101, Aman, BTech, 78	Record added: 101 | Aman | BTech | 78	Pass
2. Boundary	Add: 102, Riya, BTech, 100	Record added: 102 | Riya | BTech | 100	Pass
3a. Invalid	Add: 101, Neha, BTech, 70	Roll number 101 already exists.	Pass
3b. Invalid	Add: 103, Ravi, BTech, 150	Marks must be between 0 and 100.	Pass
4a. Valid	Search: 101	101 | Aman | BTech | 78	Pass
4b. Valid	Update marks of 101 to 85	Marks updated: 85	Pass
4c. Valid	Delete: 999	Roll number 999 not found.	Pass

8. Sample Output (View)
+--------+----------------------+------------+--------+
| Roll   | Name                 | Course     | Marks  |
+--------+----------------------+------------+--------+
| 101    | Aman                 | BTech      | 85     |
| 102    | Riya                 | BTech      | 100    |
+--------+----------------------+------------+--------+

9. Conclusion

The project successfully manages student records using Lists, Tuples and Dictionaries. All CRUD operations work, input is validated, and all given test cases pass.

10. GitHub Link

https://github.com/kundan-sharma52/Git-and-Github.git
https://github.com/kundan-sharma52/Git-and-Github.git
    https://github.com/kundan-sharma52/Git-and-Github.git
