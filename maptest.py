from tkinter import*

T =Tk()
T.mainloop()


def InitSortListBox():
    global SortListBox

    SortListBoxScrollbar = Scrollbar(g_Tk)

    SortListBoxScrollbar.pack()

    SortListBoxScrollbar.place(x=150, y=160)

    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')

    SortListBox = Listbox(g_Tk, font=TempFont, activestyle='none',

                          width=10, height=1, borderwidth=12, relief='ridge',

                          yscrollcommand=SortListBoxScrollbar.set)

    SortListBox.insert(1, "시설명")

    SortListBox.insert(2, "주소")

    SortListBox.insert(3, "연락처")

    SortListBox.pack()

    SortListBox.place(x=10, y=160)

    SortListBoxScrollbar.config(command=SortListBox.yview)


InitSortListBox()