from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=230, height=170)

kg_text = Label(text="Enter Your Weight(kg)")
kg_text.config(pady=3)
kg_text.pack()

entry_kg = Entry()
entry_kg.pack()

cm_text = Label(text="Enter Your Height(cm)")
cm_text.config(pady=3)
cm_text.pack()

entry_cm = Entry()
entry_cm.pack()


def button_click():
    global result_text
    try:
        bmi = 10000 * (int(entry_kg.get()) / int(entry_cm.get()) ** 2)
        if bmi <= 18.5:
            result_text = "You BMI: {:.2f} You are Under Weight".format(bmi)
        elif 18.5 < bmi <= 24.9:
            result_text = "You BMI: {:.2f} You are Normal Weight".format(bmi)
        elif 25 < bmi <= 29.9:
            result_text = "You BMI: {:.2f} You are Over Weight".format(bmi)
        elif 30 <= bmi <= 34.9:
            result_text = "You BMI: {:.2f} You are obesity( Class 1 ) Weight".format(bmi)
        elif 35 <= bmi <= 39.9:
            result_text = "You BMI: {:.2f} You are Obesity( Class 2 ) Weight".format(bmi)
        elif bmi >= 40:
            result_text = "You BMI: {:.2f} You are Extreme Obesity Weight".format(bmi)
        text.config(text=result_text, pady=3)
    except:
        text.config(text="Enter valid numbers!")


button = Button(text="Calculate", command=button_click)
button.pack()
text = Label(text="")
text.pack()

window.mainloop()
