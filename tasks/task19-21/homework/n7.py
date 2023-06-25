HEAP_SIZE = 25


def is_win(heap1: int, heap2: int, heap3: int, turn: int) -> bool:  # О нет, сигнатуры, какой кринж.
    if heap1 + heap2 + heap3 >= 73:
        return turn % 2 == 0  # Ход первого игрока?
    if not turn:
        return False  # Куча не заполнилась за заданное кол-во ходов.
    
    next_turns = [
        is_win(heap1 + 3, heap2, heap3, turn - 1),
        is_win(heap1 + 13, heap2, heap3, turn - 1),
        is_win(heap1 + 23, heap2, heap3, turn - 1),
        
        is_win(heap1, heap2 + 3, heap3, turn - 1),
        is_win(heap1, heap2 + 13, heap3, turn - 1),
        is_win(heap1, heap2 + 23, heap3, turn - 1),

        is_win(heap1, heap2, heap3 + 3, turn - 1),
        is_win(heap1, heap2, heap3 + 13, turn - 1),
        is_win(heap1, heap2, heap3 + 23, turn - 1),
        ]
    return any(next_turns) if (turn - 1) % 2 == 0 else all(next_turns)


def main():
    # print('19 -', min(x for x in range(1, HEAP_SIZE) if is_win(1, x, 2 * x, 2)))  # all -> any
    print('20 -', [x for x in range(2, HEAP_SIZE) if not is_win(2, x, 2 * x, 1) and is_win(2, x, 2 * x, 3)])
    print('21 -', [x for x in range(2, HEAP_SIZE) if not is_win(2, x, 2 * x, 2 ) and is_win(2, x, 2 * x, 4)])


main()