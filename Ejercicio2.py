
#Crear una clase <code>Biblioteca</code>. Una biblioteca es una colección homogénea y ordenada de libros (pueden utilizar una lista para representarla). 
#La clase debe contener métodos para facilitar:
#
#    - Crear una biblioteca vacía. (DONE)
#    - Identificar si una biblioteca está vacía o no. (DONE)
#    - Añadir y remover libros de la biblioteca.


class Biblioteca():

    def __init__(self):
        self.coleccion = None # remplazar por [] ó ListaEnlazada()

    def es_Vacia(self):
        return len(self.coleccion) == 0

    def aniadir(self, item):
        if es_Vacia(self.coleccion):
            self.coleccion.append(item)
        if type(item) != 'Libro': #podemos reemplazar 'Libro' type(self.coleccion.index(0))
            raise ValueError('el item no es del tipo de la coleccion')
        else:
            # el orden es FIFO
            self.coleccion.append(item)
            
    def remover(self, item): 
        if es_Vacia(self.coleccion):
            raise ValueError('la biblioteca esta vacia')
        #if item in self.coleccion:
            #self.coleccion.remove(item) 
        for x in range(0, len(self.colecion) - 1 ):
            if x == item:
                self.coleccion.remove(item) 

    def leer_primer_libro(self): 
        if not es_Vacia(self.coleccion):
            return self.coleccion[0]
        else:
            raise ValueError('la biblioteca esta vacia')
         

    def leer_ultimo_libro(self):
        if not es_Vacia(self.coleccion):
            return self.coleccion[-1] #hay que Cambiar por
                                        # self.coleccion.index(len(self) -1 )
        else:
            raise ValueError('la biblioteca esta vacia')

    def insertar_al_principio(self, item): 
        if es_Vacia(self.coleccion):
            self.coleccion.aniadir(item)
        if type(item) != 'Libro':
            raise ValueError('el item no es del tipo de la coleccion')
        else:
            self.coleccion.insert(0, item)

    def agregar_al_final(self, item):
        #self.coleccion.aniadir(item) 
        if es_Vacia(self.coleccion):
            self.coleccion.aniadir(item)
        if type(item) != 'Libro':
            raise ValueError('el item no es del tipo de la coleccion')
        else:
            self.coleccion.append(item)
        
    def __len__(self):
        return len(self.coleccion) - 1

    def __str__(self):
        #for x in range():
        #    string += self.coleccion[x]
        return str(self.coleccion) #return string 

    def __eq__(self, other):
        if type(other) != type(self): # type(Biblioteca)
            #raise ValueError('other no es del tipo de la coleccion')
            return NotImplemented  
        return self.coleccion == other.coleccion 

    def __add__(self, other):
        if not es_Vacia(self.coleccion):
            if type(other) != type(self): # type(Biblioteca)
                raise ValueError('el item no es del tipo de la coleccion')

                for x in range(0, len(other.coleccion) - 1 ):
                    self.coleccion.aniadir(x)
        else:                
            for x in range(0, len(other.coleccion) - 1 ):
                self.coleccion.aniadir(x)
        
