class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        inicio = 0
        fim = len(numbers) -1

        while inicio < fim:
            soma = numbers[inicio] + numbers[fim]
            if soma == target:
                return[inicio + 1, fim + 1]
            elif soma < target:
                inicio += 1
            else:
                fim -= 1
