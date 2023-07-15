class Nodo():
    def __init__(self,_estado):#_padre):#,_accion):
        self.estado=_estado   #Entendemos por estado (fila,columna)
        self.padre=[]     
                           #Accion es simplemente un texto
                              #que diga que accion se realizo, ejemplo (Arriba,Abajo,Izquierda,Derecha)
                              #No es fundamental para el funcionamiento
    def NodoPadre(self,_nodo,_vecinosDelNodo):
        #La variable _nodo no lo uso en la funcion pero lo dejo
        #por si puedo usarlo para una futura mejora.
        for i in self.estado:
            for j in _vecinosDelNodo:
                if i == j:
                    self.padre.append(i)
       
    def NodoPadre_para_AS(self,_nodo,_vecinosDelNodo,_estado):
        #La variable _nodo no lo uso en la funcion pero lo dejo
        #por si puedo usarlo para una futura mejora.
        
        for i in _estado:
            for j in _vecinosDelNodo:
                if i == j:
                    self.padre.append(i)
        
    def solucion(self,_meta):
        self.estado.reverse()
        
    
        
        self.padre.append(self.estado[0])
        
        print("------------")
        Para_usar_fruncion_expandir =Laberinto(None)
        self.padre_de_meta = [self.estado[0]]
        num = 0
        
        while num < len(self.padre):
            numero = self.padre.index(self.padre_de_meta[len(self.padre_de_meta)-1])
            if self.padre[0] == self.padre_de_meta[len(self.padre_de_meta)-1]:
                break
            self.padre_de_meta.append(self.padre[numero-1])
            num+=1
        self.padre_de_meta.reverse()
        self.padre_de_meta.append(list(_meta))
        
    def solucionBFS(self):
        
        

        self.padre_de_meta = []
        
        self.padre_de_meta.append(self.estado[len(self.estado)-1])
        
        
        while self.padre_de_meta[len(self.padre_de_meta)-1] != self.estado[0]:
            numero1 = self.estado.index(self.padre_de_meta[len(self.padre_de_meta)-1])
            numero1 -= 1
            self.padre_de_meta.append(self.padre[numero1])
        
        
        self.padre_de_meta.reverse()

    def para_costo_de_AS(self):



        self.padre_de_meta = [self.estado[len(self.estado)-1]]
        num = 0
        
        while num < len(self.padre):
            numero = self.estado.index(self.padre_de_meta[len(self.padre_de_meta)-1])
            
            if self.padre[0] == self.padre_de_meta[len(self.padre_de_meta)-1]:
                break
            self.padre_de_meta.append(self.padre[numero-1])
            num+=1
        
        self.padre_de_meta.reverse()
        
        return len(self.padre_de_meta)-1
    




        



        

        
            
        




    def SolucionPlabras(self):
        num = 0
        solucion_palabras = []

        for i in self.padre_de_meta:
            
            
            arriba = [i[0]-1,i[1]]
            abajo = [i[0]+1,i[1]]
            derecha = [i[0],i[1]+1]
            izquierda = [i[0],i[1]-1]
            numero = self.padre_de_meta.index(i)
            numero += 1
            if numero <= len(self.padre_de_meta)-1:
                if arriba == self.padre_de_meta[numero]:
                    solucion_palabras.append("Arriba")
                elif abajo == self.padre_de_meta[numero]:
                    solucion_palabras.append("Abajo")
                elif derecha == self.padre_de_meta[numero]:
                    solucion_palabras.append("Derecha")
                elif izquierda == self.padre_de_meta[numero]:
                    solucion_palabras.append("Izquierda")
           
        print("Para llegar a la meta desde el incio debe moverse\nde la siguiente manera:")   
        for i in solucion_palabras:
            print(f"--{i}")       



class FronteraStack():
    def __init__(self):
        self.lista_AS = []
        self.contador=0
        self.frontera=[]
    def __str__(self):
        return (f"Tengo los nodos {self.frontera}")
    def agregar_nodo(self,_nodo):
        #Agregar el nodo pasado por parametro a la frontera
        self.frontera.append(_nodo)
    def quitar_nodo(self):
        #Quitar nodo de la frontera (respetar el tipo de frontera)
        return self.frontera.pop()
    def esta_vacia(self):
        #Comprobar si la frontera está vacia o no
        
       
            
        
        return len(self.frontera)==0
    def contiene_estado(self,_estado):
        #Comprobar si el estado pasado por parametro ya se encuentra en la frontera
        return _estado in self.frontera

