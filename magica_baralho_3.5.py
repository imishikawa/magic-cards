#1. fazer os mágico e a platéia serem random
#2. para 10 000 vezes
import random

baralho = list();
naipes = ['ouros','copas','paus','espadas']

for i in range(1,14):
       for j in range(0,len(naipes)):
        
        if i == 1:
            name = 'Ás';
            numero = 1;
        elif i <= 10:
           name = i;
           numero = i;
        elif i == 11:
            name = 'VALETE';
            numero = 5;
        elif i == 12:
            name = 'RAINHA';
            numero = 5;
        elif i == 13:
            name = 'REI';
            numero = 5;
            
        carta = (name, naipes[j],numero) #numero é o valor de cada carta
        baralho.append(carta)


Nmax = 10000

soma = 1
while soma==1:
       
       

       #print (baralho)

       certo=0
       errado=0
       repetir=1
       while repetir<=Nmax:
                     random.shuffle (baralho)
                     posicao = 0
                     #posicaoUsuario = 5
                     #posicao = random.randint(0,9) #posicao inicial escolhida pelo magico
                     posicaoUsuario =  random.randint(0,9) #posição inicial escolhida por alguem da plateia
                     #print(posicao)
                     #print(posicaoUsuario)
#Atribuição de valores:
                     while posicao<52:
                            numero = baralho[posicao][2]
                            posicao = posicao+numero
                     posicao = posicao-numero  #voltando para a carta anterior       

                     while posicaoUsuario<52:
                            numero = baralho[posicaoUsuario][2]
                            posicaoUsuario = posicaoUsuario+numero
                     posicaoUsuario = posicaoUsuario-numero  #voltando para a carta anterior
                     #print('Posicao Usuario',posicaoUsuario)
                     #print('Posicao',posicao)
                  
                     if posicao != posicaoUsuario:
                            errado=errado+1
                                  
                     elif posicao == posicaoUsuario:
                            certo=certo+1
                                                            
                     repetir=repetir+1
       print (certo)
       print (errado)
       total=certo+errado
       divisão = certo/total
       print ("Porcentagem de acerto:", divisão*100)

       x=int(input("1 para continuar, 2 para sair:"))
       if x != 1:
              break
       else:
              soma = 1

       
