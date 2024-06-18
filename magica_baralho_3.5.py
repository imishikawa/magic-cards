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
                     posicao_magico = 0
                     #posicao_usuario = 5
                     #posicao_magico = random.randint(0,9) #posicao inicial escolhida pelo magico
                     posicao_usuario =  random.randint(0,9) #posição inicial escolhida por alguem da plateia
                     #print('Posição Mágico:' posicao_magico)
                     #print('Posição Pessoa da Platéia:' posicao_usuario)
                     
#Atribuição de valores:
                     while posicao_magico<52:
                            numero = baralho[posicao_magico][2]
                            posicao_magico = posicao_magico+numero
                     posicao_magico = posicao_magico-numero  #voltando para a carta anterior       

                     while posicao_usuario<52:
                            numero = baralho[posicao_usuario][2]
                            posicao_usuario = posicao_usuario+numero
                     posicao_usuario = posicao_usuario-numero  #voltando para a carta anterior
                     #print('Posição Mágico:' posicao_magico)
                     #print('Posição Pessoa da Platéia:' posicao_usuario)
                  
                     if posicao_magico != posicao_usuario:
                            errado=errado+1
                                  
                     elif posicao_magico == posicao_usuario:
                            certo=certo+1
                                                            
                     repetir=repetir+1
       print ('Total de Acertos:', certo)
       print ('Total de Erros:', errado)
       total=certo+errado
       divisão = certo/total
       print ('Porcentagem de acerto:', divisão*100)

       x=int(input('1 para continuar, 2 para sair:'))
       if x != 1:
              break
       else:
              soma = 1

       
