class Validate:
    
    def e_numero(valor: float) -> bool:
        return isinstance(valor, (int, float)) and not isinstance(valor, bool)
    def CPF_format(CPF: str):
        if len(CPF) == 11:
            return f"{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:]}"
        else:
            return CPF