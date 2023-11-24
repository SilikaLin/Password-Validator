import unittest

from validador_senha import ValidadorSenha

def test_validador_senha():
    validador = ValidadorSenha()

    assert validador.validar_senha("Senha123@") == True  # Senha válida com caractere especial
    assert validador.validar_senha("Abcdefg1!") == True  # Senha válida com caractere especial
    assert validador.validar_senha("Teste@1234") == True  # Senha válida com caractere especial

    assert validador.validar_senha("senha") == False  # Menos de 8 caracteres
    assert validador.validar_senha("SENHA123") == False  # Sem letra minúscula
    assert validador.validar_senha("senhaabcd") == False  # Sem número
    assert validador.validar_senha("12345678") == False  # Sem letra maiúscula e minúscula
    assert validador.validar_senha("Senha@") == False  # Sem número
    assert validador.validar_senha("Senha1234") == False  # Sem caractere especial
    assert validador.validar_senha("Senha&1234") == False  # Sem letra maiúscula
    assert validador.validar_senha("Senha#abcd") == False  # Sem letra minúscula

    assert validador.validar_senha("Senha@123") == True  # Senha válida com caractere especial
    assert validador.validar_senha("Senha1234") == False  # Sem caractere especial
