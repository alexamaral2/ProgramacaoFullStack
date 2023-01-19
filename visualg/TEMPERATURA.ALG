Algoritmo "temperatura"


Var

   TC, TF: Real
   unidade : caractere

Inicio

      escreva("Voce vai digitar a temperatura em qual escala (C/F)? ")
      leia(unidade)
      
      escolha unidade
      caso "C"
           escreva("Digite a temperatura em Fahrenheit: ")
           leia(TF)

           TC <- 5 / 9 * (TF - 32)
           escreval("Temperatura equivalente em Celsius: ", TC:4:2)
      caso "F"
           escreva("Digite a temperatura em  Celsius: ")
           leia(TC)
           
           TF <- 9 * TC / 5 + 32
           escreval("Temperatura equivalente em Fahrenheit: ", TF:4:2)
     fimescolha
Fimalgoritmo