from guizero import App, Picture, PushButton,yesno, info

def minimizar():
    if yesno("Minimizar", "¿Estás seguro de que quieres minimizar la aplicación?"):
        app.minimize()
    else:
        info("Minimizar", "Has cancelado la minimización")

app=App(title="Habul", width=300, height=300)
logo=Picture(app, image="Imagenes/habul.png", align="top")
boton=PushButton(app, text="Minimizar", command=minimizar, align="bottom")
app.display()