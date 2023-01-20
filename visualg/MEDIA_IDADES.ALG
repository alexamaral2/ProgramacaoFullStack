Algoritmo "media_idades"


Var

   idade, i, soma : inteiro
   media : Real

Inicio

      soma <- 0
      i <- 0
      
      escreval("Digite as idades: ")
      leia(idade)

      enquanto idade >= 0 faca

          soma <- soma + idade
          i <- i + 1

          leia(idade)
      fimenquanto
         
      se i > 0 entao
         media <- soma / i
         escreval("MEDIA = ", media:4:2)
      senao
         escreval("IMPOSSIVEL CALCULAR")
      fimse
Fimalgoritmo