import re

thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'

regex_pattern = r"%s%s%s%s$" % (thousand, hundred, ten, digit)

    # regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"
