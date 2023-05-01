"""Process control module."""
import tkinter as tk
from tkinter import messagebox


class Manager:
    """Application management class."""

    def get_list_of_applications(self):
        """Receiving all snap packages and standard applications."""
        from windows_tools.installed_software import get_installed_software
        return ','.join([software['name'] for software in get_installed_software()])

    def manage_application(self, app_name, is_close=False):
        """Starting or stopping applications and processes."""
        from AppOpener import open, close
        try:
            if is_close:
                close(app_name.split()[0])
            else:
                print('open')
                open(app_name)
        except FileNotFoundError as ex:
            print(ex)

    def sending_messages(self, message):
        """Sending messages that are called as new windows."""
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning('New message', message.strip())