class FronteraQueue(FronteraStack):
    '''Aplicar herencia con FronteraStack
       La unica diferencia entre ambas es como
       se quitan los nodos
    '''
    def quitar_nodo1(self):
        #Quitar nodo de la frontera (respetar el tipo de frontera)
        return self.frontera.pop(0)

class FronteraGBFS(FronteraStack):
    def quitar_nodo3(self,_meta):
        
        lista_de_resultados = []
        for i in self.frontera:
            numero = [i[0]-_meta[0],i[1]-_meta[1]]
            if numero[0]<0:
                numero = [numero[0]*(-1),numero[1]]
            if numero[1]<0:
                numero = [numero[0],numero[1]*(-1)]
            numero = numero[0]+numero[1]
            lista_de_resultados.append(numero)
        min = lista_de_resultados[0]
        for x in lista_de_resultados:
            if x < min:
                min = x
        frontera_a_quitar = lista_de_resultados.index(min)
        return self.frontera.pop(frontera_a_quitar)
        
class FronteraAS(FronteraStack):
     
    def costo_estimado_a_la_meta(self,_meta,_nodo_actual):
            #esta funcion calcula el costo estimado a la meta del nodo que le pases
            numero = [abs(_nodo_actual[0]-_meta[0]),abs(_nodo_actual[1]-_meta[1])]
            
            numero = numero[0]+numero[1]
            
            return numero
        
    def costo_para_alcanzar_al_nodo(self,_estado_de_nodos,_nodo_a_alcanzar):
        #Esta funcion calcula el costo del nodo que le pases
        recorrido_completo=_estado_de_nodos+[_nodo_a_alcanzar]
        
        para_usar_expandir = Laberinto(None)
        
        nodo3 = Nodo(recorrido_completo)
        
        estado=[]
        for i in nodo3.estado:
            
            estado.append(i)
            if i != nodo3.estado[0]:
                
                
                expandimos = para_usar_expandir.expandir_nodo(i)
                nodo3.NodoPadre_para_AS(i,expandimos,estado)
        costo = nodo3.para_costo_de_AS()
        return costo
        
        

    def quitar_nodo(self,_meta,_inicio,_estado_de_nodos):
        lista_para_comparar_fronteras = []
        if len(self.frontera)==1:
            if self.frontera[0]==_inicio:
                return self.frontera.pop(0)
        
        for i in self.frontera:
            
            costo_a_meta = self.costo_estimado_a_la_meta(_meta,i)
            
            
            costo_hasta_el= self.costo_para_alcanzar_al_nodo(_estado_de_nodos,i)
            
            suma = costo_a_meta+costo_hasta_el
            lista_para_comparar_fronteras.append(suma)

        min = lista_para_comparar_fronteras[0]
        
        numero=0
        for x in lista_para_comparar_fronteras:
            if x < min:
                min = x
          
            if x == lista_para_comparar_fronteras[0]:
                numero+=1
        
        if numero ==len(lista_para_comparar_fronteras) and len(self.frontera)>1:
            min = len(lista_para_comparar_fronteras)-1
            u = self.frontera.pop(min)
            #si todos los nodos de la frontera tienen el mismo costo en total,
            #entonces el .pop saca al ultimo nodo de la frontera
            return u
            

        if len(self.frontera)<=1 or numero !=len(lista_para_comparar_fronteras):
            frontera_a_eliminar = lista_para_comparar_fronteras.index(min)
            u=self.frontera.pop(frontera_a_eliminar)
            #si hay nodos con costos en total distintos, saca el
            #nodo con el costo menor
            #o si solo se encuentra un nodo en la frontera, saca ese nodo

            return u


        
        

        

