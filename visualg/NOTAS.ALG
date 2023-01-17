Algoritmo "notas"

Var

   nota1, nota2, notaFinal : Real

Inicio

   escreva("Digite a primeira nota: ")
   leia(nota1)
   
   escreva("Digite a segunda nota: ")
   leia(nota2)
   
   notaFinal <- nota1 + nota2 / 2
   
   se notaFinal < 60 entao
      escreval("NOTA FINAL = ", notaFinal:5:1)
      escreval("REPROVADO")
   senao
      escreva("NOTA FINAL = ", notaFinal:5:1)
   fimse

Fimalgoritmo