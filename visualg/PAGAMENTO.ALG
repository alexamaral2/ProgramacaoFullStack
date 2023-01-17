Algoritmo "pagamento"

Var

   valorHora, valorPagamento : Real
   horasTrabalhada: Inteiro
   nome : caractere

Inicio

      escreva("Nome: ")
      leia(nome)
      
      escreva("Valor por hora: ")
      leia(valorHora)
      
      escreva("Horas trabalhadas: ")
      leia(horasTrabalhada)

      valorPagamento <- valorHora * horasTrabalhada
      
      escreva("O pagamento para ",nome, " deve ser ", valorPagamento:4:2)

Fimalgoritmo