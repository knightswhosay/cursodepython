content = input('Digite algo ')

print(f'É um número {content.isnumeric()}\nsó tem espaços? {content.isspace()}\nÉ Alpha {content.isalpha()}\nÉ alphanumérioco?{content.isalnum()}\nEstá em maíscula?{content.isupper()}\nEstá em letras minúsculas? {content.islower()}\nEstá captalizado? {content.istitle()}')