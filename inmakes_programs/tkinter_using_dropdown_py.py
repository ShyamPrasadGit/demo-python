from tkinter import  *
root=Tk()
mymenu = Menu(root)
root.config(menu=mymenu)
submenu = Menu(mymenu)
def np():
    print("This is a new project")
def op():
    print("Project opened")
def sp():
    print("Project saved")
def csa():
    print("Clicked save as")
def css():
    print("Clicked settings")
def cfp():
    print("Clicked file properties")


mymenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New project",command=np)
submenu.add_command(label="Open project",command=op)
submenu.add_separator()
submenu.add_command(label="Save",command=sp)
submenu.add_command(label="Save as",command=csa)
submenu.add_separator()
submenu.add_command(label="Settings",command=css)
submenu.add_command(label="File properties",command=cfp)
submenu.add_separator()
submenu.add_command(label="Exit")

def cu():
    print("Clicked undo")
def cr():
    print("Clicked redo")
def cct():
    print("Clicked cut")
def ctp():
    print("Clicked copy")
def cpe():
    print("Clicked paste")

editmenu = Menu(mymenu)
mymenu.add_cascade(label="edit", menu=editmenu)
editmenu.add_command(label="Undo",command=cu)
editmenu.add_command(label="Redo",command=cr)
editmenu.add_separator()
editmenu.add_command(label="Cut",command=cct)
editmenu.add_command(label="Copy",command=ctp)
editmenu.add_command(label="Paste",command=cpe)

def ctm():
    print("Clicked Tool menu")
def cae():
    print("Clicked Appearance")
def crcf():
    print("Clicked Recently changed files")
def crl():
    print("Clicked Recent locations")

viewmenu = Menu(mymenu)
mymenu.add_cascade(label="View", menu=viewmenu)
viewmenu.add_command(label="Tool menu",command=ctm)
viewmenu.add_command(label="Appearance",command=cae)
viewmenu.add_separator()
viewmenu.add_command(label="Recently changed files",command=crcf)
viewmenu.add_command(label="Recent locations",command=crl)
viewmenu.add_separator()
viewmenu.add_command(label="Quick switch")
viewmenu.add_command(label="Active scheme")

navigatemenu = Menu(mymenu)
mymenu.add_cascade(label="Navigate", menu=navigatemenu)
navigatemenu.add_command(label="< back")

codemenu = Menu(mymenu)
mymenu.add_cascade(label="Code", menu=codemenu)
codemenu.add_command(label="Generate")

root.mainloop()