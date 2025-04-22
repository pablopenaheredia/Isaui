from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res

# Pedimos los datos al usuario
entrada = input("Ingresá los valores del array separados por coma (por ejemplo: 1,8,6,2,5,4,8,3,7): ")
# Convertimos a lista de enteros
altura = list(map(int, entrada.split(',')))

sol = Solution()
resultado = sol.maxArea(altura)
print("La mayor cantidad de agua que puede contener es:", resultado)
