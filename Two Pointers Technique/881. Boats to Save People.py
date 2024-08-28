class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        b = 0
        while l <= r:
            b += 1
            if people[l] + people[r] <= limit:  # at most 2 in a boat
                l += 1
                r -= 1
            else:
                r -= 1  #  only the heavier person go to the boat
        return b
