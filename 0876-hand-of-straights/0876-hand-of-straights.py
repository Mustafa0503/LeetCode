class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        card_count = Counter(hand)
        sorted_cards = sorted(card_count)
        
        for card in sorted_cards:
            if card_count[card] > 0:
                count = card_count[card]
                for i in range(groupSize):
                    if card_count[card + i] < count:
                        return False
                    card_count[card + i] -= count
                    
        return True