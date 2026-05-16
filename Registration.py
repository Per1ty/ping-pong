import customtkinter as ct


class Login(ct.CTk):
    def __init__(self):
        super().__init__()
        self.port = None
        self.host = None

        self.geometry("400x400")

        ct.CTkLabel(self, text='Підключення до гри',
                    font=('Georgia', 25)).pack(padx=10, pady=25, fill='x')
        self.entry_host = ct.CTkEntry(self, placeholder_text='HOST',
                                      font=('Georgia', 18),
                                      height=50)
        self.entry_host.pack(padx=10, fill='x')
        self.entry_port = ct.CTkEntry(self, placeholder_text='PORT',
                                      font=('Georgia', 18),
                                      height=50)
        self.entry_port.pack(padx=10, fill='x', pady=25)
        ct.CTkButton(self,
                     text='Підключитись',
                     font=("Georgia", 20),
                     height=50,
                     command=self.log).pack(padx=10, fill='x', pady=50)

    def log(self):
        self.host = self.entry_host.get()
        self.port = self.entry_port.get()
        try:

            self.port = int(self.port)
            self.destroy()
        except:
            self.entry_host.delete(0, ct.END)
            self.entry_port.delete(0, ct.END)