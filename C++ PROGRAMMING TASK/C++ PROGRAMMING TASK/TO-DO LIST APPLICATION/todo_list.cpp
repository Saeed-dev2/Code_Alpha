#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Task structure to store task details
struct Task {
    string description;
    bool isCompleted;

    Task(string desc) : description(desc), isCompleted(false) {}
};

// ToDoList class to manage tasks
class ToDoList {
private:
    vector<Task> tasks;

public:
    // Add a new task
    void addTask(const string& description) {
        tasks.emplace_back(description);
        cout << "Task added successfully.\n";
    }

    // Mark a task as completed
    void markCompleted(int index) {
        if (index < 1 || index > tasks.size()) {
            cout << "Invalid task number.\n";
            return;
        }
        tasks[index - 1].isCompleted = true;
        cout << "Task marked as completed.\n";
    }

    // Display current tasks
    void viewTasks() const {
        if (tasks.empty()) {
            cout << "No tasks to show.\n";
            return;
        }
        cout << "\nCurrent Tasks:\n";
        for (size_t i = 0; i < tasks.size(); ++i) {
            cout << i + 1 << ". " << tasks[i].description;
            if (tasks[i].isCompleted) {
                cout << " [Completed]";
            }
            cout << "\n";
        }
    }
};

int main() {
    ToDoList todoList;
    int choice;
    do {
        // Display menu
        cout << "\n--- To-Do List Menu ---\n";
        cout << "1. Add Task\n";
        cout << "2. Mark Task as Completed\n";
        cout << "3. View Tasks\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        cin.ignore(); // Clear input buffer

        switch (choice) {
        case 1: {
            string description;
            cout << "Enter task description: ";
            getline(cin, description);
            todoList.addTask(description);
            break;
        }
        case 2: {
            int taskNumber;
            cout << "Enter task number to mark as completed: ";
            cin >> taskNumber;
            todoList.markCompleted(taskNumber);
            break;
        }
        case 3:
            todoList.viewTasks();
            break;
        case 4:
            cout << "Exiting application. Goodbye!\n";
            break;
        default:
            cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 4);

    return 0;
}
