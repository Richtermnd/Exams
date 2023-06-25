from math import ceil


HEAP_SIZE = 1000


def is_win(heap1: int, heap2: int, turn: int) -> bool:  # О нет, сигнатуры, какой кринж.
    if heap1 + heap2 <= 20:
        return turn % 2 == 0  # Ход первого игрока?
    if not turn:
        return False  # Куча не заполнилась за заданное кол-во ходов.
    
    next_turns = [
        is_win(heap1 - 1, heap2, turn - 1),
        is_win(ceil(heap1 / 2), heap2, turn - 1),

        is_win(heap1, heap2 - 1, turn - 1),
        is_win(heap1, ceil(heap2 / 2), turn - 1),
        ]
    return any(next_turns) if (turn - 1) % 2 == 0 else all(next_turns)


def main():
    print('19 -', [x for x in range(11, HEAP_SIZE) if is_win(10, x, 2)])
    print('20 -', [x for x in range(11, HEAP_SIZE) if not is_win(10, x, 1) and is_win(10, x, 3)])
    print('21 -', [x for x in range(11, HEAP_SIZE) if not is_win(10, x, 2) and is_win(10, x, 4)])


main()
