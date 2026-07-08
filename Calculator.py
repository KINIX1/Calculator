import customtkinter as ctk

calculator = ctk.CTk()
calculator.title("Calculator")
calculator.geometry("1500x900")
calculator.configure(fg_color = "white")

#калькулятор на головному екрані          //////////////////

BG_calculator = ctk.CTkFrame( 
    calculator,
    width = 1000,
    height = 1000,
    fg_color="#DBE0E0",
    corner_radius = 50
)
BG_calculator.place(x=250, y=50)

BG_calculator = ctk.CTkFrame( # фрейм де написано "калькулятор"
    calculator,
    width = 850,
    height = 200,
    fg_color="#A9A9A9",
    corner_radius = 50,
    bg_color="#DBE0E0"
)
BG_calculator.place(x=325, y=100)

text = ctk.CTkLabel(
    calculator,
    text="CALCULATOR",
    font=("Zen Dots", 90, "bold"),
    text_color = "#DADADA",
    fg_color = "#A9A9A9"

)
text.pack(pady=20)
text.place(x=345, y=150)

BG_calculator = ctk.CTkFrame(  #фрейм на якому розміщені кнопки 
    calculator,
    width = 850,
    height = 525,
    fg_color="#A9A9A9",
    corner_radius = 50,
    bg_color="#DBE0E0"
)
BG_calculator.place(x=325, y=350)



BG_calculator = ctk.CTkButton(  #КНОПКА CALCULATE
    calculator,
    width = 500,
    height = 100,
    fg_color="#DADADA",
    corner_radius = 50,
    bg_color="#A9A9A9",
    hover_color = "#777777",
    text = "CALCULATE",
    font = ("Zen Dots", 55, "bold"),
    text_color = "#A9A9A9"
)
BG_calculator.place(x=350, y=375) 


BG_calculator = ctk.CTkButton(  #КНОПКА SETTINGS
    calculator,
    width = 500,
    height = 100,
    fg_color="#DADADA",
    corner_radius = 50,
    bg_color="#A9A9A9",
    hover_color = "#777777",
    text = "SETTINGS",
    font = ("Zen Dots", 55, "bold"),
    text_color = "#A9A9A9"
)
BG_calculator.place(x=650, y=500)

BG_calculator = ctk.CTkButton(  #КНОПКА EXIT
    calculator,
    width = 500,
    height = 100,
    fg_color="#DADADA",
    corner_radius = 50,
    bg_color="#A9A9A9",
    hover_color = "#777777",
    text = "EXIT",
    font = ("Zen Dots", 55, "bold"),
    text_color = "#A9A9A9"
)
BG_calculator.place(x=350, y=625)



BG_calculator = ctk.CTkButton(  #КНОПКА 4
    calculator,
    width = 250,
    height = 100,
    fg_color="#DADADA",
    corner_radius = 50,
    bg_color="#A9A9A9",
    hover_color = "#777777",
    text = "3",
    font = ("Zen Dots", 55, "bold"),
    text_color = "#A9A9A9"
)
BG_calculator.place(x=900, y=375) 

BG_calculator = ctk.CTkButton(  #КНОПКА 9
    calculator,
    width = 250,
    height = 100,
    fg_color="#DADADA",
    corner_radius = 50,
    bg_color="#A9A9A9",
    hover_color = "#777777",
    text = "9",
    font = ("Zen Dots", 55, "bold"),
    text_color = "#A9A9A9"
)
BG_calculator.place(x=900, y=625)

BG_calculator = ctk.CTkButton(  #КНОПКА 5
    calculator,
    width = 250,
    height = 100,
    fg_color="#DADADA",
    corner_radius = 50,
    bg_color="#A9A9A9",
    hover_color = "#777777",
    text = "4",
    font = ("Zen Dots", 55, "bold"),
    text_color = "#A9A9A9"
)
BG_calculator.place(x=350, y=500)



BG_calculator = ctk.CTkButton(  #КНОПКА +
    calculator,
    width = 181.25,
    height = 100,
    fg_color="#DADADA",
    corner_radius = 50,
    bg_color="#A9A9A9",
    hover_color = "#777777",
    text = "+",
    font = ("Zen Dots", 55, "bold"),
    text_color = "#A9A9A9"
)
BG_calculator.place(x=350, y=750)

BG_calculator = ctk.CTkButton(  #КНОПКА -
    calculator,
    width = 181.25,
    height = 100,
    fg_color="#DADADA",
    corner_radius = 50,
    bg_color="#A9A9A9",
    hover_color = "#777777",
    text = "-",
    font = ("Zen Dots", 55, "bold"),
    text_color = "#A9A9A9"
)
BG_calculator.place(x=556.25, y=750)

BG_calculator = ctk.CTkButton(  #КНОПКА *
    calculator,
    width = 181.25,
    height = 100,
    fg_color="#DADADA",
    corner_radius = 50,
    bg_color="#A9A9A9",
    hover_color = "#777777",
    text = "×",
    font = ("Zen Dots", 55, "bold"),
    text_color = "#A9A9A9"
)
BG_calculator.place(x=762.5, y=750)


BG_calculator = ctk.CTkButton(  #КНОПКА /
    calculator,
    width = 181.25,
    height = 100,
    fg_color="#DADADA",
    corner_radius = 50,
    bg_color="#A9A9A9",
    hover_color = "#777777",
    text = "÷",
    font = ("Zen Dots", 55, "bold"),
    text_color = "#A9A9A9"
)
BG_calculator.place(x=968.75, y=750)
















calculator.mainloop()