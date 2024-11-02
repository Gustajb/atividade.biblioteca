class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista para armazenar livros

    def adicionar_livro(self, titulo, autor):
        """Adiciona um livro à biblioteca."""
        livro = {'titulo': titulo, 'autor': autor}
        self.livros.append(livro)
        print(f'Livro "{titulo}" adicionado com sucesso!')

    def remover_livro(self, titulo):
        """Remove um livro da biblioteca pelo título."""
        for livro in self.livros:
            if livro['titulo'] == titulo:
                self.livros.remove(livro)
                print(f'Livro "{titulo}" removido com sucesso!')
                return
        print(f'Livro "{titulo}" não encontrado.')

    def listar_livros(self):
        """Lista todos os livros da biblioteca."""
        if not self.livros:
            print('Nenhum livro disponível.')
            return
        print('Livros disponíveis:')
        for livro in self.livros:
            print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}')

    def buscar_livro(self, titulo):
        """Busca um livro pelo título."""
        for livro in self.livros:
            if livro['titulo'] == titulo:
                print(f'Livro encontrado: Título: {livro["titulo"]}, Autor: {livro["autor"]}')
                return
        print(f'Livro "{titulo}" não encontrado.')

    def emprestar_livro(self, titulo):
        """Empresta um livro, removendo-o da lista."""
        for livro in self.livros:
            if livro['titulo'] == titulo:
                self.livros.remove(livro)
                print(f'Livro "{titulo}" emprestado com sucesso!')
                return
        print(f'Livro "{titulo}" não disponível para empréstimo.')
