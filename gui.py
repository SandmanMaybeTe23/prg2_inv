import tkinter
main = tkinter.Tk()

from inv import inv, item
Inv= inv()


##main.geometry("500x400")
main.configure(background="purple")

label = tkinter.Label(main, text="hello world")
label.pack()


input_box= tkinter.Entry(main)
input_box.pack()


def log(event = None):
    for item in Inv.get_contents():
        textbox.insert(tkinter.END, item.name + "\n")


def create_add(event = None):
    item_name = input_box.get
    Inv.add_item(item(item_name,9,23,9))


button= tkinter.Button(main, text="Click Me now", width=20 , height=20 ,command=create_add)
button.pack(pady=20)


log_button = tkinter.Button(main,text= "show me item", command=log)
log_button.pack(pady = 20)

textbox= tkinter.Text(main, height=10, width=50)
textbox.pack(pady=20)



main.mainloop()