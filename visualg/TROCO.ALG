Algoritmo "troco"

Var
   preco, dinheiroRecebido, troco: Real
   quantidade : Inteiro
Inicio

      escreva("Preço unitário do produto: ")
      leia(preco)
      
      escreva("Quantidade comprada: ")
      leia(quantidade)
      
      escreva("Dinheiro recebido: ")
      leia(dinheiroRecebido)
      
      troco <- dinheiroRecebido - (preco * quantidade)

      escreva("TROCO = ", troco:4:2)

Fimalgoritmo