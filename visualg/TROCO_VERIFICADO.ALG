Algoritmo "troco_verificado"

Var

   precoUnitario, dinheiroRecebido, troco, resto : Real
   quantidadeComprada : inteiro

Inicio

      escreva("Preço unitário do produto: ")
      leia(precoUnitario)
      
      escreva("Quantidade comprada: ")
      leia(quantidadeComprada)
      
      escreva("Dinheiro recebido: ")
      leia(dinheiroRecebido)
      
      se dinheiroRecebido >= (precoUnitario * quantidadeComprada) entao
         troco <- dinheiroRecebido - precoUnitario * quantidadeComprada
         escreval("TROCO = ", troco:4:2)
      senao
           resto <- precoUnitario * quantidadeComprada - dinheiroRecebido
           escreva("DINHEIRO INSUFICIENTE.", "FALTAM ", resto:4:2, " REAIS")
      fimse

Fimalgoritmo