import csv

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
            
    def orderFile(self):        
        with open(file_libro, encoding='utf-8-sig') as file:
            next(file)
            fileLibro = csv.reader(file)

            lista = []
            for row in fileLibro:
                if row[1]:
                    lista.append(row[1])    
                    lista.sort()
            print(lista)
            file.close()

print(Libro.readFile(file_libro))
print(Libro.orderFile(file_libro))