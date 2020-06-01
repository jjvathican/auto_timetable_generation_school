import tkinter as tk   # python3


TITLE_FONT = ("Helvetica", 18, "bold")

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (login, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("login")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def check(self):
        print('hai')
        self.show_frame("PageOne")

class login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="login page")
        label.pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self, text="username:")
        label2 = tk.Label(self, text="password:")
        label1.grid(row=0,column=0)
        label2.grid(row=1, column=0)

        label1.pack()
        label2.pack()

        button1 = tk.Button(self, text="login",
                            command=lambda: controller.check())#show_frame("PageOne"))
        button2 = tk.Button(self, text="signup",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("login"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # self.builder  = pygubu.Builder()
        # self.builder.add_from_file('f:\helloworld.ui')
        #self.mainwindow = builder.get_object('mainwindow')


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()