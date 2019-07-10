# TCS codevita 2018 inverses
ONES = [
    None, 'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine'
]

TEENS = [
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
]

TENS = [
    None, None, 'twenty', 'thirty', 'forty',
    'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
]

POWERS_OF_1000 = [
    None, 'thousand', 'million', 'billion', 'trillion',
    'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion'
]

def number_to_chunks(number):
    """
    Split an integer into little-endian base-1000 chunks.

    >>> list(number_to_chunks(1234))
    [234, 1]
    >>> list(number_to_chunks(31415000))
    [0, 415, 31]
    >>> list(number_to_chunks(0))
    []
    """
    while number:
        number, n = divmod(number, 1000)
        yield n

def chunk_to_words(chunk, scale):
    """
    Generate English words given a chunk (an integer less than 1000) and its
    scale (power of 1000).

    >>> list(chunk_to_words(31, 1))
    ['thirty', 'one', 'thousand']
    >>> list(chunk_to_words(50, 2))
    ['fifty', 'million']
    >>> list(chunk_to_words(0, 0))
    []
    >>> list(chunk_to_words(12, 3))
    ['twelve', 'billion']
    """
    assert 0 <= chunk < 1000
    hundreds, tens, ones = chunk // 100, chunk // 10 % 10, chunk % 10

    if hundreds:
        yield ONES[hundreds]
        yield 'hundred'

    if tens == 1:
        yield TEENS[ones]
    else:
        if tens:
            yield TENS[tens]
        if ones:
            yield ONES[ones]

    if chunk and scale:
        yield POWERS_OF_1000[scale]

def number_to_words(number):
    """
    Convert a nonnegative integer less than 10**30 to an English phrase.

    >>> number_to_words(103)
    'one hundred three'
    >>> number_to_words(0)
    'zero'
    >>> number_to_words(1_000_001)
    'one million one'
    >>> number_to_words(31_415_926_535)
    'thirty one billion four hundred fifteen million nine hundred twenty six thousand five hundred thirty five'
    """
    chunks = [
        ' '.join(chunk_to_words(chunk, i))
        for i, chunk in enumerate(number_to_chunks(number))
    ]
    return ' '.join(c for c in chunks[::-1] if c) or 'zero'


def checking(a,b):
    if (number_to_words(a) == number_to_words(b)):
        print(a)

    elif (number_to_words(a) > number_to_words(b)):
        k = a
        l = b
        a = a+l
        b = b+k
        checking(a,b)
    else :
        a = a+a
        b = b+b 
        checking(a,b)

if __name__ == "__main__":
    a, b = map(int,input().split())
    checking(a,b)
   
    

