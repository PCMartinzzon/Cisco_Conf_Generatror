import os
import tkinter as tk
from tkinter import ttk, messagebox

def create_router_config():
    dir_path = os.getcwd()
    hostname = router_hostname_entry.get()
    secret = router_secret_entry.get()
    console = router_console_entry.get()
    vty = router_vty_entry.get()
    filename = f"{hostname}_router.txt"  # Specify the filename for the router config
    # Rest of your router configuration code here...

    try:
        with open(filename, "w") as r:
            # Rest of your router configuration code here...
            r.write(f"enable\nconfigure terminal\n!\n")
            r.write(f"hostname {hostname}\n!\n")
            r.write(f"enable secret {secret}\n!\n")
            r.write(f"line console 0\n")
            r.write(f" password {console}\n")
            r.write(f" login\n!\n")
            # Write the router configuration to the file

        # Show a message box when the configuration is created
        messagebox.showinfo("Router Configuration Created", f"Router config file for {hostname} has been created.\nYou can find it in: {dir_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")




def create_switch_config():
    dir_path = os.getcwd()
    hostname = switch_hostname_entry.get()
    secret = switch_secret_entry.get()
    console = switch_console_entry.get()
    vty = switch_vty_entry.get()
    filename = f"{hostname}_switch.txt"  # Specify the filename for the switch config
    # Rest of your switch configuration code here...

    try:
        with open(filename, "w") as s:
            # Rest of your switch configuration code here...
            s.write("enable\nconfigure terminal\n")
            # Write the switch configuration to the file

        # Show a message box when the configuration is created
        messagebox.showinfo("Switch Configuration Created", f"Switch config file for {hostname} has been created.\nYou can find it in: {dir_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create a tkinter window
window = tk.Tk()
window.title("Network Configuration Generator")
window.geometry("500x200")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(window)

# Router Configuration Tab
router_tab = ttk.Frame(notebook)
notebook.add(router_tab, text="Router")

# Create and arrange widgets for the router tab
tk.Label(router_tab, text="Router Configuration").pack()

tk.Label(router_tab, text="Hostname:").pack()
router_hostname_entry = tk.Entry(router_tab)
router_hostname_entry.pack()

tk.Label(router_tab, text="Secret Password:").pack()
router_secret_entry = tk.Entry(router_tab)
router_secret_entry.pack()

tk.Label(router_tab, text="Console Password:").pack()
router_console_entry = tk.Entry(router_tab)
router_console_entry.pack()

tk.Label(router_tab, text="VTY Password:").pack()
router_vty_entry = tk.Entry(router_tab)
router_vty_entry.pack()

generate_router_button = tk.Button(router_tab, text="Generate Router Configuration", command=create_router_config)
generate_router_button.pack()




# Switch Configuration Tab
switch_tab = ttk.Frame(notebook)
notebook.add(switch_tab, text="Switch")

# Create and arrange widgets for the switch tab
tk.Label(switch_tab, text="Switch Configuration").pack()

tk.Label(switch_tab, text="Hostname:").pack()
switch_hostname_entry = tk.Entry(switch_tab)
switch_hostname_entry.pack()

tk.Label(switch_tab, text="Secret Password:").pack()
switch_secret_entry = tk.Entry(switch_tab)
switch_secret_entry.pack()

tk.Label(switch_tab, text="Console Password:").pack()
switch_console_entry = tk.Entry(switch_tab)
switch_console_entry.pack()

tk.Label(switch_tab, text="VTY Password:").pack()
switch_vty_entry = tk.Entry(switch_tab)
switch_vty_entry.pack()

generate_switch_button = tk.Button(switch_tab, text="Generate Switch Configuration", command=create_switch_config)
generate_switch_button.pack()

# Pack the notebook
notebook.pack()

# Start the tkinter main loop
window.mainloop()