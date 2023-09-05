class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        num = space = 0

        for m in moves:
            if m == 'L':
                num -= 1
            elif m == 'R':
                num += 1
            else:
                space += 1

        return space + abs(num)