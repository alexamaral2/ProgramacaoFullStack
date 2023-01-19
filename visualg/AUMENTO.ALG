Algoritmo "aumento"

Var

salarioPessoa, aumento, porcentagem, novoSalario: real

Inicio

      escreva("Digite o salario da pessoa: ")
      leia(salarioPessoa)
      
      se salarioPessoa <= 1000.00 entao
         porcentagem <- 20
      senao
         se salarioPessoa <= 3000.00 entao
            porcentagem <- 15
         senao
              se salarioPessoa <= 8000.00 entao
                 porcentagem <- 10
              senao
                   se salarioPessoa > 8000 entao
                      porcentagem <- 5
                   fimse
               fimse
         fimse
      fimse

      aumento <- salarioPessoa * porcentagem / 100
      novoSalario <- salarioPessoa + aumento
      
      escreval("Novo salario = R$ ", novoSalario:8:2)
      escreval("Aumento = R$ ", aumento:6:2)
      escreval("Porcentagem: ", porcentagem, "%")
Fimalgoritmo