Algoritmo "semnome"

Var

   produto1 : caracter
   produto2 : caracter
   preco1: real
   preco2: real
   idade: inteiro
   codigo: inteiro
   genero: caracter
   
Inicio

      produto1 <- "Computador"
      produto2 <- "TV"
      preco1 <- 2100.58
      preco2 <- 1830
      idade <- 30
      codigo <- 5291
      genero <- "F"

      escreval("Produtos")
      escreval("O Produto ", produto1, " custa R$", preco1:8:2)
      escreval("O Produto ", produto2, " custa R$", preco2:8:2)
      escreval("")

      escreval("Código = ",codigo)
      escreval("")
      
      escreval("Dados da Pessoa: Genero ", genero, " Idade", idade)
Fimalgoritmo