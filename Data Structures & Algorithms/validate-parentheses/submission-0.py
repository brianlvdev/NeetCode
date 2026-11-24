class Solution:
    def isValid(self, s: str) -> bool:
    # metodo de pilha
    # visto nao visto
        mapa = {"(": ")", "[": "]", "{": "}"}
        pilha = []
        for i in s:
            if i in mapa:
                pilha.append(i)
            elif i in mapa.values():
                if not pilha:
                    return False
                ult_aberto = pilha.pop()
                if mapa[ult_aberto] != i:
                    return False
        return len(pilha) == 0