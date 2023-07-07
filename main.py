import requests
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("To Do")
root.geometry("600x500")
root.configure(bg="black")

# Microsoft To Do API endpoint and authentication headers
todo_task_list_id = "YOUR_TASK_LIST_ID"
api_url = f"https://graph.microsoft.com/v1.0/me/todo/lists/{todo_task_list_id}/tasks"
access_token = "YOUR_ACCESS_TOKEN"  

def get_tasks():
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        tasks = response.json().get("value")
        if tasks:
            for task in tasks:
                # Process and display each task in your app's UI
                task_name = task["title"]
                # ... Add your code to display the task in your app ...
        else:
            print("No tasks found.")
    else:
        print(f"Failed to retrieve tasks. Error: {response.status_code}")

def frame1():
    global frame1e
    frame1e = Frame(root)
    frame1e.grid(row=0, column=0, sticky="NSEW")
    frame1e.configure(bg="black")
    # Call the get_tasks function to retrieve and display your tasks
    get_tasks()



if 1 == 1:
    frame1()
else:
    frame1()

root.mainloop() # ends the main loop
