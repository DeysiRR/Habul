from guizero import App, Text, yesno, info

app = App(title="Habul", width=500, height=200, bg="white")
app.tk.resizable(False, False)

app.tk.iconbitmap("Imagenes/logo.ico")
# logo=Picture(app, image="Imagenes/habul.png", align="top", width=80, height=80)
message = Text(app, text="Traductor de lengua de señas a texto", size=10, font="times new roman", color="black", align="top", width=50, height=3)
app.display()
