"""
LeetCode Problem #1510: Stone Game IV

Alice and Bob take turns playing a game, with Alice starting first.
Initially, there are n stones in a pile.  On each player's turn, that player makes
a move consisting of removing any non-zero square number of stones in the pile.
Also, if a player cannot make a move, he/she loses the game.
Given a positive integer n. Return True if and only if Alice wins the game otherwise
return False, assuming both players play optimally.

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile.  On each player's turn, that player makes
a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.
Given a positive integer n. Return True if and only if Alice wins the game otherwise
return False, assuming both players play optimally.

Example 1:
Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.

Example 2:
Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one
winning the game (2 -> 1 -> 0).

Example 3:
Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing
4 stones (4 -> 0).

Example 4:
Input: n = 7
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
If Alice starts removing 4 stones, Bob will remove 1 stone then Alice should remove
only 1 stone and finally Bob removes the last one (7 -> 3 -> 2 -> 1 -> 0).
If Alice starts removing 1 stone, Bob will remove 4 stones then Alice only can remove
1 stone and finally Bob removes the last one (7 -> 6 -> 2 -> 1 -> 0).

Example 5:
Input: n = 17
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
"""
import math


class Solution:

    def __init__(self):
        self.n = None

    @staticmethod
    def perfect_square(num):
        if math.sqrt(num) - int(math.sqrt(num)) == 0:
            return True
        else:
            return False

    def nearest_perfect_square(self, num):  # returning the perfect sqr near the given no. n
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

        diff = self.n - self.nearest_perfect_square(num)

        if (diff in [1, 3]) or self.perfect_square(diff):
            return self.rmv_opt_num(self.nearest_perfect_square(num) - 1)
        else:
            return self.nearest_perfect_square(num)

    def winner_square_game(self, n: int) -> bool:

        if n == self.nearest_perfect_square(n):
            return True
        if n in [1, 3]:
            return True
        elif n in [2, 5]:
            return False

        count = 0
        while 1:
            self.n = n
            n -= self.rmv_opt_num(n)
            # print(self.rmv_opt_num(n))
            count += 1
            if count % 2 == 0:  # is even?
                if n in [1, 3] or self.perfect_square(n):
                    return True
                elif n == 2:
                    return False

            else:  # no it's odd
                if n in [1, 3] or self.perfect_square(n):
                    return False
                elif n == 2:
                    return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.winner_square_game(47))
