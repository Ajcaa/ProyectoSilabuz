import csv
from csv import *
import pandas as pd

file_libro = "libros.csv"
cant_max_libro = 1
cant_column = 6
cant_row = 3

class Libro:
           
    def __init__(self,id,titulo,genero,isbn,editorial,autor):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.editorial = editorial
        self.autor = autor
    
    def readFile(self):
        with open(file_libro, encoding='utf-8-sig') as file:
            fileLibro = csv.reader(file)
            

            for i in fileLibro:
                print (i[1:5])


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


    def searchFile(self):
        datos = pd.read_csv(file_libro)
        title = datos['Titulo']
        ISBN_book = datos['ISBN']
        
        search = int(input("Elija una opcion de busqueda de informacion de  libros: \n1) Por Titulo \n2) Por ISBN\n  "))

        if search == 1: 
            print('Tenemos los siguientes libros:', '\n', title)
            search_book = input("Ingrese el titulo de un libro:  ").capitalize()             
            fortitulo = datos[datos['Titulo'] == search_book]
            print(fortitulo.head())
        if search == 2:
            print('Tenemos los siguientes ISBN:  ', '\n', ISBN_book)
            search_ISBN = input('Ingresa el ISBN de un libro:  ')
            forISBN = datos[datos['ISBN'] == search_ISBN]
            print(forISBN.head())





    def searchFile7(self):
        datos = pd.read_csv(file_libro)
        author = datos['Autor(es)']
        editorial = datos['Editorial']
        genre = datos['Genero']

        search7 = int(input("Elija una opcion de busqueda de informacion de  libros: \n1) Por autor \n2) Por editorial \n3) Por genero\n"))
        if search7 == 1:
            print('Tenemos los siguientes ISBN:  ', '\n', author)
            search7_book = input('Ingrese el autor de un libro:  ').title()
            forAuthor = datos[datos['Autor(es)'] == search7_book]
            print(forAuthor.head())

        if search7 == 2:
            print('Tenemos los siguientes ISBN:  ', '\n', editorial)
            search7_book = input('Ingrese la editorial:  ')
            forEditorial = datos[datos['Editorial'] == search7_book]
            print(forEditorial.head())

        if search7 == 3:
            print('Tenemos los siguientes ISBN:  ', '\n', genre)
            search7_book = input('Ingrese el genero:  ').capitalize()
            forGenre = datos[datos['Genero'] == search7_book]
            print(forGenre.head())


    def discoDuro(self):
        save_book = input("Elija un formato para guardar tus libros" "\n1) csv 2) txt)  ")
        if save_book == "1":
            bookcsv = pd.read_csv(file_libro, on_bad_lines='skip')
            namecsv = input("Ingrese un nombre para el nuevo archivo en csv:  ")
            bookcsv.to_csv(f'{namecsv}.csv')
            print('El archivo', namecsv, 'ha sido creado')

        if save_book == "2":
            bookcsv = pd.read_csv(file_libro, on_bad_lines='skip')
            nametxt = input("Ingrese un nombre para el nuevo archivo en txt:  ")
            bookcsv.to_csv(f'{nametxt}.txt')
            print('El archivo', nametxt, 'ha sido creado')




print(Libro.readFile(file_libro))
print(Libro.orderFile(file_libro))
print(Libro.searchFile(file_libro))
print(Libro.searchFile7(file_libro))
print(Libro.discoDuro(file_libro))
print(Libro.addFile(file_libro))