import customtkinter

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.geometry("500x350")

#
# def login():
#     print("Test")
#
#
# frame = ctk.CTkFrame(master=root)
# frame.pack(pady=20, padx=60, fill="both", expand=True)
#
# label = ctk.CTkLabel(master=frame, text="Login System", text_font=("Roboto", 24))
# label.pack(pady=12, padx=10)
#
# button = ctk.CTkButton(master=frame, text="login", command=login)
# button.pack(pady=12, padx=10)
#
# checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me")
# checkbox.pack(pady=12, padx=10)

window.mainloop()
