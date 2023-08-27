

def score(dice):
    """
        Calculates the total score based on the values in the dice list.
        Args:
            dice (list): A list of integers representing the values on the dice.
        Returns:
            int: The total score calculated based on the values in the dice list.
        Example Usage:
            >>> print(score([5, 1, 3, 4, 1]))
            250
            >>> print(score([1, 1, 1, 3, 1]))
            1100
            >>> print(score([2, 3, 4, 6, 2]))
            0
            >>> print(score([4, 4, 4, 3, 3]))
            400
    """

    total_score = 0
    for number in range(1, 7, 1):
        reps = dice.count(number)
        if reps >= 3:
            if number == 1:
                total_score += number * 1000
            else:
                total_score += number * 100
            reps -= 3
        if number == 1:
            total_score += reps * 100
        if number == 5:
            total_score += reps * number * 10

    return total_score

def main():
    print(score([5, 1, 3, 4, 1]))
    print(score([1, 1, 1, 3, 1]))
    print(score([2, 3, 4, 6, 2]))
    print(score([4, 4, 4, 3, 3]))

if __name__ == '__main__':
    main()