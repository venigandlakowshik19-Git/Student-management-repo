import json

FILENAME = "students.json"

def load_students():
    try:
        with open(FILENAME,'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
def add_student(students):
    sid = input('Enter Student ID:')
    name = input('Enter Name:')
    age = input('Enter Age:')
    course = input('Enter Course:')
    marks = input('Enter Marks:')
    students.append({
        "id":sid,
        "name":name,
        "age":age,
        "course":course,
        "marks":marks
    })
    print('student added succesfully')

def display_student(students):
    if not students:
        print('no students records found')
        return
    print('\n----STUDENTS RECORDS----')
    for s in students:
        print(f'ID:{s['id']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}, Marks: {s['marks']}')

def search_student(students):
    sid = input('Enter student ID to search:')

    for s in students:
        if s['id'] == sid:
            print(f'Found -> {s}')
            return
    print('Student Record Not Found')   

def update_student(students):
    sid = input('Enter student ID to Update:')

    for s in students:
        if s['id'] == sid:
            s['name'] = input('Enter New Name:')
            s['age'] = input('Enter New Age:')
            s['course'] = input('Enter New course:')
            s['marks'] = input('Enter New Marks:')

            print('student updated successfully')
            return
        print('student not Found')

def delete_student(students):
    sid = input('Enter student ID to delete:')
    
    for s in students:
        if s['id'] == sid:
            students.remove(s)
            print(f'student deleted successfully')
            return
    print('Student Record Not Found')


def save_student(students):
    with open(FILENAME,'w') as f:
        json.dump(students,f,indent=4)
def main():

    students = load_students()

    while True:
        print("\n====== Student DataBase Menu ======")
        print("1. Add student")
        print("2. Display Students")
        print("3. Search Student")      
        print("4. Update Student")
        print("5. Delete Student")      
        print("6. Save & Exit")

        choice = input('Enter your choice:')

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_student(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            save_student(students)
            print("Data saved. Existing program.")
            break
        else:
            print("Invalid choice! Try again.")
main()







