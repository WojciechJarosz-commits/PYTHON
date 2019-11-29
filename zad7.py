def person_print(name, last_name, *others, age):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name,last_name,age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)

    person_print('Wojciech', 'Jarosz', 'student', '22')


    def args(x, *y):
        print(x)
        print(y)

    args('Wojciech', 'Jarosz', 'student', '22')

    def kwargs(x, **z):
        print(x)
        print(z)


    kwargs('Wojciech', a='Jarosz', b='student')

    def argsandkwargs(x, *y, **z):
        print(x)
        print(y)
        print(z)

        argsandkwargs('Wojciech', 'Jarosz', 'student','Wojtek',a='Jaro', b='uczeń', c='23')