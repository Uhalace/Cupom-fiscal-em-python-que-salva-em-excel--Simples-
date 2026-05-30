
from dependencias.Porcess.Validation import Validate
from dependencias.Base.BD import Temp

temp =Temp.temp

e_numero = Validate.e_numero

class Salvar:
    @staticmethod
    def salvar_dados(numero: int, ordem: int, item: str,quantidade: float, valor:float):

        campos ={
            'numero': numero,
            'ordem': ordem,
            'quantidade': quantidade,
            'valor': valor
        }

        for nome_campo, valor_campo in campos.items():
            if not e_numero(valor_campo):
                return f"Atenção o campo {nome_campo}, possui um valor invalido"
                
        temp.append([numero, ordem, item, quantidade, valor])
        return "Dados salvos com sucesso"