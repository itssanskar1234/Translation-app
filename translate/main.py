import customtkinter # Importing customtkinter module
from googletrans import Translator,LANGUAGES # Importing Translator class and LANGUAGES dictionary from googletrans module
from tkinter.ttk import Combobox # Importing Combobox class from tkinter.ttk module
from tkinter import messagebox as tmsg # Importing messagebox submodule as tmsg from tkinter module

class Ui(customtkinter.CTk):
    def __init__(self):
        super().__init__()

    def ui(self):
        '''Method to create the user interface.'''

        # Create the main frame
        Main_frame  = customtkinter.CTkFrame(master=self)
        Main_frame.place(x=0,y=0)

         # Create arrows label
        arrows = customtkinter.CTkLabel(master=Main_frame,text="→\n←",font=("Verdana",12,'bold'))
        arrows.place(x=393,y=10)

        # Frame for combobox 1 
        select_box_1 = customtkinter.CTkFrame(master=Main_frame)
        select_box_1.grid(row=0,column=0,pady=10)
        
        # Frame for combobox 2
        select_box_2 = customtkinter.CTkFrame(master=Main_frame)
        select_box_2.grid(row=0,column=1)

        # Get language list
        lang_list = []
        for lang in LANGUAGES.values():
            lang_list.append(lang)

        # Create combobox for selecting 'from' language
        self.from_  = Combobox(master=select_box_1,font=('Verdana',20),width=10,values=lang_list,state='readonly',justify='center')
        self.from_.set("english")
        self.from_.grid(row=0,column=0,padx=20)

        # Create combobox for selecting 'to' language
        self.to_  = Combobox(master=select_box_2,font=('Verdana',20),width=10,values=lang_list,state='readonly',justify='center')
        self.to_.set('hindi')
        self.to_.grid(row=0,column=0,padx=20)
        
        # Create text field 1 for input
        self.text_field_1 = customtkinter.CTkTextbox(master= Main_frame,width=300,height=200,font=('Verdana',20),fg_color='Silver',text_color='black')
        self.text_field_1.grid(row=1,column=0,padx=50,pady=45)

        # Create text field 2 for output
        self.text_field_2 = customtkinter.CTkTextbox(master= Main_frame,width=300,height=200,font=('Verdana',20),fg_color='Silver',text_color='black')
        self.text_field_2.grid(row=1,column=1,padx=50)

        # Create translate button
        Translate_Button = customtkinter.CTkButton(master=Main_frame,text="Translate",font=('Verdana',15),command=self.Translate,width=10)
        Translate_Button.place(x=358,y=310)



class Logic(Ui):
    def __init__(self):
        super().__init__()
    def Translate(self):
        """Method to translate text."""

        if self.from_.get() == self.to_.get():
            tmsg.showerror("Error","You select same languages")

        else:
            text_to_translate = self.text_field_1.get("1.0",customtkinter.END)

            for key,val in LANGUAGES.items():
                if val == self.from_.get():
                    from_translate = key
                if val == self.to_.get():
                    to_translate = key


            def translate_logic(text,target_language=from_translate):
                    """Internal method for translation logic."""
                    translator = Translator()
                    translating = translator.translate(text,dest=target_language)
                    return translating.text
            try:
                self.translated_text = translate_logic(text_to_translate,target_language=to_translate)
                self.display_translated_text()            
            except Exception:
                pass 
            

    def display_translated_text(self):
        """Method to display translated text."""
        self.text_field_2.delete("1.0",customtkinter.END)
        self.text_field_2.insert("1.0",self.translated_text)


            
class Gemometry(Logic):
    def __init__(self,width,height):
        super().__init__()
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        self.width = width 
        self.height = height

        x  = (self.winfo_screenwidth() - self.width)//2
        y  = (self.winfo_screenheight() - self.height)//2

        self.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.resizable(False,False)


if __name__ == "__main__":
    translator = Gemometry(800,350)
    translator.ui()
    translator.mainloop()