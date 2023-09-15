def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    words = phrase.lower().split()
    capitalized_words = []

    for word in words:
        capitalized_words.append(word.capitalize())
    return ' '.join(capitalized_words)


titleize('this is awesome')
titleize('oNLy cAPITALIZe fIRSt')
