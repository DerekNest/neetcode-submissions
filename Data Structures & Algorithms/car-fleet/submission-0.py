class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        n = len(position)
        cars = []
        
        for i in range(n):
            time = (target - position[i]) / speed[i]
            cars.append([position[i], time])
          
        cars.sort(reverse=True)
        
        stack = []
        
        for i in range(n):
            current_time = cars[i][1]

            if not stack or current_time > stack[-1]:
                stack.append(current_time)
                
        return len(stack)