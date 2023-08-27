def prime_factors(n):
    """
        Returns a string representation of the prime factors of the input number `n`.

        Args:
            n (int): The number for which to find the prime factors.

        Returns:
            str: A string representation of the prime factors, enclosed in parentheses.
                Each factor is represented as `div**count`, where `div` is the prime factor
                and `count` is the number of times it appears in the factorization.

        Example:
            >>> prime_factors(7775460)
            '(2**2)(3**3)(5)(7**2)(11)(17)'

            >>> prime_factors(7919)
            '(7919)'
    """
    string = ""
    div = 2

    while n >= 2:
        count = 0
        while n % div ==0:
            n //= div
            count += 1

        if count > 0:
            if len(string) > 0:
                string += ''
            string += f'({div}{"**" + str(count) if count > 1 else ""})'
        div += 1
    return string


def main():
    print(f'Resultado de 7775460: {prime_factors(7775460)}')
    print(f'Resultado de 7919: {prime_factors(7919)}')

if __name__ == '__main__':
    main()