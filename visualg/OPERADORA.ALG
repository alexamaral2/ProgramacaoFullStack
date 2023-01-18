Algoritmo "operadora"

Var

   qtdMinutos, valorBasico : inteiro
   valorFinal : Real

Inicio

      escreva("Digite a quantidade de minutos: ")
      leia(qtdMinutos)

      se qtdMinutos > 100 entao
         valorFinal <- 50 + ((qtdMinutos - 100) * 2)
      senao
           valorFinal <- 50
      fimse
      escreval("Valor Gasto: R$ ", valorFinal:5:2)
Fimalgoritmo