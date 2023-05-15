from tkinter import * 
root = Tk()
root.geometry("600x400")
root.title("Private Variable Login Page") 

name_label = Label(root, text = "Name: ")
name_label.place(relx = 0.3, rely = 0.2, anchor = CENTER)

name_input = Entry(root)
name_input.place(relx = 0.5, rely = 0.2, anchor = CENTER)

password_label = Label(root, text = "Password: ")
password_label.place(relx = 0.3, rely = 0.3, anchor = CENTER)

password_input = Entry(root)
password_input.place(relx = 0.5, rely = 0.3, anchor = CENTER)

captcha_label = Label(root, text = "Captcha: ")
captcha_label.place(relx = 0.3, rely = 0.4, anchor = CENTER)

captcha_input = Entry(root)
captcha_input.place(relx = 0.5, rely = 0.4, anchor = CENTER)

updated_name = Label(root)
updated_name.place(relx = 0.4, rely = 0.6, anchor = CENTER)

updated_password = Label(root)
updated_password.place(relx = 0.4, rely = 0.7, anchor = CENTER)
 
updated_captcha = Label(root)
updated_captcha.place(relx = 0.4, rely = 0.8, anchor = CENTER)

class userDB:
    def __init__(self):
        self.__username = "Rohan"
        self.__password = "rohan12@34"
        self.captcha = "_r_0901"
        
    def showUser(self):
        updated_name["text"] = "Name: " + self.__username
        updated_password["text"] = "Password: " + self.__password
        updated_captcha["text"] = "Captcha: " + self.captcha

user = userDB()

def addUser():
    global user 
    user.username = name_input.get()
    user.password = password_input.get()
    user.captcha = captcha_input.get()
    print("Details Updated")  

btn_update_details = Button(root, text = "Update Login Details", command = addUser)
btn_update_details.place(relx = 0.3, rely = 0.5, anchor = CENTER)
btn_show_profile = Button(root, text = "Show Profile", command = user.showUser)
btn_show_profile.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()