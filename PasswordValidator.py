class ValidadorSenha:
    def validar_senha(self, senha):
        if len(senha) < 8:
            return False

        tem_maiuscula = False
        tem_minuscula = False
        tem_digito = False
        tem_caracter_especial = False

        for caractere in senha:
            if caractere.isupper():
                tem_maiuscula = True
            elif caractere.islower():
                tem_minuscula = True
            elif caractere.isdigit():
                tem_digito = True
            else:
                tem_caracter_especial = True

        return tem_maiuscula and tem_minuscula and tem_digito and tem_caracter_especial
