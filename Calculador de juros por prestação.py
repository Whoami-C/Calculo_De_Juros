def pagamentos (P, D): ## P = prestações, D = Dias de atraso
    
    if D == 0: ## If para identificar  e retornar O valor da prestação  Caso o dia de atraso for 0
        return P
    
    else: ## Calculo do codigo
        
        M = P * 0.03
        J = P * 0.01 * D 
        return M + J + P
Quantidade = 0 ## Apresentando Variaveis 
ValorFinal = 0
while True: ##  Iniciando bloco de repetição
    
    Prestacao = int(input("Digite o valor da prestação(0 Para sair e visualizar o relatario): ")) 
    if Prestacao < 0: ## Finalizações do codigo
        break
    if Prestacao == 0: 
        break        
    DiasA = int(input("Digite a quantidade de Dias em atraso: ")) ## Adquirindo Variaveis para execução do codigo
    ValorTotal = pagamentos(Prestacao, DiasA)
    print (f"Valor a ser pago: R${ValorTotal}") ## Chamando a função // Executando o calculo
    Quantidade += 1   
    ValorFinal += ValorTotal

print (" ======= Relatorio Final =======\n") ## Visualização dos resultados!
print (f"Quantidade de Prestações: {Quantidade}")
print (f"Valor total de Prestações: {ValorFinal}")