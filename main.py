# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']





    password_list = [choice(letters) for a in range(randint(8, 10))] + [choice(symbols) for b in range(randint(2, 4))] + [choice(numbers) for c in range(randint(2, 4))]

    shuffle(password_list)

    passcode = "".join(password_list)
    pyperclip.copy(passcode)

    password_input.delete(0, END)
    password_input.insert(0,f"{passcode}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_input.get()
    username = username_input.get()
    passwords = password_input.get()
    new_data = {
        web: {
            "email": username,
            "password": passwords,
        }
    }

    if len(web) <= 0 or len(username) <= 0 or len(passwords) <= 0:
        messagebox.showwarning(title="Invalid Input", message="Please correct empty fields.")
        return

    is_ok = messagebox.askokcancel(title=web, message=f"The information entered: \nEmail: {username} "
                                                      f"\nPassword: {passwords} \nIs it ok to save?")
    try:
        with open ("data.json", "r") as file:



            if is_ok:
                #Reading old data
                data = json.load(file)
                #Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
                    web_input.delete(0, END)
                    # username_input.delete(0, END)
                    password_input.delete(0, END)

    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
            web_input.delete(0, END)
            # username_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- SEARCH --------------------------------- #
def find_password():
    web = web_input.get()
    username = username_input.get()
    passwords = password_input.get()

    if len(web.strip()) <= 0:
        messagebox.showwarning(title="Invalid Input", message="Please correct empty fields.")
        return
    try:
        with open("data.json", "r") as file:
            result = json.load(file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found.")
    else:
            key_results = {key: value for key, value in result.items() if web.lower() in key.lower()}
            if not key_results:
                messagebox.showinfo(title="No Results", message="No matching website found.")
            else:
                for key, value in key_results.items():
                    messagebox.showinfo(title=key, message=f"Email: {value['email']}\nPassword: {value['password']}")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "email@example.com")

password = StringVar()
password_input = Entry(width=21, textvariable=password, show="*")
password_input.grid(column=1, row=3)

generate_pass = Button(text="Generate Password", command=pass_gen)
generate_pass.grid(column=2, row=3)

search = Button(text="Search", width=15, command=find_password)
search.grid(column=3, row=1)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()
