# Step 1: Import the required packages
import threading
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import client

def send_message():
    message = entry.get()
    client.send_message(message)
    list_box.insert(tk.END, "You: " + message)
    entry.delete(0, tk.END)

def receive_messages():
    while True:
        try:
            message = client.client_socket.recv(1024).decode()
            if message:
                list_box.insert(tk.END, message)
        except:
            break

def start_client():
    client.on_message_received = on_message_received  # Set the callback for received messages
    client.start_client()
    threading.Thread(target=receive_messages).start()

def on_message_received(message):
    list_box.insert(tk.END, message)

# Create the main window
root = ThemedTk(theme="arc")
root.title("Chat App")
root.geometry("300x200")

# Configure the grid layout
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_columnconfigure(0, weight=1)

# Create widgets
list_box = tk.Listbox(root)
scroll_bar = ttk.Scrollbar(root)
entry = ttk.Entry(root)
send_btn = ttk.Button(root, text="Send", command=send_message)

# Arrange widgets using grid
list_box.grid(row=0, column=0, sticky="nsew")
scroll_bar.grid(row=0, column=1, sticky="ns")
entry.grid(row=1, column=0, sticky="ew")
send_btn.grid(row=2, column=0, sticky="ew")

# Attach the scrollbar to the listbox
list_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_box.yview)

# Start the client
start_client()

# Start the Tkinter event loop
root.mainloop()
