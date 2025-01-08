def pawn(x1, y1, x2, y2):
    return y2-y1==1 and abs(x2-x1)==1

def miniKing(x1, y1, x2, y2, is_damka=False):
    if is_damka:
        return abs(x2 - x1) == abs(y2 - y1)
    else:  
        return y2 - y1 == 1 and abs(x2 - x1) == 1
