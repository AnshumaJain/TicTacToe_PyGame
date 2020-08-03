"""
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there are n stones in a pile.  On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.
Also, if a player cannot make a move, he/she loses the game.
Given a positive integer n. Return True if and only if Alice wins the game otherwise return False, assuming both players play optimally.

"""
import math


class Solution:

    def perfect_square(self, num):
        if math.sqrt(num) - int(math.sqrt(num)) == 0:
            return True
        else:
            return False

    def lar_nearestPerfSqr_to(self, num):  # returning the perfect sqr near the given no. n
        if self.perfect_square(num):
            return num
        else:
            i = 1
            while 1:
                x = num - i
                if self.perfect_square(x):
                    return x
                else:
                    i += 1

    def rmv_opt_num(self, num):

        Diff = self.n - self.lar_nearestPerfSqr_to(num)

        if (Diff in [1, 3]) or (self.perfect_square(Diff) == True):
            return self.rmv_opt_num(self.lar_nearestPerfSqr_to(num) - 1)
        else:
            return self.lar_nearestPerfSqr_to(num)

    def winnerSquareGame(self, n: int) -> bool:

        if n == self.lar_nearestPerfSqr_to(n):
            return True
        if n in [1, 3]:
            return True
        elif n in [2, 5]:
            return False

        count = 0
        while 1:
            self.n = n
            n -= self.rmv_opt_num(n)
            print(self.rmv_opt_num(n))
            count += 1
            if count % 2 == 0:  # is even?
                if n in [1, 3] or self.perfect_square(n) == True:
                    return True
                elif n == 2:
                    return False

            else:  # no it's odd
                if n in [1, 3] or self.perfect_square(n) == True:
                    return False
                elif n == 2:
                    return True


object = Solution()
# print(lar_nearestPerfSqr_to())
# print(perfect_square(lar_nearestPerfSqr_to()))
# print(rmv_opt_num())
print(object.winnerSquareGame(47))