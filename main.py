#=========================================================
#      SISTEMA NOTA FISCAL EM PYTHON V1
#      @AUTOR: UHALACE DE SOUZA
#==========================================================

from typing import List, Any

#==========================================================
#                       DEPENDÊNCIAS
#==========================================================
from dependencias.Base.BD import Temp
from dependencias.Porcess.Validation import Validate
from dependencias.Porcess.Salvar import Salvar
from dependencias.Forms.CadItem import CadastroItem
from dependencias.Export.Excel import Excel



nomeCliente = str(input("Digite o nome do cliente: "))
CPFd = str(input("Digite o CPF do cliente: "))

CPFformatado = Validate.CPF_format(CPFd)


numero_da_nota = CadastroItem.numero_nota()

CadastroItem.iniciar_cadastro(numero_da_nota)

salvar = str(input("Deseja salvar em excel? (s/n): ")).strip().lower()
while salvar not in ["s", "n"]:
    print("Opção invalida")
    salvar = str(input("Deseja salvar em excel? (s/n): ")).strip().lower()

if salvar == "s":
    Excel.salvar_excel(Temp.temp, numero_da_nota, nomeCliente, CPFformatado)




     