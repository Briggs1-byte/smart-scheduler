import json

def load_data():
    try:
        with open("exams.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open("exams.json", "w") as f:
        json.dump(data, f, indent=4)

def show_menu():
    print("\nSmart Scheduler")
    print("1. Add Exam")
    print("2. View Exams")
    print("3. Edit Exam")
    print("4. Delete Exam")
    print("5. Exit")

def add_exam(data):
    name = input("Exam name: ")
    date = input("Date (YYYY-MM-DD): ")
    time = input("Time (HH:MM): ")
    room = input("Room: ")
    data.append({"name": name, "date": date, "time": time, "room": room})
    save_data(data)
    print("Exam added.")

def view_exams(data):
    if not data:
        print("No exams scheduled.")
        return
    for i, exam in enumerate(data):
        print(f"{i+1}. {exam['name']} on {exam['date']} at {exam['time']} in {exam['room']}")

def edit_exam(data):
    view_exams(data)
    idx = int(input("Select exam number to edit: ")) - 1
    if 0 <= idx < len(data):
        data[idx]['name'] = input("New Exam name: ")
        data[idx]['date'] = input("New Date (YYYY-MM-DD): ")
        data[idx]['time'] = input("New Time (HH:MM): ")
        data[idx]['room'] = input("New Room: ")
        save_data(data)
        print("Exam updated.")
    else:
        print("Invalid selection.")

def delete_exam(data):
    view_exams(data)
    idx = int(input("Select exam number to delete: ")) - 1
    if 0 <= idx < len(data):
        del data[idx]
        save_data(data)
        print("Exam deleted.")
    else:
        print("Invalid selection.")

def main():
    data = load_data()
    while True:
        show_menu()
        choice = input("Enter choice: ")
        if choice == '1':
            add_exam(data)
        elif choice == '2':
            view_exams(data)
        elif choice == '3':
            edit_exam(data)
        elif choice == '4':
            delete_exam(data)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if _name_ == "_main_":
    main()