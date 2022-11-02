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
            
            #data = [i for i in fileLibro]
            #print(data)
            for i in fileLibro:
                print (i[1:5])
            
            #cont = 0
            """
            for i in fileLibro:
                for j in range(cant_column):
                    #print("\n"+i[j],end='')
                    print(i[j]+"     ",end=' ')
                    #print("\n")
                #cont += 1
                #print(i)
            """
            #print (fileLibro)
            #print(file.read())
    
    """
    def readFile(self):
        with open(file,'r') as file:
            libros = csv.reader(file)
            for i in libros:
                print(i)
    """

print(Libro.readFile(file_libro))