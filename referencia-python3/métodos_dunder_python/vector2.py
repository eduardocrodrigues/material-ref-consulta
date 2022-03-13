import math

class Vector2:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        #################################################
        # o método hasattr() funciona da seguinte forma:
        # o PRIMEIRO PARÂMETRO recebe um objeto (ou seja,
        # tem que ser uma classe) que no nosso caso é uma classe do tipo Vector2
        # o SGUNDO PARÂMETRO recebe uma string que representa O ATRIBUTO ou O MÉTODO dentro da classe definida
        # no primeiro parâmetro. O valor retornado do método hasattr() é um boleano (True ou False).
        if hasattr(x, "__getitem__"):
            x, y = x
            self._v = [float(x), float(y)]
        else:
            self._v = [float(x), float(y)]

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    # esse é um MÉTODO INDEPENDENTE dentro da classe Vector2, pq não possui o: self no primeiro parâmetro.
    def from_points(P1, P2):
        # Vc deve estar se perguntando:
        #   COMO CONSEGUIMOS RETORNAR A PRÓPRIA ESTURURA DA CLASSE Vector2() EM UM MÉTODO
        #   DA PRÓPRIA ESTRUTURA DA CLASSE: Vector2() que ACABAMOS DE CRIAR?
        #
        # e a resposta é simples, quando definimos a classe (ou seja, a estrutura da classe em uma arquivo,
        # que no caso é a classe: Vector2()), e chamamos essa classe, por exemplo:
        #
        #    Vector2(10, 20)
        #        ou
        #    v = Vector2(10, 20)
        #
        # e NAS LINHAS APÓS A ESTRUTURA DA CLASSE, CHAMARMOS O MÉTODO QUE RETORNA A PROPRIA CLASSE (que no caso,
        # é o método: .from_points()), exemplo:
        #
        #    print(Vector2(10, 20).from_points(Vector2(10, 20), Vector2(30, 40))
        #        ou
        #    novoVetor = v.from_points(Vector2(10, 20), Vector2(30, 40))
        #    print(novoVetor)
        #
        # quando colocamos o arquivo para executar, o python primeiro lê a estrutura da classe: Vector2(), (definida
        # sempre no começo do arquivo) e é como se o python dissesse:
        # (python: ESTOU LENDO ESSE ARQUIVO E VEJO UMA ESTRUTURA DE CLASSE CHAMADA: Vector2())
        #
        # e nas linhas abaixo, DEPOIS DA ESTRUTURA DA CLASSE,
        # (o python lê as linhas da seguinte forma:
        #  FOI CRIADA UMA INSTÂNCIA DA CLASSE Vector2())
        #
        #    novoVetor = v.from_points(Vector2(10, 20), Vector2(30, 40))
        #
        # e na linha seguinte, quando chamamos o método: .from_points(),
        # ( é como se o python dissesse:
        # NA INSTÂNCIA CRIADA COM A CLASSE Vector2(), FOI CHAMADO O MÉTODO: .from_points(), E DENTRO DESSE MÉTODO
        # É RETORNADO A PRÓPRIA CLASSE: Vector2(), que é A ESTRUTURA DE CLASSE QUE EU LÍ NO COMEÇO DO ARQUIVO !!!).
        #
        # É por isso que o python consegue retornar a própria classe, PQ QUANDO O MÉTODO: .from_points() É CHAMADO
        # A PARTIR DA INSTÂNCIA DA CLASSE, É COMO SE TIVESSEMOS INSERIDO O NOME DA CLASSE Vector2() NA
        # LINHA ONDE ESTÁ A PALAVRA: return DENTRO DO MÉTODO: .from_points(), NO MOMENTO
        # QUE CHAMAMOS O MÉTODO: .from_points().
        #
        return Vector2(P2[0] - P1[0], P2[1] - P1[1])

    def get_magnitude(self):
        return math.sqrt( self.x**2 + self.y**2 )

    def normalize(self):

        magnitude = self.get_magnitude()
        try:
            self.x /= magnitude
            self.y /= magnitude

        except ZeroDivisionError:
            self.x = 0
            self.y = 0

    # rhs quer dizer Right Hand Side (Lado Direito)
    def __add__(self, rhs):
        return Vector2( self.x + rhs.x, self.y + rhs.y )

    def __sub__(self, rhs):
        return Vector2( self.x - rhs.x, self.y - rhs.y )

    def __neg__(self, rhs):
        return Vector2( -self.x, -self.y )

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

    def __getitem__(self, index):
        return self._v[index]

    def __setitem__(self, index, value):
        self._v[index] = 1.0 * value



va = (10, 20)
vb = (30, 50)

##################################
# só para entendimento, EU INSTÂNCIEI A CLASSE: Vector2(),
# mas NÃO ESTOU USANDO ELA.
v = Vector2(2, 5)
#######################################################
# Já na linha abaixo, em:
#
#    result = Vector2.from_points(va, vb)
#
# EU NÃO CRIEI NENHUMA INSTÂNCIA PARA PODER USAR O MÉTODO: .from_points(va, vb), ISSO PORQUE
# O MÉTODO: .from_points() da classe: Vector2(), É UM MÉTODO INDEPENDENTE,
# isso significa que VC NÃO PRECISA DE INSTÂNCIAR A CLASSE PARA USAR O MÉTODO,
# BASTA CHAMAR O NOME DA CLASSE SEGUIDO DO NOME DO MÉTODO, COMO MOSTRA A LINHA ABAIXO,
# e vc PODERÁ USAR O MÉTODO NORMALMENTE.
#
#  OBS: SE VOCÊ INSTANCIAR UMA CLASSE e TENTAR USAR UM MÉTODO INDEPENDENTE a partir DA INSTÂNCIA DA CLASSE,
#  O CÓDIGO GERARÁ UM ERRO !!!!
#
result = Vector2.from_points(va, vb)
print(result)
