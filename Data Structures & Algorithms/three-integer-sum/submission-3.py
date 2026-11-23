class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        saida = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            esquerda = i + 1
            direita = len(nums) - 1
            
            while esquerda < direita:
                soma = nums[i] + nums[esquerda] + nums[direita]
                
                if soma < 0:
                    esquerda += 1
                elif soma > 0:
                    direita -= 1
                else:
                    saida.append([nums[i], nums[esquerda], nums[direita]])
                    esquerda += 1
                    direita -= 1
                    while esquerda < direita and nums[esquerda] == nums[esquerda - 1]:
                        esquerda += 1
                        
        return saida