class Laberinto(Nodo):
    def  __init__(self,_algoritmo):
        '''Dentro del init podemos ejecutar funciones
           para ir definiendo los atributos de la clase.
           Les dejo lista la parte de leer el laberinto
           del archivo de texto, y la detección del inicio,
           meta y paredes.
        '''
        with open('laberinto.txt','r') as archivo:
            laberinto=archivo.read()     #Con read() leemos todo el archivo y lo guardamos en laberinto
        
        laberinto=laberinto.splitlines() #Con splitlines() separamos el laberinto en lineas, eliminando el \n
        
        self.ancho=len(laberinto[0])    #El ancho del laberinto es la cantidad 
                                        #de caracteres de la primer linea 
                                        #(O de cualquiera suponiendo que todas tienen el mismo ancho)
        self.alto=len(laberinto)        #El alto del laberinto es la cantidad de lineas
        self.paredes=[]                 #Lista de paredes

        for fila in range(self.alto):   #Recorremos todas las filas
            fila_paredes=[]             #Creamos una lista vacia para las paredes de la fila actual
                                      #para cada fila se vuelve a limpiar la lista
            for columna in range(self.ancho):                                #Recorremos todas las columnas
                if laberinto[fila][columna]=='#': #Si el caracter es # es una pared
                    fila_paredes.append((fila,columna)) #Agregamos la pared a la lista de paredes de la fila actual
                elif laberinto[fila][columna]=='I':   #Si el caracter es I es el inicio
                    self.inicio=(fila,columna)         #Guardamos el inicio
                elif laberinto[fila][columna]=='M':   #Si el caracter es M es la meta
                    self.meta=(fila,columna) 
                                                          #Guardamos la meta
            self.paredes.append(fila_paredes)        #Agregamos la lista de paredes de la fila actual a la lista de paredes
        #De este modo ya tenemos identificadas las paredes, el inicio y la meta
       
        try:
            self.estado = self.inicio
        except:
            print("No se encontro un inicio asignado.")
            return
        try:
            u = self.meta
        except:
            print("No se encontro una meta asignada.")
            return
        self.recorrido_actual_del_nodo=[]
        self.algoritmo=_algoritmo #String en el que pasamos el nombre del algoritmo a utilizar
        self.resolver()
    def expandir_nodo(self,_nodo):
        '''Dentro de _nodo.estado tenemos la posicion actual del nodo
           Debemos comprobar en todas las direcciones si podemos movernos
           descartando las que sean paredes o esten fuera del laberinto                 (i-1,j)     --->   (fila-1,columna)
           Utilicen el grafico que está en el Notion para guiarse                (i,j-1) (i,j) (i,j+1)
           Devolver una lista de vecinos posibles (nodos hijo)                          (i+1,j)     --->   (fila+1,columna)
        '''
        
        vecinos_posibles = []
        
        arriva = [_nodo[0]-1,_nodo[1]]
        abajo = [_nodo[0]+1,_nodo[1]]
        derecha = [_nodo[0],_nodo[1]+1]
        izquierda = [_nodo[0],_nodo[1]-1]
        vecinos_posibles.append(arriva)
        vecinos_posibles.append(abajo)
        vecinos_posibles.append(derecha)
        vecinos_posibles.append(izquierda)
        
        for i in self.paredes:
            for j in i:
                for e in vecinos_posibles:
                    
                    if tuple(e) == j:
                        vecinos_posibles.remove(e)
        for i in vecinos_posibles:
            
            if i[1] >= self.ancho or i[0] >= self.alto or i[1] < 0 or i[0] < 0:
                vecinos_posibles.remove(i)
        
        return vecinos_posibles
        

        



        
        

    def resolver(self):
        '''
        Acá tienen que implementar el algoritmo de busqueda
        La idea es intentar replicar el pseudocodigo que vimos en clase
        1- Inicializar la frontera con el nodo inicial
        2- Inicializar el conjunto de explorados como vacio
        3- Repetimos:
            3.1- Si la frontera esta vacia, no hay solucion
            3.2- Quitamos un nodo de la frontera
            3.3- Si el nodo contiene un estado que es meta, devolver la solucion
            3.4- Agregar el nodo a explorados
            3.5- Expandir el nodo, agregando los nodos hijos a la frontera
        '''
        if self.algoritmo=='BFS':
            #Crear la frontera que corresponda
            #iniciamos con la frontera que contiene el estado inicial
            nodo1 = Nodo([list(self.inicio)])
            frontera1 = FronteraQueue()
            frontera1.agregar_nodo(list(self.inicio))
            nodos_explorados1 = []

            num1 = 0 #esta variable es para mostrar el except una sola ves
            while True:
                num1 +=1
                if True == frontera1.esta_vacia():
                    print("Se termino de recorrer todo el laberinto sin encontrar una meta.")
                    print("-----------")
                    print("Recorrido completo(Evaluando los caminos a la meta, no hay uno que llegue a ella):")
                    print(self.recorrido_actual_del_nodo)
                    return
                nodo_quitado1 = frontera1.quitar_nodo1()
                self.recorrido_actual_del_nodo.append(nodo_quitado1)
                
                if tuple(nodo_quitado1) == self.meta:
                    print("Recorrido completo para llegar a la meta: ")
                    print(self.recorrido_actual_del_nodo)

                    print(f"La IA tuvo que hacer {len(self.recorrido_actual_del_nodo)-1} movimientos\npara llegar a la meta.")
                    print("Se uso el metodo BFS.")

                    break
                
                nodos_explorados1.append(nodo_quitado1)
                
                expandimos1 = self.expandir_nodo(nodo_quitado1)
                
                
                for i in expandimos1:   
                    opcion1 = frontera1.contiene_estado(i)
                    if opcion1 == True:
                        expandimos1.remove(i)
                    for j in nodos_explorados1:
                        if i == j:
                            
                            expandimos1.remove(i)
                        
                for i in expandimos1:
                    frontera1.agregar_nodo(i)
                if num1 >1:
                    nodo1.estado.append(nodo_quitado1)
                    expandimos3 = self.expandir_nodo(nodo_quitado1)
                    nodo1.NodoPadre(nodo_quitado1,expandimos3)
            
            nodo1.estado.append(list(self.meta))
            expandimos3 = self.expandir_nodo(list(self.meta))
            nodo1.NodoPadre(list(self.meta),expandimos3)
            print("--------------------------------")

            nodo1.solucionBFS() 

            nodo1.SolucionPlabras()
            print("-------")
            print(f"Recorrido directo desde el inicio hasta la meta, en matriz:\n{nodo1.padre_de_meta}")
            
            
            
        elif self.algoritmo=='DFS':
            #Crear la frontera que corresponda
            nodo = Nodo([list(self.inicio)])
            frontera = FronteraStack()
            frontera.agregar_nodo(list(self.inicio))
            nodos_explorados = []
            num = 0 #esta variable es para mostrar el except una sola ves
            while True:
                num +=1
                if True == frontera.esta_vacia():
                    print("Se termino de recorrer todo el laberinto sin encontrar una meta.")
                    print("-----------")
                    print("Recorrido completo(Evaluando los caminos a la meta, no hay uno que llegue a ella):")
                    print(self.recorrido_actual_del_nodo)
                    return
                nodo_quitado = frontera.quitar_nodo()
                self.recorrido_actual_del_nodo.append(nodo_quitado)
                
                
                if tuple(nodo_quitado) == self.meta:
                    print("Recorrido completo para llegar a la meta: ")
                    print(self.recorrido_actual_del_nodo)
                    print(f"La IA tuvo que hacer {len(self.recorrido_actual_del_nodo)-1} movimientos\npara llegar a la meta.")
                    print("Se uso el metodo DFS.")

                    break
                
                nodos_explorados.append(nodo_quitado)
                
                expandimos = self.expandir_nodo(nodo_quitado)
                
                for i in expandimos:   
                    opcion = frontera.contiene_estado(i)
                    if opcion == True:
                        expandimos.remove(i)
                    for j in nodos_explorados:
                        if i == j:
                            expandimos.remove(i)
                for i in expandimos:
                    frontera.agregar_nodo(i)
                if num >1:
                    nodo.estado.append(nodo_quitado)
                    expandimos2 = self.expandir_nodo(nodo_quitado)
                    nodo.NodoPadre(nodo_quitado,expandimos2)
                   
            print("--------------------------------")
            nodo.solucion(self.meta)    
            nodo.SolucionPlabras()
            print("-------")
            print(f"Recorrido directo desde el inicio hasta la meta, en matriz:\n{nodo.padre_de_meta}")
            
            
        #------------------------------------------------------------------------

        elif self.algoritmo == "GBFS":


            nodo = Nodo([list(self.inicio)])
            frontera = FronteraGBFS()
            frontera.agregar_nodo(list(self.inicio))
            nodos_explorados = []
            num = 0 #esta variable es para mostrar el except una sola ves
            while True:
                num +=1
                if True == frontera.esta_vacia():
                    print("Se termino de recorrer todo el laberinto sin encontrar una meta.")
                    print("-----------")
                    print("Recorrido completo(Evaluando los caminos a la meta, no hay uno que llegue a ella):")
                    print(self.recorrido_actual_del_nodo)
                    return
                nodo_quitado = frontera.quitar_nodo3(list(self.meta))
                self.recorrido_actual_del_nodo.append(nodo_quitado)
                
                
                if tuple(nodo_quitado) == self.meta:
                    print("Recorrido completo para llegar a la meta: ")
                    print(self.recorrido_actual_del_nodo)
                    print(f"La IA tuvo que hacer {len(self.recorrido_actual_del_nodo)-1} movimientos\npara llegar a la meta.")
                    print("Se uso el metodo DFS.")

                    break
                
                nodos_explorados.append(nodo_quitado)
                
                expandimos = self.expandir_nodo(nodo_quitado)
            
                for i in expandimos:   
                    opcion = frontera.contiene_estado(i)
                    if opcion == True:
                        expandimos.remove(i)
                    for j in nodos_explorados:
                        if i == j:
                            expandimos.remove(i)
                for i in expandimos:
                    frontera.agregar_nodo(i)

                if num >1:
                    nodo.estado.append(nodo_quitado)
                    expandimos = self.expandir_nodo(nodo_quitado)
                    
                    nodo.NodoPadre(nodo_quitado,expandimos)
            
            nodo.estado.append(list(self.meta))
            expandimos = self.expandir_nodo(list(self.meta))
            nodo.NodoPadre(list(self.meta),expandimos)
            print("--------------------------------")

            nodo.solucionBFS() 

            nodo.SolucionPlabras()
            print("-------")
            print(f"Recorrido directo desde el inicio hasta la meta, en matriz:\n{nodo.padre_de_meta}")
            
                


        elif self.algoritmo == "AS":
        
            nodo = Nodo([list(self.inicio)])
            

            frontera = FronteraAS()
            frontera.agregar_nodo(list(self.inicio))
            nodos_explorados = []
            num = 0 #esta variable es para mostrar el except una sola ves

            while True:
                num +=1
                
                
                if True == frontera.esta_vacia():
                    print("Se termino de recorrer todo el laberinto sin encontrar una meta.")
                    print("-----------")
                    print("Recorrido completo(Evaluando los caminos a la meta, no hay uno que llegue a ella):")
                    print(self.recorrido_actual_del_nodo)
                    return
                
                
                    

                nodo_quitado = frontera.quitar_nodo(list(self.meta),list(self.inicio),self.recorrido_actual_del_nodo)
                self.recorrido_actual_del_nodo.append(nodo_quitado)
                
                
                if tuple(nodo_quitado) == self.meta:
                    print("Recorrido completo para llegar a la meta: ")
                    print(self.recorrido_actual_del_nodo)
                    print(f"La IA tuvo que hacer {len(self.recorrido_actual_del_nodo)-1} movimientos\npara llegar a la meta.")
                    print("Se uso el metodo DFS.")

                    break
                
                nodos_explorados.append(nodo_quitado)
                
                expandimos = self.expandir_nodo(nodo_quitado)
                
                for i in expandimos:   
                    opcion = frontera.contiene_estado(i)
                    if opcion == True:
                        expandimos.remove(i)
                    for j in nodos_explorados:
                        if i == j:
                            expandimos.remove(i)
                
                for i in expandimos:
                    frontera.agregar_nodo(i)
                
                if num >=1:
                    nodo.estado.append(nodo_quitado)
                    expandimos = self.expandir_nodo(nodo_quitado)
                    nodo.NodoPadre(nodo_quitado,expandimos)
            
            nodo.estado.append(list(self.meta))
            expandimos = self.expandir_nodo(list(self.meta))
            nodo.NodoPadre(list(self.meta),expandimos)
            print("--------------------------------")

            nodo.solucionBFS() 

            nodo.SolucionPlabras()
            print("-------")
            print(f"Recorrido directo desde el inicio hasta la meta, en matriz:\n{nodo.padre_de_meta}")
            
            
                    
                    
                
            

Laberinto("GBFS")
