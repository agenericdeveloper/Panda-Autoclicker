import tkinter as tk
import threading
import pyautogui
import time
import keyboard

class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Panda Autoclicker")

        self.clicking = False

        self.start_button = tk.Button(root, text="Start Clicking", command=self.start_clicking)
        self.stop_button = tk.Button(root, text="Stop Clicking", command=self.stop_clicking)

        self.start_button.pack(pady=10)
        self.stop_button.pack()

        # Set the initial window size (width x height)
        self.root.geometry("200x100") 

        # Create a label for failsafe
        self.failsafe_label = tk.Label(root, text="", font=("Arial", 12))

    def click(self):
        while self.clicking:
            pyautogui.click()

            time.sleep(0.000000001) 

    def start_clicking(self):
        if not self.clicking:
            self.clicking = True
            self.click_thread = threading.Thread(target=self.click)
            self.click_thread.start()

    def stop_clicking(self):
        self.clicking = False

    def check_failsafe(self):
        while True:
            if keyboard.is_pressed('ctrl+alt'):
                self.start_button.pack_forget()
                self.stop_button.pack_forget()
                self.failsafe_label.config(text="Failsafe activated!")
                self.failsafe_label.pack(pady=10)
                self.stop_clicking()
                break
            else:
                self.failsafe_label.config(text="")
            time.sleep(0.0001)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClickerApp(root)
    failsafe_thread = threading.Thread(target=app.check_failsafe)
    failsafe_thread.start()
    root.mainloop()
