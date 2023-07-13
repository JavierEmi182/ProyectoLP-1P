import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

def file_chooser():
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
    showinfo(title="Import exitoso",message="El cuadro de texto contiene la información del archivo importado")
    text_arear.config(state='normal')
    text_arear.delete('1.0',tk.END)
    write_result("Codigo añadido.")
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
        title='Error!',message="No se ha podido cargar el código. Revisa el formato.")
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
    text_arear.delete('1.0','end')
    text_arear.config(state='normal')
    text_arear.insert(tk.INSERT, string)
    text_arear.config(state='disabled')

def lexer():
    text_arear.config(state='normal')
    text_arear.delete('1.0',tk.END)
    text_arear.config(state='disabled')
    import AnalisisLexico as lx
    datos_parse=text_area.get('1.0',tk.END)
    lx.lexer.input(datos_parse)
    ltok = lx.getTokens(lx.lexer)
    print("tokens")
    print(ltok)
    write_result("Tokens ({}):\n".format(len(ltok)))
    for i in ltok:
        i=str(i)+"\n"
        write_result(i)


def parser():
    
    text_arear.config(state='normal')
    text_arear.delete('1.0',tk.END)
    text_arear.config(state='disabled')
    import AnalisisSintactico as sn
    sn.listaerr = []
    datos_parse=text_area.get('1.0',tk.END)
    resultado = sn.parser.parse(datos_parse,tracking=True)
    error = sn.getErrors()
    text_arear.config(state='normal') 
    text_arear.delete('1.0',tk.END) 
    text_arear.config(state='disabled') 
    if len(error) > 0:
        resultado = error
        write_result("Resultados del analizador sintactico:\n")
        write_result(resultado)
    else:
        write_result("Resultados del analizador sintactico:\n")
        write_result("No se encontraron errores.")

    sn.listerr.clear()

def parser_sem():
    text_arear.config(state='normal')
    text_arear.delete('1.0',tk.END)
    text_arear.config(state='disabled')
    import AnalisisSemantico as sm   
    sm.listaerr = []
    datos_parse=text_area.get('1.0',tk.END)
    resultado = sm.parser.parse(datos_parse,tracking=True)
    error = sm.getErrors()
    text_arear.config(state='normal') 
    text_arear.delete('1.0',tk.END) 
    text_arear.config(state='disabled') 

    if len(error) > 0:
        resultado = error
        write_result("Resultados del analizador semantico:\n")
        write_result(resultado)
    else:
        write_result("Resultados del analizador semantico:\n")
        write_result("No se encontraron errores.")
    sm.listerr.clear()

#Ventana principal
mainwindow = tk.Tk()
mainwindow.geometry("1024x640")
mainwindow.resizable(False, False)
mainwindow.title("Analizador Swift")

#Contenedor superior
container1 = tk.Frame(mainwindow,height=200)
container1.config(bg="black")
tag_container1 = tk.Label(container1,text="Validar para Swift",font=("Arial",35),bg="black",fg="white").pack(anchor="w",side=tk.LEFT)
tag_group = tk.Label(container1, text="Grupo 3: Josseline Astudillo, Victor Peña, Javier Vergara", bg="orange",font=("Arial",15)).pack(side=tk.RIGHT,fill=tk.BOTH,padx=2, pady=15)


container1.pack(fill=tk.X,side=tk.TOP)

#Contenedor para parte inferior
contenedorinf = tk.Frame(mainwindow,height=768)
contenedorinf.config(bg="gray")
#Contenedor columna
container3 = tk.Frame(contenedorinf)
container3.config(bg="gray",width=100)
container3.pack(side=tk.LEFT,anchor="w")

contenedorinf.pack(fill=tk.BOTH)

#Contenedor central derecha
container2 = tk.Frame(contenedorinf)
container2.pack(fill=tk.BOTH)
container2.config(bg='gray')
container2_txt = tk.Frame(container2)
container2_but = tk.Frame(container2)
container2_but.config(bg="gray")
container2_res = tk.Frame(container2)

container2_txt.pack(side=tk.TOP,anchor="n")
container2_but.pack()
container2_res.pack(side=tk.BOTTOM,anchor="s")
container2.pack(side=tk.LEFT,anchor="n")

#Campos de texto y labels
labeltxt = tk.Label(container2_txt,text="Código Fuente :", bg="#7E82C4",font=("Arial",20)).pack(side=tk.TOP,anchor="n",fill=tk.X)
text_area = scrolledtext.ScrolledText(container2_txt, bg="lavender",
                                      wrap = tk.WORD, 
                                      width = 145,
                                      height = 10, 
                                      font = ("Arial",
                                              12), state='normal')
text_area.pack(anchor="n")
labeltxt = tk.Label(container2_res,text="Resultado :", bg="#FF8000",font=("Arial",20)).pack(side=tk.TOP,anchor="n",fill=tk.X)
text_arear = scrolledtext.ScrolledText(container2_res, bg='#FDD99C',
                                      wrap = tk.WORD, 
                                      width = 145,
                                      height = 12, 
                                      font = ("Arial",12),state ='disabled')
text_arear.pack(anchor="s")

#Contenedor para analizadores
labelactions = tk.Label(container2_but, text='Análisis disponibles : ',bg='gray',padx=50,pady=5 ,font=('Arial bold',18)).pack(side=tk.TOP)
button_lex = tk.Button(container2_but,bg="dark cyan", text="Análisis léxico", command=lambda: lexer(),font=('Arial',11), padx=65,pady=10).pack(pady=5,padx=15,side=tk.LEFT)
button_syn = tk.Button(container2_but,bg="dark cyan", text="Análisis sintáctico", command=lambda: parser(),font=('Arial',11), padx=50,pady=10).pack(pady=5,padx=15,side=tk.LEFT)
button_sem = tk.Button(container2_but,bg="dark cyan", text="Análisis semántico", command=lambda: parser_sem(),font=('Arial',11), padx=45,pady=10).pack(pady=5,padx=15,side=tk.LEFT)


#Contenedor para acciones
labelactions1 = tk.Label(container3,width=4, text='Acciones',bg='gray',padx=30 ,font=('Arial bold',22)).pack()
labelactions2 = tk.Label(container3,height=1,width=4, text='disponibles: ',bg='gray',padx=55 ,font=('Arial bold',22)).pack()
botonupload = tk.Button(container3,height=1,width=4, text="Borrar reporte",bg='#788199',fg='white', command=delete_content, padx=85,pady=40,font=("Arial",15)).pack(padx=15,pady=20)
botonupload = tk.Button(container3,height=1,width=4,text='Importar Archivo',bg='#788199',fg='white',command=file_chooser, padx=85,pady=40,font=("Arial",15)).pack(padx=15,pady=20)

mainwindow.mainloop()


