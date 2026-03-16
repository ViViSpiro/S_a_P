# Классы исключений
class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

# Функция для определения победителя в игре Камень-Ножницы-Бумага
def rps_game_winner(players):
    # Проверка количества игроков (должно быть ровно 2)
    if len(players) != 2:
        raise WrongNumberOfPlayersError
    
    # Извлекаем ходы игроков
    player1_name, player1_move = players[0]
    player2_name, player2_move = players[1]
    
    # Проверка допустимости ходов (только R, P, S)
    valid_moves = ['R', 'P', 'S']
    if player1_move not in valid_moves or player2_move not in valid_moves:
        raise NoSuchStrategyError
    
    # Если ходы одинаковые, побеждает первый игрок
    if player1_move == player2_move:
        return f"{player1_name} {player1_move}"
    
    # Правила игры:
    # R (камень) побеждает S (ножницы)
    # S (ножницы) побеждают P (бумагу)
    # P (бумага) побеждает R (камень)
    if (player1_move == 'R' and player2_move == 'S') or \
       (player1_move == 'S' and player2_move == 'P') or \
       (player1_move == 'P' and player2_move == 'R'):
        return f"{player1_name} {player1_move}"
    else:
        return f"{player2_name} {player2_move}"


# Получаем входные данные
try:
    players = eval(input())
    print(rps_game_winner(players))
except WrongNumberOfPlayersError:
    print("WrongNumberOfPlayersError")
except NoSuchStrategyError:
    print("NoSuchStrategyError")