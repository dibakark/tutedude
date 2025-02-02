employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}
}

def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using EMS. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


def add_employee():
    while True:
        try:
          emp_id = int(input("Enter Employee ID: "))
          if emp_id in employees:
              print("Employee ID already exists. Please enter a unique ID.")
              continue
          break
        except ValueError:
          print("Invalid ID. Please enter a valid integer ID")
          continue


    name = input("Enter Employee Name: ")
    while True:
      try:
        age = int(input("Enter Employee Age: "))
        if age <= 0:
          print("Invalid age. Please enter a valid age")
          continue
        break
      except ValueError:
        print("Invalid age. Please enter a valid integer age")
        continue
    department = input("Enter Employee Department: ")
    while True:
        try:
          salary = int(input("Enter Employee Salary: "))
          if salary <= 0:
            print("Invalid salary. Please enter a valid salary")
            continue
          break
        except ValueError:
          print("Invalid salary. Please enter a valid integer salary")
          continue

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print("Employee added successfully!")


def view_employees():
    if not employees:
        print("No employees available.")
        return

    print("\nEmployee Details:")
    print("-" * 60)
    print("{:<8} {:<15} {:<5} {:<15} {:<10}".format("ID", "Name", "Age", "Department", "Salary"))
    print("-" * 60)

    for emp_id, emp_data in employees.items():
        print("{:<8} {:<15} {:<5} {:<15} {:<10}".format(emp_id, emp_data['name'], emp_data['age'], emp_data['department'], emp_data['salary']))

    print("-" * 60)


def search_employee():
    while True:
      try:
        emp_id = int(input("Enter Employee ID to search: "))
        break
      except ValueError:
        print("Invalid ID. Please enter a valid integer ID")
        continue

    if emp_id in employees:
        emp_data = employees[emp_id]
        print("\nEmployee Details:")
        print("-" * 40)
        print("Name:", emp_data['name'])
        print("Age:", emp_data['age'])
        print("Department:", emp_data['department'])
        print("Salary:", emp_data['salary'])
        print("-" * 40)
    else:
        print("Employee not found.")


if __name__ == "__main__":
  main_menu()