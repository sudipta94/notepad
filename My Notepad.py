# project name My Notepad
# Author Sudipta Das
# Email-das.sudipta94@gmail.com
# Date- 7 August 2019
# This Project is done by using Python 3.7.4 and Pycharm IDLE

# Package import
from tkinter import *
from tkinter import filedialog
from tkinter .ttk import Combobox
from datetime import datetime
import os
import time
from tkinter import font
from tkinter import colorchooser
from PIL import Image, ImageTk


class my_notepad:

    line_count: int
    word_count: int
    char_count: int
    font_family_obj = Combobox
    editor = Toplevel
    font_size_obj = Combobox
    fg_selector = Button
    bg_selector = Button
    save_changes = Toplevel

    def __init__(self, master):
        # set default value
        self.master=master
        self.font_size=11
        self.font_type='Consolas'
        self.font_color='black'
        self.background_color='white'
        self.current_path = ''
        self.last_save = True
        self.current_operation = ''
        self.right_click_state=0

        # icon folder initialize

        self.new_icon = PhotoImage(file=r"icon\new.png")
        self.open_icon=PhotoImage(file=r"icon\open.png")
        self.save_icon = PhotoImage(file=r"icon\save.png")
        self.copy_icon = PhotoImage(file=r"icon\copy.png")
        self.cut_icon = PhotoImage(file=r"icon\cut.png")
        self.paste_icon = PhotoImage(file=r"icon\paste.png")
        self.delete_icon = PhotoImage(file=r"icon\delete.png")
        self.undo_icon = PhotoImage(file=r"icon\undo.png")
        self.redo_icon = PhotoImage(file=r"icon\redo.png")
        self.find_icon = PhotoImage(file=r"icon\find.png")

        # Initial layout of My Notepad
        # Window name
        master.title("My Notepad")
        # window height and width
        master.iconbitmap(r"icon\main.ico")
        master.geometry("800x600+120+120")

        # Menu bar create
        self.main_menu = Menu(master, activeborderwidth=0)
        master.config(menu=self.main_menu)

        # file menu create
        self.file = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="File", menu=self.file)
        # sub menu create
        self.file.add_command(label="New    Ctrl+N", command=self.new_file)
        self.file.add_command(label="Open   Ctrl+O", command=self.open)
        self.file.add_command(label="Save   Ctrl+S", command=self.save)
        self.file.add_command(label="Save As", command=self.save_as)
        # add separator
        self.file.add_separator()

        self.file.add_command(label="Print...   Ctrl+P", command=self.printing)

        # add separator
        self.file.add_separator()

        self.file.add_command(label="Exit", command=self.exits)

        # edit menu create
        self.edit = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Edit", menu=self.edit)

        # sub menu create
        self.edit.add_command(label="Undo       Ctrl+Z", command=self.undoo)
        self.edit.add_command(label="Redo       Ctrl+Y", command=self.redoo)
        self.edit.add_command(label="Cut        Ctrl+X", command=self.cut)
        self.edit.add_command(label="Copy       Ctrl+C", command=self.copy)
        self.edit.add_command(label="Paste      Ctrl+V", command=self.paste)
        self.edit.add_command(label="Delete     Del", command=self.delete)

        # add separator
        self.edit.add_separator()

        self.edit.add_command(label="Find           Ctrl+F", command=self.find_frame)
        self.edit.add_command(label="Replace        Ctrl+H")

        # add separator
        self.edit.add_separator()

        self.edit.add_command(label="Time/ Date     Ctrl+T", command=self.date_time)

        # format menu create
        self.format = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Format", menu=self.format)

        # sub menu create
        self.wrap = IntVar()
        self.format.add_checkbutton(label="Word Wrap", onvalue=1, offvalue=0, command=self.word_wrap,
                                    variable=self.wrap)
        self.format.add_command(label="Editor Settings", command=self.editors)

        #  view create
        self.view = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="View", menu=self.view)

        # sub menu create
        self.bar = IntVar()
        self.view.add_checkbutton(label="Status Bar", onvalue=1, offvalue=0, command=self.status_bar,
                                  variable=self.bar)

        #  help create
        self.help = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Help", menu=self.help)

        # sub menu create
        self.help.add_command(label="About My Notepad", command=self.about)

        # main menu end
        master_top=Frame(master)
        # icon frame
        icon_frame=Frame(master_top)
        Button(icon_frame, image=self.new_icon, command=self.new_file).pack(side=LEFT)
        Button(icon_frame, image=self.open_icon, command=self.open).pack(side=LEFT)
        Button(icon_frame, image=self.save_icon, command=self.save).pack(side=LEFT)
        Button(icon_frame, image=self.copy_icon, command=self.copy).pack(side=LEFT)
        Button(icon_frame, image=self.cut_icon, command=self.cut).pack(side=LEFT)
        Button(icon_frame, image=self.paste_icon, command=self.paste).pack(side=LEFT)
        Button(icon_frame, image=self.delete_icon, command=self.delete).pack(side=LEFT)
        Button(icon_frame, image=self.undo_icon, command=self.undoo).pack(side=LEFT)
        Button(icon_frame, image=self.redo_icon, command=self.redoo).pack(side=LEFT)
        Button(icon_frame, image=self.find_icon, command=self.find_frame).pack(side=LEFT)
        icon_frame.pack(side=LEFT)
        # end icon frame
        # create frame
        self.find_frame=Frame(master_top)
        self.find_entry = Entry(self.find_frame)
        self.find_entry.pack(side=LEFT)
        self.find_button = Button(self.find_frame, text="Find", command=self.find)
        self.find_button.pack(side=LEFT)
        self.find_close = Button(self.find_frame, text="Close", command=self.find_frame_close)
        self.find_close.pack()
        self.find_frame.pack_forget()
        # create status bar label
        self.status_frame=Frame(master_top)
        self.status_bar_label = Label(self.status_frame, text="")
        self.status_bar_label.grid(row=0, column=14, sticky="ew")
        self.status_frame.pack_forget()
        master_top.pack(side=TOP, fill=X)

        buttom_master=Frame(master)

        # scroll bar object create
        self.vertical_scroll = Scrollbar(buttom_master, orient=VERTICAL)
        # text area create
        self.text_area = Text(buttom_master, yscrollcommand=self.vertical_scroll.set, undo=True)
        self.text_area.config(font=("{}".format(self.font_type), self.font_size),
                              bg=self.background_color, fg=self.font_color)
        self.text_area.pack(side=LEFT, fill=BOTH, expand=1)

        self.text_area.bind('<KeyPress>', self.save_status)

        # vertical scroll bar
        self.vertical_scroll.config(command=self.text_area.yview)
        self.vertical_scroll.pack(side=LEFT, fill=Y, padx=0, pady=0)

        buttom_master.pack(side=BOTTOM, fill=BOTH, expand=1)

        # Shortcut key
        master.bind('<Control-n>', self.new_file)
        master.bind('<Control-o>', self.open)
        master.bind('<Control-s>', self.save)
        master.bind('<Control-p>', self.printing)
        master.bind('<Control-z>', self.undoo)
        master.bind('<Control-x>', self.cut)
        master.bind('<Control-c>', self.copy)
        master.bind('<Control-v>', self.paste)
        master.bind('<Control-f>', self.find_frame)
        master.bind('<Control-t>', self.date_time)
        master.bind('<Control-y>', self.redoo)

        # end Initial layout of My Notepad
    # save status of text
    def save_status(self, event):
        self.last_save = False
        s=self.text_area.get(0.1, END)
        self.line_count =len(s.splitlines())
        self.word_count= len(s.split())
        self.char_count = 0
        for i in s:
            if not i.isspace():
                self.char_count += 1
        self.status_bar_label.config(text="Line:{} Word:{} Char:{}"
                                     .format(self.line_count, self.word_count, self.char_count+1))
    # about section

    @staticmethod
    def about():
        about = Toplevel()
        about.title("About My Notepad")
        about.resizable(0, 0)
        about.geometry('300x300+120+120')
        about.iconbitmap(r'icon\about.ico')
        load = Image.open("icon\SD.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(about, image=render)
        img.image = render
        img.place(x=100, y=0)
        label=Label(about, text="This is a demo project \n Created by Sudipta Das \n "
                               "das.sudipta94@gmail.com-Contact me on this mail  \n")
        label.pack(side=BOTTOM)

    # word wrap section

    def word_wrap(self):
        if self.wrap.get():
            self.text_area.config(wrap=WORD)
        else:
            self.text_area.config(wrap=CHAR)
    # status bar

    def status_bar(self):
        if self.bar.get():
            self.status_frame.pack(side=LEFT)
        else:
            self.status_frame.pack_forget()

    # Editor settings

    def editors(self):
        self.editor = Toplevel()
        self.editor.title("Font and Background Settings")
        self.editor.resizable(0, 0)
        self.editor.geometry('500x180+120+120')
        self.editor.lift(aboveThis=self.master)
        self.editor.iconbitmap(r'icon\editor.ico')

        # font family label
        Label(self.editor, text="      Font Style").grid(row=0, column=1)

        # font family
        fonts = list(font.families())
        self.font_family_obj=Combobox(self.editor, value=fonts)
        self.font_family_obj.grid(row=0, column=2)
        self.font_family_obj.set(self.font_type)

        # create space
        Label(self.editor, text="    ").grid(row=1, column=1)
        Label(self.editor, text="    ").grid(row=1, column=2)

        # font size label
        Label(self.editor, text="       Font Size").grid(row=2, column=1)

        # font size
        size=list(range(1, 61))
        self.font_size_obj = Combobox(self.editor, value=size)
        self.font_size_obj.grid(row=2, column=2)
        self.font_size_obj.set(self.font_size)
        # font color label

        Label(self.editor, text="        Font colour").grid(row=0, column=3)
        # font color selector
        self.fg_selector = Button(self.editor, bg=self.font_color, width=5, command=self.choose_fg)
        self.fg_selector.grid(row=0, column=4)
        # create space

        Label(self.editor, text="    ").grid(row=1, column=3)
        Label(self.editor, text="    ").grid(row=1, column=4)

        # background color label
        Label(self.editor, text="        Background colour").grid(row=2, column=3)

        # background color selector
        self.bg_selector = Button(self.editor, bg=self.background_color, width=5, command=self.choose_bg)
        self.bg_selector.grid(row=2, column=4)

        # select button
        select=Button(self.editor, text="Select", command=self.set_font)
        select.place(x=320, y=150)
        select = Button(self.editor, text="Cancel", command=self.editor.destroy)
        select.place(x=400, y=150)

    def choose_fg(self):
        self.editor.destroy()
        clr = colorchooser.askcolor(title="choose")
        self.font_color=clr[1]
        self.editors()

    def choose_bg(self):
        self.editor.destroy()
        clr = colorchooser.askcolor(title="choose")
        self.background_color = clr[1]
        self.editors()

    def set_font(self):
        self.font_type=self.font_family_obj.get()
        self.font_size=self.font_size_obj.get()
        self.text_area.config(font=("{}".format(self.font_type), self.font_size),
                              bg=self.background_color, fg=self.font_color)
        self.editor.destroy()

    # save as
    def save_as(self):
        save_path = filedialog.asksaveasfile(mode='w+', defaultextension=".txt")
        if save_path:
            self.current_path = save_path.name
            save_path.write(self.text_area.get(1.0, END))
            save_path.close()
            self.last_save = True

    # save
    def save(self, event=None):
        if self.current_path == "":
            self.save_as()
        else:
            save_file = open(self.current_path, "w+")
            save_file.write(self.text_area.get(1.0, END))
            save_file.close()
            self.last_save = True

    # Open file
    def open(self, event=None):
        if not self.last_save:
            self.current_operation = 'Open'
            self.save_change()
        else:
            open_file = filedialog.askopenfile(initialdir="/", title="Select",
                                               filetypes=(("text files", ".txt"), ("all type", "*.*")))
            if open_file:
                self.current_path = open_file.name
                self.text_area.delete(1.0, END)
                print(self.current_path)
                for i in open_file:
                    self.text_area.insert(END, i)
            else:
                self.last_save = False

    # New file
    def new_file(self, event=None):
        if not self.last_save:
            self.current_operation = 'New'
            self.save_change()
        else:
            self.text_area.delete(1.0, END)

    # Quit program

    def exits(self):
        if not self.last_save:
            self.current_operation = 'Quit'
            self.save_change()
        else:
            self.master.quit()
    # Undo program

    def undoo(self, event=None):
        self.text_area.edit_undo()

    # Redo program
    def redoo(self, event=None):
        self.text_area.edit_redo()
    # make find frame visible

    def find_frame(self, event=None):
        self.find_frame.pack(side=LEFT)
    # make find frame invisible

    def find_frame_close(self):
        self.find_frame.pack_forget()
        self.text_area.tag_remove('found', '1.0', END)

    def find(self):
        self.text_area.tag_remove('found', '1.0', END)
        s = self.find_entry.get()
        if s:
            idx = '1.0'
            while 1:
                idx = self.text_area.search(s, idx, nocase=1, stopindex=END)

                if not idx:
                    break
                lastidx = '%s+%dc' % (idx, len(s))
                self.text_area.tag_add('found', idx, lastidx)
                idx = lastidx
            self.text_area.tag_config('found', foreground='red')
        self.find_entry.focus_set()
    # go to

    def goto(self):

        pass
    # copy function

    def copy(self, event=None):
        try:
            self.text_area.clipboard_clear()
            self.text_area.clipboard_append(self.text_area.selection_get())
        except:
            pass
    # cut function

    def cut(self, event=None):
        try:
            self.copy()
            self.text_area.delete("sel.first", "sel.last")
        except:
            pass
    #   paste function

    def paste(self, event=None):
        try:
            self.text_area.insert(INSERT, self.text_area.clipboard_get())
        except:
            pass

    # delete function
    def delete(self):
        self.text_area.delete("sel.first", "sel.last")

    # date and time function
    def date_time(self, event=None):
        now = datetime.now()
        self.text_area.insert(INSERT, now.strftime(" %d-%m-%Y  %H:%M %p"))

    # print file
    def printing(self, event=None):
        path = '\\temp.txt'
        f = open(path, mode='w+')
        f.write(self.text_area.get(1.0, END))
        os.startfile(path, "print")
        f.close()
        time.sleep(0.5)
        os.remove(path)

    def save_change(self):
        self.save_changes = Toplevel()
        self.save_changes.title(self.current_operation)
        self.save_changes.resizable(0, 0)
        self.save_changes.geometry('350x120+120+120')
        self.save_changes.config(bg="#e7dadb")
        self.save_changes.iconbitmap(r'icon\pop.ico')
        if not self.current_path=='':
            label1 = Label(self.save_changes, text="Do you want to save changes to\n{}"
                           .format(self.current_path), font=('Helvetica', 14), fg="#0e85ad", bg="#e7dadb")
        else:
            label1 = Label(self.save_changes, text="Do you want to save changes to Untitled",
                           font=('Helvetica', 14), fg="#0e85ad", bg="#e7dadb")
        label1.pack()
        save = Button(self.save_changes, text="Save", command=self.reset_save)
        dont_save = Button(self.save_changes, text="Don't Save", command=self.reset_dnt_save)
        cancel = Button(self.save_changes, text="Cancel", command=self.save_changes.destroy)
        save.pack(side=RIGHT, padx=5)
        dont_save.pack(side=RIGHT, padx=5)
        cancel.pack(side=RIGHT, padx=5)

    # popup save for change

    def reset_save(self):
        self.save_changes.destroy()
        if self.current_operation == 'Open':
            self.save()
            if self.last_save:
                self.open()
        elif self.current_operation == 'New':
            self.save()
            if self.last_save:
                self.new_file()
        elif self.current_operation == 'Quit':
            self.save()
            if self.last_save:
                self.exits()

    def reset_dnt_save(self):
        self.save_changes.destroy()
        if self.current_operation == 'Open':
            self.last_save = True
            self.open()
        elif self.current_operation == 'New':
            self.last_save = True
            self.new_file()
        elif self.current_operation == 'Quit':
            self.last_save = True
            self.exits()

    # pop save for change end
# end class

# Create Root window(Tk) object


Root = Tk()

# Create object of my_notepad class
ob = my_notepad(Root)
# Create loop
Root.mainloop()
