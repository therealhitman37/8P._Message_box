from tkinter import *
from tkinter import messagebox

window = Tk()

# Put the window in the middle of the screen and on top of other window
window.eval("tk::PlaceWindow %s center" % window.winfo_toplevel())     

# Make tk window invisible
window.withdraw()

# Content of the message box
# messagebox.showinfo("Question","Are you fat like a big pig eating every day")
# messagebox.askyesno("Question","Are you fat like a big pig eating every day")
# messagebox.askokcancel("Question","Are you fat like a big pig eating every day")
# messagebox.askretrycancel("Question","Are you fat like a big pig eating every day")

if messagebox.askyesno("Question","Are you fat like a big pig eating every day", icon = "info") == True:
    print("Yes")
else:
    print("No")

# Quit window
window.deiconify()
window.destroy()
window.quit()