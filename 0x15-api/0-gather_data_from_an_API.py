#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    # Check if the user provided the employee ID as argument
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    # Save employee ID provided by the user
    employee_id = sys.argv[1]

    # Get employee info
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(user_url)
    user_data = response.json()

    # Get employee's TODO list
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response = requests.get(todo_url)
    todo_data = response.json()

    # Extract completed tasks and count them
    completed_tasks = [task for task in todo_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    num_total_tasks = len(todo_data)

    # Print employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(user_data['name'], num_completed_tasks, num_total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task['title']))