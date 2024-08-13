class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort() # [2,3,5,7,11,13,17]
        q = deque(range(len(deck))) # [0,1,2,3,4,5,6] if len(deck) = 7

        res = [0] * len(deck) # [0,0,0,0,0,0,0]
        for card in deck:
            popIndex = q.popleft() # [1,2,3,4,5,6]
            res[popIndex] = card # [2,0,0,0,0,0,0]
            if q:
                q.append(q.popleft()) # [2,3,4,5,6,1]

        return res

    # dq = collections.deque()

    #     for card in reversed(sorted(deck)):
    #       dq.rotate()
    #       dq.appendleft(card)

    #     return list(dq)