from tkinter import *

window=Tk()
window.title("Mile to Km converter")
window.minsize(200,100)

def convert():
    mile_num=int(number.get())
    new_km=mile_num*1.60934
    new_kmr=str(round(new_km,2))
    out.config(text=new_kmr)




#label (Miles)
label_1=Label(text="Miles")
label_1.grid(row=0,column=2)

#label(is equal to)
label_2=Label(text="is equal to")
label_2.grid(row=1,column=0)

#label (km)
label_3=Label(text="Km")
label_3.grid(row=1,column=2)

#button
button=Button(text="Convert",command=convert)
button.grid(row=2,column=1)

#entry
number=Entry(width=10)
number.grid(row=0,column=1)
number.get()

#print the output label
out=Label(text="0")
out.grid(row=1,column=1)




window.mainloop()
