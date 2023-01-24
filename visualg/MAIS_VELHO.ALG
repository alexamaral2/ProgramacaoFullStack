Algoritmo "mais_velho"

Var
   N,i, posMaior, maiorIdade : inteiro
   nome : vetor[0..99] de caractere
   idade : vetor[0..99] de inteiro

Inicio

      escreva("Quantas pessoas voce vai digitar? ")
      leia(N)
      
      para i de 0 ate N-1 faca
           escreval("Dados da ", i+1, "a", " pessoa:")

           escreval("Nome: ")
           leia(nome[i])

           escreval("Idade: ")
           leia(idade[i])
           escreval
      fimpara
      
      maiorIdade <- idade[0]
      
      para i de 0 ate N-1 faca
           se idade[i] > maiorIdade entao
              maiorIdade <- idade[i]
              posMaior <- i
           fimse
      fimpara

      escreval("PESSOA MAIS VELHA: ", nome[posMaior])
Fimalgoritmo