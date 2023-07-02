import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
#from PIL import ImageTk, Image

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

    open_file(filename)

def open_file(nomarch):
    file = open(nomarch,'r')
    global datos_parse
    datos_parse = file.read()
    file.close()
    file = open(nomarch,'r')
    text_area.delete('1.0',tk.END)
    for line in file:
        text_area.insert(tk.INSERT, line)
    showinfo(title="Importacion correcta!",message="Su codigo fuente ha sido agregado correctamente.")
    #datos_parse = file.read() #Para el analizador sintatcico
    text_arear.config(state='normal')
    text_arear.delete('1.0',tk.END)
    write_result("Codigo cargado y listo para analizar.")
    text_arear.config(state='disabled')

def delete_content():
    text_area.delete('1.0',tk.END)
    text_arear.config(state='normal')
    text_arear.delete('1.0',tk.END)
    text_arear.config(state='disabled')
    global input
    input = ""
    global datos_parse
    datos_parse = ""


#Guarda el contenido del textbox en un string
def save_content():
    global input
    input = text_area.get('1.0',tk.END)
    if input.strip() == "":
        showinfo(
        title='Error!',message="No se ha podido cargar el codigo. Revisa tu entrada!")
        return
    fileaux = open("fuente.txt","w")
    for elem in input:
        fileaux.write(elem)
    fileaux.close()
    open_file("fuente.txt")
    text_arear.config(state='normal')
    text_arear.delete('1.0',tk.END)
    write_result("Codigo cargado y listo para analizar.")
    text_arear.config(state='disabled')

#Escribe los resultados en el area de resultados
def write_result(string):
    text_arear.config(state='normal')
    text_arear.insert(tk.INSERT, string)
    text_arear.config(state='disabled')

def lexer():
    text_arear.config(state='normal')
    text_arear.delete('1.0',tk.END)
    text_arear.config(state='disabled')
    import AnalisisLexico as lx
    lx.lexer.input(datos_parse)
    ltok = lx.getTokens(lx.lexer)
    print("tokens")
    print(ltok)
    write_result("Tokens:\n")
    for i in ltok:
        i=str(i)+"\n"
        write_result(i)
   # write_result(ltok)


def parser():
    
    text_arear.config(state='normal')
    text_arear.delete('1.0',tk.END)
    text_arear.config(state='disabled')
    import AnalisisSintactico as sn
    sn.listaerr = []
    resultado = sn.parser.parse(datos_parse,tracking=True)
    error = sn.getErrors()
    text_arear.config(state='normal')
    text_arear.delete('1.0',tk.END)
    text_arear.config(state='disabled')
    if len(error) > 0:
        resultado = error
        write_result("Resultado del analizador sintactico:\n")
        write_result(resultado)
    else:
        write_result("Resultado del analizador sintactico:\n")
        write_result(str(resultado))

def parser_sem():
    text_arear.config(state='normal')
    text_arear.delete('1.0',tk.END)
    text_arear.config(state='disabled')
    import AnalisisSemantico as sm   
    sm.listaerr = []
    resultado = sm.parser.parse(datos_parse,tracking=True)
    error = sm.getErrors()
    if len(error) > 0:
        resultado = error
        write_result("Resultado del analizador semantico:\n")
        write_result(resultado)
    else:
        write_result("Resultado del analizador semantico:\n")
        write_result(str(resultado))


#Ventana principal
mainwindow = tk.Tk()
mainwindow.geometry("1280x720")
mainwindow.resizable(False, False)
mainwindow.title("Analizador Swift")
#Contenedores
#Contenedor para label y foto
contenedor1 = tk.Frame(mainwindow,height=200)
contenedor1.config(bg="black")
tag_contenedor1 = tk.Label(contenedor1,text="Validar para Swift",font=("Arial",35),bg="black",fg="white").pack(anchor="w",side=tk.LEFT)
####img = ImageTk.PhotoImage(Image.open("golang.png").resize((150,75), Image.LANCZOS))
####labelimg = tk.Label(contenedor1,image=img).pack(pady=0,anchor="ne",side=tk.RIGHT)


contenedor1.pack(fill=tk.X,side=tk.TOP)

#Contenedor para parte inferior
contenedorinf = tk.Frame(mainwindow,height=1080)
contenedorinf.config(bg="gray")
#Contenedor para textarea y boton confirmar editar
contenedor3 = tk.Frame(contenedorinf)
contenedor3.config(bg="gray")
contenedor3.pack(side=tk.LEFT,anchor="ne")

contenedorinf.pack(fill=tk.BOTH)

contenedor2 = tk.Frame(contenedorinf)
contenedor2_txt = tk.Frame(contenedor2)
contenedor2_but = tk.Frame(contenedor2)
contenedor2_but.config(bg="gray")
contenedor2_res = tk.Frame(contenedor2)

contenedor2_txt.pack(side=tk.TOP,anchor="n")
contenedor2_but.pack()
contenedor2_res.pack(side=tk.BOTTOM,anchor="s")
contenedor2.pack(side=tk.LEFT,anchor="n")

contenedor4 = tk.Frame(mainwindow)
contenedor4.config(bg="orange")
contenedor4.pack(fill=tk.BOTH)

#Campos de texto y labels
labeltxt = tk.Label(contenedor2_txt,text="Código Fuente", bg="#7E82C4",font=("Arial",20)).pack(side=tk.TOP,anchor="n",fill=tk.X)
text_area = scrolledtext.ScrolledText(contenedor2_txt, bg="lavender",
                                      wrap = tk.WORD, 
                                      width = 145,
                                      height = 13, 
                                      font = ("Arial",
                                              12), state='normal')
text_area.pack(anchor="n")
labeltxt = tk.Label(contenedor2_res,text="Resultado", bg="gray",font=("Arial",20)).pack(side=tk.TOP,anchor="n",fill=tk.X)
text_arear = scrolledtext.ScrolledText(contenedor2_res, 
                                      wrap = tk.WORD, 
                                      width = 145,
                                      height = 12, 
                                      font = ("Arial",12),state ='disabled')
text_arear.pack(anchor="s")

button_lex = tk.Button(contenedor2_but,bg="dark cyan", text="Análisis léxico", command=lambda: lexer(), padx=85,pady=15).pack(side=tk.LEFT)
button_syn = tk.Button(contenedor2_but,bg="dark cyan", text="Análisis sintáctico", command=lambda: parser(), padx=75,pady=15).pack(side=tk.LEFT)
button_sem = tk.Button(contenedor2_but,bg="dark cyan", text="Análisis semántico", command=lambda: parser_sem(), padx=75,pady=15).pack(side=tk.LEFT)


#Contenedor para analizadores

botonupload = tk.Button(contenedor3, text="Realizar Análisis", command=save_content, padx=85,pady=50,font=("Arial",10)).pack(pady=50)
botonupload = tk.Button(contenedor3, text="Borrar reporte", command=delete_content, padx=85,pady=50,font=("Arial",10)).pack()
botonupload = tk.Button(contenedor3,text='Importar Archivo',command=select_file, padx=85,pady=50,font=("Arial",10)).pack(pady=50)


#Contenedor para marca de agua

tag_group = tk.Label(contenedor4, text="Grupo 3: Josseline Astudillo, Victor Peña, Javier Vergara", bg="orange",font=("Arial",15)).pack(fill=tk.BOTH, pady=15)



mainwindow.mainloop()


