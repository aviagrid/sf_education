import numpy as np
from numpy import random


def random_predict(number:int=1) -> int:
    """The computer guesses a random number

    Args:
        number (int, optional): 
            The hidden number. Defaults to 1.

    Returns:
        int: 
            The number of attempts
    """
    count = 0
    while True:
        count += 1  
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
        print('...wait...')
    return (count)


def score_game(random_predict) -> int:
    """Calculating the average number of 1000 guessing attempts by the computer

    Args:
        random_predict ([function]): 
            The computer guesses a random number

    Returns:
        int: 
            Average score
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за - {score} попыток.')
    
    return (score)

score_game(random_predict)