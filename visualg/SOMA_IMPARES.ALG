Algoritmo "soma_impares"

Var

   X, Y, troca, soma,i : inteiro


Inicio

      escreval("Digite dois numeros: ")
      leia(X)
      leia(Y)
      
      se X > Y entao
         troca <- X
         X <- Y
         Y <- troca
      fimse

      para i de X+1 ate Y-1 faca
           se i % 2 <> 0 entao
              soma <- soma + i
           fimse
      fimpara
      
      escreval("SOMA DOS IMPARES = ", soma)
Fimalgoritmo