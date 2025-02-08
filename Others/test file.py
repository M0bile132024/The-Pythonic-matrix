#test file
import tkinter as tk

def copy_to_keyboard(text,true_or_false):
    if true_or_false == True:    
        root = tk.Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        print("Text copied to clipboard!")
        root.destroy()

        return
    else:
        return
def print_clipboard():
    root = tk.Tk()
    root.withdraw()
    print(root.clipboard_get())
copy_to_keyboard("Hello",True)
copy_to_keyboard("World",True)
print_clipboard()
