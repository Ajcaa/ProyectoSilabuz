import csv
from csv import *
import pandas as pd

file_libro = "libros.csv"
cant_max_libro = 1
cant_column = 6
cant_row = 3
play = True

class Libro:
           
    def __init__(self,id,titulo,genero,isbn,editorial,autor):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.editorial = editorial
        self.autor = autor
    

    #-------OPCION 2------#
    def readFile(self):
        with open(file_libro, encoding='utf-8-sig') as file:
            fileLibro = csv.reader(file)
            

            for i in fileLibro:
                print (i[0:6])

    #-------OPCION 3------#
    def addFile(self):

        new_list = [] 
        with open(file_libro, "a", newline="") as file:
            
                      
            new_file = writer(file)
            
            u = input("Agregue una ID para el nuevo libro:  ").upper()
            new_list.append(u)            


            v = input("Agregue un titulo para el nuevo libro:  ")
            new_list.append(v)
                    
            w =input("Agregue un genero para el nuevo libro:  ")
            new_list.append(w)

            x =input("Agregue un ISBN para el nuevo libro:  ")
            new_list.append(x)

            y = input("Agregue un editoral para el nuevo libro:  ")
            new_list.append(y)

            z = input("Agregue un(os) autores para el nuevo libro:  ")
            new_list.append(z)


            new_file.writerow(new_list)
            print("         -------------------------------Se agrego un nuevo libro-------------------------------")
            file.close()


    #-------OPCION 4------#
    def deleteFile(self):
        
        df = pd.read_csv(file_libro,on_bad_lines='skip')
        print("         ----------------------------------Libros actuales----------------------------------")
        print(df)
        cual = input('Elija que libro eliminar por id:  ')

        
        df.set_index("Id", inplace=True)
        df = df.drop(cual)
        df.to_csv(file_libro,)
        print("         ----------------------------Se ha elimado el libro. Libros actuales----------------------------")
        print(df)







    #-------OPCION 6------#
    def orderFile(self):        
        with open(file_libro, encoding='utf-8-sig') as file:
            next(file)
            fileLibro = csv.reader(file)

            lista = []
            for row in fileLibro:
                if row[1]:
                    lista.append(row[1])    
                    lista.sort()
            h = input("Pulse Enter para ver los libros ordenados:  ")
            print(lista)
            file.close()

    #-------OPCION 5------#
    def searchFile(self):
        datos = pd.read_csv(file_libro)
        title = datos['Titulo']
        ISBN_book = datos['ISBN']
        
        search = int(input("Elija una opcion de busqueda de informacion de  libros: \n1) Por Titulo \n2) Por ISBN\n  "))

        if search == 1: 
            print('Tenemos los siguientes titulos de libros:', '\n', title.to_string())
            search_book = input("Ingrese el titulo de un libro:  ").capitalize()             
            fortitulo = datos[datos['Titulo'] == search_book]
            print(fortitulo.head())
        if search == 2:
            print('Tenemos los siguientes ISBN:  ', '\n', ISBN_book.to_string())
            search_ISBN = input('Ingresa el ISBN de un libro:  ').upper()
            forISBN = datos[datos['ISBN'] == search_ISBN]
            print(forISBN.head())




    #-------OPCION 7------#
    def searchFile7(self):
        datos = pd.read_csv(file_libro)
        author = datos['Autor(es)']
        editorial = datos['Editorial']
        genre = datos['Genero']

        search7 = int(input("Elija una opcion de busqueda de informacion de  libros: \n1) Por autor \n2) Por editorial \n3) Por genero\n"))
        if search7 == 1:
            print('Tenemos los siguientes autores:  ', '\n', author.to_string())
            search7_book = input('Ingrese el autor de un libro:  ').title()
            forAuthor = datos[datos['Autor(es)'] == search7_book]
            print(forAuthor.head())

        if search7 == 2:
            print('Tenemos los siguientes editoriales:  ', '\n', editorial.to_string())
            search7_book = input('Ingrese la editorial:  ').title()
            forEditorial = datos[datos['Editorial'] == search7_book]
            print(forEditorial.head())

        if search7 == 3:
            print('Tenemos los siguientes generos:  ', '\n', genre.to_string())
            search7_book = input('Ingrese el genero:  ').capitalize()
            forGenre = datos[datos['Genero'] == search7_book]
            print(forGenre.head())


    #-------OPCION 9------#
    def editFile(self):
        df = pd.read_csv(file_libro) 

        valId = input("Ingrese que libro actualizar por ID:  ")

        valTitle =  input("Ingrese el nuevo titulo:  ").capitalize()
        df.loc[df['Id'] == valId, "Titulo"] = valTitle

        valGenre =  input("Ingrese el nuevo genero:  ").capitalize()
        df.loc[df['Id'] == valId, "Genero"] = valGenre

        valISBN =  input("Ingrese el nuevo ISBN:  ").upper()
        df.loc[df['Id'] == valId, "ISBN"] = valISBN

        valEditorial =  input("Ingrese la nueva editorial:  ").title()
        df.loc[df['Id'] == valId, "Editorial"] = valEditorial

        valAutor =  input("Ingrese el nuevo autor :  ").title()
        df.loc[df['Id'] == valId, "Autor(es)"] = valAutor

        
        df.to_csv(file_libro, index=False)
        print("Se actualizo el libro")






    #-------OPCION 10------#
    def discoDuro(self):
        save_book = input("Elija un formato para guardar tus libros" "\n1) csv 2) txt)  ")
        if save_book == "1":
            bookcsv = pd.read_csv(file_libro, on_bad_lines='skip')
            namecsv = input("Ingrese un nombre para el nuevo archivo en csv:  ")
            bookcsv.to_csv(f'{namecsv}.csv', index=False)
            print('El archivo', namecsv, 'ha sido creado')

        if save_book == "2":
            bookcsv = pd.read_csv(file_libro, on_bad_lines='skip')
            nametxt = input("Ingrese un nombre para el nuevo archivo en txt:  ")
            bookcsv.to_csv(f'{nametxt}.txt', index=False)
            print('El archivo', nametxt, 'ha sido creado')




while play:
    print("""
                        Opción 1: Leer archivo de disco duro (.txt o csv) que carga 3 libros.
                        Opción 2: Listar libros.
                        Opción 3: Agregar libro.
                        Opción 4: Eliminar libro.
                        Opción 5: Buscar libro por ISBN o por título.
                        Opción 6: Ordenar libros por título.
                        Opción 7: Buscar libros por autor, editorial o género.
                        Opción 8: Buscar libros por número de autores. 
                        Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).
                        Opción 10: Guardar libros en archivo de disco duro (.txt o csv).
    """)

    start = int(input("                    Elija un opcion:  "))

    while start not in(1,2,3,4,5,6,7,8,9,10):
        start = int(input("Elija una opcion valida:  "))


    if start == 1:
        print("Se ha leido el archivo libros.csv")
    if start == 2:
        Libro.readFile(file_libro)

    if start == 3:
        Libro.addFile(file_libro)

    if start == 4:   
        Libro.deleteFile(file_libro)

    if start == 5:
        Libro.searchFile(file_libro)

    if start == 6:
        Libro.orderFile(file_libro)

    if start == 7:
        Libro.searchFile7(file_libro)

    if start == 9:
        Libro.editFile(file_libro)

    if start == 10:
        Libro.discoDuro(file_libro)

    if start == 8:
        Libro.searchAuthorExtense(file_libro)

    continuee = input("Desea continuar? (Si/No):  ").lower()    
    if continuee != "si":
        print("Fin del programa")
        play = False