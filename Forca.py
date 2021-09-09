#BIBLIOTECAS
import random

#TABULEIRO
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

lc=[]
le=[]
z=0
x=0
class enforcado:
    #método construtor
    def __init__(self,word,x,z):
        self.word=list(word)
        self.ocult=list(word)
        self.n=len(word)
        self.x=x
        self.z=z
    def ocultar(self):
        for i in range(0,self.n):
            self.ocult[i]='_'
    def imprimir(self):
        print(board[self.x])
        print('palavra:')
        print(self.ocult)
        print('letras corretas:')
        print(lc)
        print('letras erradas:')
        print(le)
        print(self.word)
        #print(self.n)
        #print(self.z)
    def adivinhar(self,letra,lc,le):
        for v in range(0,self.n):
            if letra==self.word[v]:
                for k in range(0,self.n):
                    if letra == self.word[k]:
                        self.ocult[k]=letra
                        lc.append(letra)
                        self.z+=1
                    else:
                        for l in range(0,self.n):
                            if letra == self.word[l]:
                                break
                            elif l==self.n-1:
                                le.append(letra)
                                self.x+=1
                                break
                break
            elif v==self.n-1:
                le.append(letra)
                self.x+=1



                
    def verifica(self):
        if self.z==self.n:
            self.imprimir()
            print('parabéns, você se safou dessa!')
            return 'venceu'
        elif self.x>6:
            print('você foi enforcado, tente novamente!')
            return 'perdeu'
        else:
            print('segue o jogo!')
            return 'jogando'
# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt","rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()

def main():
    status='jogando'
    #passar a palavra do banco
    game = enforcado(rand_word(),x,z)
    #ocultar a palavra
    game.ocultar()
    #enquanto o jogador não estourar erros ou acertar todas as letras PLAY
    while status=='jogando':
        game.imprimir()
        letra=(input('digite a letra:'))
        game.adivinhar(letra,lc,le)
        status=game.verifica()
# Executa o programa		
if __name__ == "__main__":
	main()
    
        
    