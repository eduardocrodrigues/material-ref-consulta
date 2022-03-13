
# class Impressora:
    
#     @classmethod
#     def imprimir_folha(cls): 
#         print("folha impressa")


# epson = Impressora() # criando a instância da classe Impressora
# epson.imprimir_folha() # acessando o método da classe A PARTIR DA INSTÂNCIA DA CLASSE.

# Impressora.imprimir_folha() # ACESSANDO DIRETAMENTE DA ESTRUTURA (ESCOPO DA CLASSE) 


# class Impressora:

#     # def __init__(self):
#     #     self.a = 10
    
#     #@classmethod
#     def imprimir_folha(cls): 
#         print("folha impressa")

#     # def imprimir_a(cls):
#     #     print(cls.a)



# e = Impressora()
# e.imprimir_folha()

# Impressora.imprimir_folha()


# class Impressora:

#     @classmethod
#     def imprimir_folha(cls):
#         print('folha impressa')

#     @classmethod
#     def imprimir_livro(cls, paginas):
#         for i in range(paginas):
#             cls.imprimir_folha()


# Impressora.imprimir_folha()

# i = Impressora()
# i.imprimir_livro(5)


# class NomeDaClasse:

#     atributo1 = 'valor1'
#     atributo2 = 'valor2'

#     @classmethod
#     def metodo(cls):
#         print(cls.atributo1)

#     def outroMetodo(self):
#         print('um texto qualquer')

# NomeDaClasse.metodo()


# class Impressora:

#     tinta1 = 'azul'

#     @classmethod
#     def imprimir_folha(cls):
#         print('folha impressa, a tinta escrina na folha é:', cls.tinta1)

#     @classmethod
#     def imprimir_livro(cls, paginas):
#         for i in range(paginas):
#             cls.imprimir_folha()


# Impressora.imprimir_livro(5)



# class Impressora:

#     def trocar_tinta(self, tinta):
#        print('a tinta foi trocada para a cor:', tinta)


# Impressora.trocar_tinta('Verde')

# # i = Impressora()
# i.trocar_tinta('Verde')


# class Impressora:

#     def __init__(self):
#         self.tinta1 = 'azul' # atributo de instância
    
#     @classmethod
#     def imprimir_folha(cls):
#         ########################################################################
#         # qualquer uma das duas linhas abaixo, se for executada, gerará erro !!!
#         #print('cor da tinta:',self.tinta1) 
#         print('cor da tinta:', cls.tinta1) # mesmo se vc trocar o: self do atributo, por: cls, gerará erro, pq o atributo pertence ao escopo de instância da classe !!! 
#         print("folha impressa")


# Impressora.imprimir_folha() # gerará um erro !!! 



# class Impressora:

#     modelo = 'epson' # ATRIBUTO DE CLASSE !!!

#     def __init__(self, numero_folhas):
#         self.numero_folhas = numero_folhas

#     def imprimir_folha(self):
#         print('folha impressa')

#     def imprimir_livro(self, paginas):
#         if paginas <= self.numero_folhas:
#             for i in range(paginas):
#                 self.imprimir_folha()
#                 self.numero_folhas -= 1

#     @classmethod  
#     def print_modelo(cls):
#         print(cls.modelo) 

#     def print_modelo_instancia(self): # MÉTODO DE INSTÂNCIA, pq POSSUI: self, NO PRIMEIRO PARÂMETRO !!!
#         print(self.modelo) # usando ATRIBUTO DE ESCOPO DE CLASSE, com NOTAÇÃO: self, DENTRO DO MÉTODO DE ESCOPO DE INSTÂNCIA.


# impressora = Impressora(10)

# impressora.print_modelo_instancia() # exibe o valor do ATRIBUTO DO ESCOPO DE CLASSE inserido DENTRO do MÉTODO DE INSTÂNCIA !!!


class Impressora:

    modelo = 'epson' # ATRIBUTO DE CLASSE !!!

    def __init__(self, numero_folhas):
        self.numero_folhas = numero_folhas

    def imprimir_folha(self):
        print('folha impressa')

    def imprimir_livro(self, paginas):
        if paginas <= self.numero_folhas:
            for i in range(paginas):
                self.imprimir_folha()
                self.numero_folhas -= 1


impressora = Impressora(15) # criando uma instância

print(impressora.modelo) # ACESSANDO ATRIBUTO DE ESCOPO DE CLASSE a partir DA INSTÂNCIA.

