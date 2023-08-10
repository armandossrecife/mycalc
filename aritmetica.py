class OperacoesBasicas:
    def soma(self, valor1, valor2):
        return valor1 + valor2
    
    def subtrair(self, valor1, valor2):
        return valor1-valor2
    
    def multiplicar(self, valor1, valor2):
        return valor1*valor2

    def dividir(self, valor1, valor2):
        if valor2 != 0:
            return valor1/valor2
        return "Erro!"
    
    def ler_valores(self):
        valor1 = float(input('Qual o valor1 ?'))
        valor2 = float(input('Qual o valor2 ?'))
        return valor1, valor2
    
    def menu(self):
        print('Operações artiméticas básicas')
        print('1 - Adição')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('S - SAIR')
    
    def executar(self):
        while True: 
            self.menu()
            opcao = input('Qual a opção? ')
            valor1, valor2 = self.ler_valores()
            if opcao == '1':
                resultado = self.soma(valor1, valor2)
            elif opcao == '2':
                resultado = self.subtrair(valor1, valor2)
            elif opcao == '3':
                resultado = self.multiplicar(valor1, valor2)
            elif opcao == '4':
                resultado = self.dividir(valor1, valor2)
            elif opcao.lower() == 's':
                break
            else:
                print('Opcao inválida!')
            print(f'Resultado da operação: {resultado}')