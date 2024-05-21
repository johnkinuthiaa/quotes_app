import random
import requests
from tkinter import *
import json


def get_new_quote():
    api_url =("https://api.api-ninjas.com/v1/quotes?category ={}")
    
    response =requests.get(api_url,headers={'X-Api-Key':"use your api key from api ninjas"})
    response.raise_for_status()
    data =json.loads(response.text)
    
    for dict_item in data:
        new_quote = dict_item["quote"]
        author =dict_item["author"]
    label.config(text=author,fg="blue",font=("Yrsa SemiBold",25))
    canvas.itemconfig(quote_text, text=new_quote)

window =Tk()
window.config(bg="white")

canvas = Canvas(width=1040, height=1040,bg="white",highlightthickness=0)
quotes_img =PhotoImage(file="button.png")
canvas.create_image(659,610,image=quotes_img)

quote_text = canvas.create_text(520,290, text="",fill="blue",font=("Yrsa SemiBold",25),width=300)
canvas.grid(column=1,row=1)


button =Button(text="new qoute",fg="black",command=get_new_quote)
button.grid(column=0,row=0,padx=10,pady=10)

label =Label(text="")
label.grid(column=1,row=0)



window.mainloop()


