from dependencias.Porcess.Validation import Validate
from dependencias.Porcess.Salvar import Salvar
from dependencias.Base.BD import Temp

class CadastroItem:
    
    @staticmethod
    def numero_nota():
        while True:
            try:
                numeronota = int(input("Digite o numero da nota: "))
                break
            except ValueError:
                print("Valor invalido, digite um numero inteiro")
                
        return numeronota
    
    @staticmethod
    def iniciar_cadastro(numeronota):  
      
        temp = Temp.temp        
        continuar = "s"

        while continuar == "s":
            nomeitem = str(input("Digite o nome do item: "))
            
            while True:
                try:
                    valoritem = float(input("Digite o valor do Item: "))
                    break
                except ValueError:
                    print("Valor invalido, digite um numero inteiro ou decimal")
      
            while True:
                try:
                    quantvalor = float(input("Digite a quantidade do item: "))
                    break
                except ValueError:
                    print("Valor invalido, digite um numero inteiro ou decimal")
            
            ordem = len(temp) + 1
            adicionar = Salvar.salvar_dados(numeronota, ordem, nomeitem, quantvalor, valoritem)
            print(adicionar)
            
            continuar = str(input("Deseja continuar?(s/n) ")).strip().lower()
            while continuar not in ["s", "n"]:
                print("Opção invalida")
                continuar = str(input("Deseja continuar?(s/n) ")).strip().lower()
        
       