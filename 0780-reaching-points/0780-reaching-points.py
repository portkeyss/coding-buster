class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if tx < sx or ty < sy:
            return False
        while True:
            if tx == sx and ty == sy:
                return True
            if tx > ty:
                if tx - ty < sx:
                    return False # the only possible one step backward transformation fails
                k = (tx - sx) // ty
                tx, ty = tx - k * ty, ty
            elif tx < ty:
                if ty - tx < sy:
                    return False
                k = (ty - sy) // tx
                tx, ty = tx, ty - k * tx
            else:
                return False