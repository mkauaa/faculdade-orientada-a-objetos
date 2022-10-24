class Artista():
    def __init__(self, nome, nacionalidade):
        self._nome = nome
        self._nacionalidade = nacionalidade

    @property
    def nome(self):
        return self._nome

    @property
    def nacionalidade(self):
        return self._nacionalidade

    def imprimir(self):
        return f'Nome: {self.nome} \nNacionalidade: {self.nacionalidade}'        

class Obra():
    codigo = 0
    def __init__(self, titulo, tecnica, autor:Artista):
        self._codigo = __class__.codigo + 1
        __class__.codigo += 1
        self._titulo = titulo
        self._tecnica = tecnica
        self._autor = autor
        self._valor = 0

    @property
    def titulo(self):
        return self._valor

    @property
    def tenica(self):
        return self._tecnica  

    @property
    def autor(self):
        return self._autor

    @property
    def valor(self):
        return self._valor

    def avaliar(self):
        # Técnica: 1 - Boa/ 2 - Interessante/ 5 - Excelente
        # Inovação: 2 - Comum/ 4 - Inovadora/ 6 - Única

        ava_tecnica = int(input('Qual a nota para a técnica? [1/ 2/ 5] : '))
        ava_inovacao = int(input('Qual a nota para a inovação? [2/ 4/ 6] : '))
        
        self._valor = (ava_tecnica * 50 + ava_inovacao * 80) * 10
        return f'Valor: R${self._valor}'

    def imprimir(self):
        return f'Código: {self.codigo} \nTítulo: {self.titulo} \nAutor: {self.autor} \nTécnica: {self.tecnica}'
    
    def imprimirObra(self):
        return f'Código: {self.codigo} \nTítulo: {self.titulo} \nValor: {self._valor}'


class Pintura(Obra):
    def __init__(self, titulo, tecnica, inovacao, autor: Artista, tinta):
        super().__init__(titulo, tecnica, inovacao, autor)
        self.tinta = tinta

    @property
    def tinta(self):
        return self._tinta

    def imprimir(self):
        return super().imprimir() + 'Tipo de tinta: ' + self.tinta

class Escultura(Obra):
    def __init__(self, titulo, tecnica, inovacao, autor: Artista, material):
        super().__init__(titulo, tecnica, inovacao, autor)
        self.material = material

    @property
    def material(self):
        return self._material

    def imprimir(self):
        return super().imprimir() + 'Tipo de material: ' + self.material

class Galeria():
    def __init__(self, nome, telefone, nomeResponsavel):
        self._nome = nome
        self._telefone = telefone
        self._nomeResponsavel = nomeResponsavel

        self._pinturas = []
        self._esculturas = []

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone
    
    @property
    def nomeResponsavel(self):
        return self._nomeResponsavel

    @property
    def pinturas(self):
        return self._pinturas
    @pinturas.setter
    def pinturas(self, obra: Pintura):
        self._pinturas.append(obra)

    @property
    def esculturas(self):
        return self._esculturas
    @esculturas.setter
    def esculturas(self, obra: Escultura):
        self._esculturas.append(obra)

    def cadastrarObra(self):
        nome = input('Digite o nome do artista: ')
        artista = self.pesquisarArtista(nome)
        if artista == None:
            print('Artista não cadastrado. Vamos cadastrar!')
            artista2 = Artista(nome, input('Digite a nacionalidade do artista: '))
            artista = artista2

        tipo_obra = int(input('Deseja cadastrar uma [1] Pintura ou [2] Escultura? '))

        if tipo_obra == 1:
            self.cadastrarPintura(artista)
            print('Cadastro realizado.')

        if tipo_obra == 2:
            self.cadastrarEscultura(artista)
            print('Cadastro realizado.')
    
    def cadastrarPintura(self, autor):
        titulo = input('Titulo: ')
        tecnica = input('Técnica: ')
        tinta = input('Tinta: ')
        obra = input('Obra: ')
        self.pinturas = []

    def cadastrarEscultura(self, autor):
        titulo = input('Titulo: ')
        tecnica = input('Técnica: ')
        material = input('Material: ')
        obra = input('Obra: ')
        self.esculturas = []
        
    def pesquisarObras(self, nome):
        for elemento in self.pinturas:
            if(elemento._autor.nome == nome):
                print(elemento.imprimir())

        for elemento in self.escultura:
            if(elemento._autor.nome == nome):
                print(elemento.imprimir())

    def pesquisarArtista(self, nome):
        for elemento in self.pinturas:
            if(elemento._autor.nome == nome):
                return elemento

        for elemento in self.escultura:
            if(elemento._autor.nome == nome):
                return elemento
        
        return None

    def pesquisarCodigo(self, codigo):
        for elemento in self.pinturas:
            if(elemento._autor.codigo == codigo):
                return elemento

        for elemento in self.escultura:
            if(elemento._autor.codigo == codigo):
                return elemento

    def imprimirObras(self):
        for elemento in self.pinturas:            
            return Pintura.imprimir

        for elemento in self.escultura:
            return Escultura.imprimir
    
