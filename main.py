# Piyodaning diagonal yurishi
def pawn(x1, y1, x2, y2):
    """Oddiy piyodaning yurishi: diagonal oldinga bir qadam"""
    return y2 - y1 == 1 and abs(x2 - x1) == 1


# Damkaning diagonal yurishi
def damka(x1, y1, x2, y2):
    """Damkaning yurishi: diagonalda har qanday masofa"""
    return abs(x2 - x1) == abs(y2 - y1)


# Harakatni tekshirish
def valid_move(piece, x1, y1, x2, y2):
    """Yurish mumkinligini tekshiradi: piyoda yoki damka"""
    if piece == "pawn":
        return pawn(x1, y1, x2, y2)
    elif piece == "damka":
        return damka(x1, y1, x2, y2)
    return False


# Foydalanuvchi uchun interaktiv harakat
print("Shashka harakat tekshiruvi")
print("Figuralar: 'pawn' (piyoda), 'damka' (damka)")
piece = input("Figurani tanlang (pawn yoki damka): ").strip().lower()

try:
    x1 = int(input("Boshlang'ich x koordinatasi (x1): "))
    y1 = int(input("Boshlang'ich y koordinatasi (y1): "))
    x2 = int(input("Yakuniy x koordinatasi (x2): "))
    y2 = int(input("Yakuniy y koordinatasi (y2): "))

    if valid_move(piece, x1, y1, x2, y2):
        print(f"{piece.capitalize()} ({x1},{y1} -> {x2},{y2}) yurishi to'g'ri!")
    else:
        print(f"{piece.capitalize()} ({x1},{y1} -> {x2},{y2}) yurishi noto'g'ri!")
except ValueError:
    print("Koordinatalar son bo‘lishi kerak!")