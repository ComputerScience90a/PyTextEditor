from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename
import os
import webbrowser
def source1(event):
 link="https://github.com/ComputerScience90a/PyTextEditor";
 webbrowser.open(link);


root=Tk();
root.geometry('1370x800');
root.title("Atom Editor");
root.resizable(0,0)


#------------------------------------------------------------------------------------------------------------------------------->
#-                                                                                                                             -
#-              Author:Sumit Kumar                                                                                             -
#-              Logic:reading,writing files                                                                                    -
#-              Knowledge:Little python,GUI tkinter                                                                            -
#-                                                                                                                             -
#-                                                                                                                             -
#-                                                                                                                             -
#-                                                                                                                             -
#-                                                                                                                             -
#-                                                                                                                             -
#-                                                                                                                             -
#-                                                                                                                             -
#-                                                                                                                             -
#------------------------------------------------------------------------------------------------------------------------------->

#Font size

#Exit section
def exit1():
        root.destroy();
#About Section
        
def about():
	about=Tk();
	about.title("About");
	about.configure(bg="#262626");
	about.geometry("400x500");
	about.resizable(0,0);
	label=Label(about,text="Atom Text Editor",font=("courier",20),bg="#262626",fg="#fff");
	label_2=Label(about,text="A lightweight Text Editor For Windows\n Made With Python 3.6",bg='#262626',fg="#fff");
	email=Label(about,text="email:sbcuston@gmail.com",font=("arial",12),bg="#262626",fg="#fff");
	version=Label(about,text="version:Beta(v1.0)",font=("arial",12),bg="#262626",fg="#fff");
	source=Label(about,text="Get Source from:https://github.com/ComputerScience90a/PyTextEditor",font=("arial",8),bg="#262626",fg="#fff");
	source.bind("<Button-1>", source1)
	credit=Label(about,text="Credits",fg="#262626",bg="#ccc",bd="0.5");
	Sumit=Label(about,text="1.Sumit(Programmer)",fg="#fff",bg="#262626");
	Sumit.place(x="80",y="400");
	kabir=Label(about,text="2.Prashant Gautam(Helper)",fg="#fff",bg="#262626");
	kabir.place(x="80",y="420");
	rahul=Label(about,text="3.Rahul Khatri(Documentary)",fg="#fff",bg="#262626");
	rahul.place(x="80",y="440");
	somya=Label(about,text="4.Somya Sinha(Source Provider)",fg="#fff",bg="#262626");
	somya.place(x="80",y="460");
	credit.place(x="170",y="380");
	source.place(x="35",y="320");
	version.place(x="80",y="300");
	email.place(x="80",y="280");
	label_2.place(x="80",y="150");
	label.place(x="80",y="100");
	about.mainloop();

def doc():
	doc=Tk();
	doc.title("Documentation");
	doc.geometry("400x500");
	doc.mainloop();
#EDIT OPTION
def copy():
        text.event_generate("<<Copy>>")
def cut():
        text.event_generate("<<Cut>>")
def paste():
        text.event_generate("<<Paste>>")
#New file
def New():
    root.title("Untitled");
    text.delete(1.0,END)
#open a file
def Open():
         
        file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt")])
 
        if file == "":
             
            # no file to open
            file = None
        else:
             
            # Try to open the file
            # set the window title
            root.title(os.path.basename(file) + " - Notepad")
            text.delete(1.0,END)
 
            file = open(file,"r")
 
            text.insert(1.0,file.read())
 
            file.close()

#Themes Function

def dark():
    text.configure(bg="#262626",fg="#fff");
    subMenu.configure(bg="#262626",fg="#fff");
    fontMenu.configure(bg="#262626",fg="#fff");
    themeMenu.configure(bg="#262626",fg="#fff");

def light():
    text.configure(bg="#fafafa",fg="#262626");
    subMenu.configure(bg="#fafafa",fg="#262626");
    fontMenu.configure(bg="#fafafa",fg="#262626");
    themeMenu.configure(bg="#fafafa",fg="#262626");
def blue():
    text.configure(bg="#834bff",fg="#fff");
    subMenu.configure(bg="#834bff",fg="#fff");
    fontMenu.configure(bg="#834bff",fg="#fff");
    themeMenu.configure(bg="#834bff",fg="#fff");
def pp():
    text.configure(bg="#607D8B",fg="#fff");
    subMenu.configure(bg="#607D8B",fg="#fff");
    fontMenu.configure(bg="#607D8B",fg="#fff");
    themeMenu.configure(bg="#607D8B",fg="#fff");
def red():
    text.configure(bg="#C2185B",fg="#fff");
    subMenu.configure(bg="#C2185B",fg="#fff");
    fontMenu.configure(bg="#C2185B",fg="#fff");
    themeMenu.configure(bg="#C2185B",fg="#fff");

#End of Themes Function
def saveas(event):
    name=asksaveasfile(mode='w',defaultextension=".txt",
                                      filetypes=[("All Files","*.*")])
    text2save=str(text.get(0.0,END))
    name.write(text2save)
    name.close()
    root.quit()
root.bind('<Control-s>', saveas)
def newas(event):
    root.title("Untitled");
    text.delete(1.0,END)
root.bind('<Control-n>', newas)

#Font Section
def FontHelvetica():

   global text
   text.config(font=("Helvetica",35))
def FontCourier():
    global text
    text.config(font="Courier")
def FontImpact():
    global text
    text.config(font="Impact")
#File Saving Function
def save():
    name=asksaveasfile(mode='w',defaultextension=".txt")
    text2save=str(text.get(0.0,END))
    name.write(text2save)


#File Menu

menu=Menu(root);
root.config(menu=menu);
subMenu=Menu(menu,tearoff=0);
menu.add_cascade(label="File",menu=subMenu);
subMenu.add_command(label="New ctrl+N",command=New);
subMenu.add_command(label="Open",command=Open);
subMenu.add_command(label="Save",command=save);
subMenu.add_command(label="Save As",command=saveas);
subMenu.add_command(label="Exit",command=exit1);

#EDIT MENU
EDIT=Menu(menu,tearoff=0);
menu.add_cascade(label="Edit",menu=EDIT);
EDIT.add_command(label="copy",command=copy);
EDIT.add_command(label="cut",command=cut);
EDIT.add_command(label="Paste",command=paste);
#Fonts
fontMenu=Menu(menu,tearoff=0);
menu.add_cascade(label="Fonts",menu=fontMenu);
fontMenu.add_command(label="Halvetica",command=FontHelvetica);
fontMenu.add_command(label="Courier",command=FontCourier);
fontMenu.add_command(label="Impact",command=FontImpact);
#Themes
themeMenu=Menu(menu,tearoff=0);
menu.add_cascade(label="Theme",menu=themeMenu);
themeMenu.add_command(label="Dark",command=dark);
themeMenu.add_command(label="Light",command=light);
themeMenu.add_command(label="Blue",command=blue);
themeMenu.add_command(label="Blue Grey",command=pp);
themeMenu.add_command(label="Purple",command=red);
#Help Section

Help=Menu(menu,tearoff=0);
menu.add_cascade(label="Help",menu=Help);
Help.add_command(label="About AtomEditor",command=about);
Help.add_command(label="Documentaion",command=doc);



#scrollbar

S = Scrollbar(root)
text = Text(root, height=700, width=200)
S.pack(side=RIGHT, fill=Y)
text.pack(side=LEFT, fill=Y)
S.config(command=text.yview)
text.config(yscrollcommand=S.set)
#Editable Widget comes From Here

root.mainloop();
