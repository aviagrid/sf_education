import numpy as np


def random_predict(number:int=1) -> int:
    """The computer guesses a random number

    Args:
        number (int, optional): 
            The hidden number. Defaults to 1.

    Returns:
        int: 
            The number of attempts
    """
    # Инициализируем границы поиска случайным методом
    # Так, что бы left_border < number > right_border
    right_border = 101
    left_border = 0
    
    # Идея алгоритма заключается в постоянном сужении области поиска
    # предсказываемого числа
    attempt_cnt = 0
    while True:
        attempt_cnt += 1  
        predict_number = np.random.randint(left_border, right_border+1)
        if number == predict_number:
            break
        elif number > predict_number:
            if left_border < number and predict_number > left_border:
                left_border = predict_number
        elif number < right_border:
            if right_border > number and predict_number < right_border:
                right_border = predict_number
                
    return (attempt_cnt)


def score_game(random_predict) -> int:
    """Calculating the average number of 10000 guessing attempts by the computer

    Args:
        random_predict ([function]): 
            The computer guesses a random number

    Returns:
        int: 
            Average score
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(10000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за - {score} попыток.')
    
    return (score)

score_game(random_predict)