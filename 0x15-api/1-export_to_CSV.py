#!/usr/bin/python3
"""
extend Python script to export data in the CSV format.
"""

import csv
import json
import sys
import urllib.request

if __name__ == "__main__":
    employee_ID = sys.argv[1]

    employee_data = urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}/".format(
            employee_ID))
    employee_tasks = urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
            employee_ID))

    employee_data_dict = json.loads(employee_data.read().decode())
    employee_task_data_dict = json.loads(employee_tasks.read().decode())

    task_done_count = 0  # counter for tasks done
    total_tasks = 0  # counter for all tasks
    completed_tasks = []  # list to contain completed tasks
    for i in employee_task_data_dict:
        if i["completed"] is True:
            completed_tasks.append(i)
            task_done_count += 1
        total_tasks += 1

    EMPLOYEE_NAME = employee_data_dict["name"]
    USERNAME = employee_data_dict["username"]
    USER_ID = employee_data_dict["id"]

    filename = "{}.csv".format(USER_ID)
    with open(filename, mode="w", newline="") as csv_file:
        fieldnames = ["USER_ID",
                      "USERNAME",
                      "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csv_file,
                                fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        # writer.writeheader()

        for task in employee_task_data_dict:
            task_status = "True" if task["completed"] else "False"
            writer.writerow({
                "USER_ID": USER_ID,
                "USERNAME": USERNAME,
                "TASK_COMPLETED_STATUS": task_status,
                "TASK_TITLE": task["title"]
            })
