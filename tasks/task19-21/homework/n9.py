HEAP_SIZE = 2163


def is_win(heap: int, turn: int) -> bool:  # О нет, сигнатуры, какой кринж.
    if heap >= HEAP_SIZE:
        return turn % 2 == 0  # Ход первого игрока?
    if not turn:
        return False  # Куча не заполнилась за заданное кол-во ходов.
    
    next_turns = [
        is_win(heap + 1, turn - 1),
        is_win(heap * 3, turn - 1),
        ]
    return any(next_turns) if (turn - 1) % 2 == 0 else all(next_turns)


def main():
    print('19 -', [x for x in range(1, HEAP_SIZE) if not is_win(x, 1) and is_win(x, 2)])
    print('20 -', [x for x in range(1, HEAP_SIZE) if not is_win(x, 1) and is_win(x, 3)])
    print('21 -', [x for x in range(1, HEAP_SIZE) if not is_win(x, 2) and is_win(x, 4)])


main()