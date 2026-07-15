class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        
        for i in range(n):
            time = (target-(position[i])) / speed[i]
            cars.append((position[i], time))

        cars.sort(reverse=True)
        stack = []

        for i, time in cars:
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)


