from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return flowerbed[0] == 0

        for index in range(0, len(flowerbed)):
            if index == 0:
                if flowerbed[index] == 0 and flowerbed[index + 1] == 0:
                    flowerbed[index] = 1
                    n -= 1
            elif index == len(flowerbed) - 1:
                if flowerbed[index - 1] == 0 and flowerbed[index] == 0:
                    flowerbed[index] = 1
                    n -= 1
            else:
                if flowerbed[index] == 0 and flowerbed[index - 1] == 0 and flowerbed[index + 1] == 0:
                    flowerbed[index] = 1
                    n -= 1

        return n <= 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.canPlaceFlowers([0,0,1,0,0], 1))
