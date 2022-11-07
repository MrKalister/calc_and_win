from random import randint


def set_enemy_health():
    return randint(80, 120)


def get_lite_attack():
    return randint(2, 5)


def get_mid_attack():
    return randint(15, 25)


def get_hard_attack():
    return randint(30, 40)


def calc_diff(enemy_health, user_total_attack):
    return enemy_health - user_total_attack


def compare_valumes(point_difference):
    if point_difference <= 0:
        return True
    return False


def get_user_attack():
    total = 0
    attacks_types = {
        'lite': get_lite_attack,
        'mid': get_mid_attack,
        'hard': get_hard_attack,
    }

    for i in range(5):
        input_attack = input('Введи тип атаки: ').lower()
        attack_value = attacks_types[input_attack]()
        print(f'Количество очков твоей атаки: {attack_value}.')
        total += attack_value
    return total


def run_game():
    user_total_attack = get_user_attack()
    enemy_health = set_enemy_health()
    print(f'Очки здоровья противника: {enemy_health}.')
    print(f'Тобой нанесён урон противнику равный {user_total_attack}.')
    left_points = calc_diff(enemy_health, user_total_attack)
    win = compare_valumes(left_points)
    if win:
        print('Ура! Победа за тобой!')
    else:
        print('В этот раз не повезло :( Бой проигран.')
        print(f'У противника осталось: {left_points} очков здоровья')
    yes_no = {
        'Y': True,
        'N': False,
    }
    replay = input('Чтобы сыграть ещё раз, введи "y"; '
                   'если не хочешь продолжать игру, введи "n": ').upper()
    if replay not in yes_no:
        raise ValueError('Такой команды в игре нет.')
    return yes_no[replay]
