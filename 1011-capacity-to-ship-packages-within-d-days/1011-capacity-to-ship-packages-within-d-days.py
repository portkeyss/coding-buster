class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        low, high = max(weights), sum(weights)
        while low < high:
            mid = (low + high) // 2
            curShipment = 0
            shipmentCount = 1
            for w in weights:
                if w+curShipment <= mid:
                    curShipment += w
                else:
                    curShipment = w
                    shipmentCount += 1
                    if shipmentCount > D:
                        break
            if shipmentCount <= D:
                high = mid
            else:
                low = mid + 1
        return low