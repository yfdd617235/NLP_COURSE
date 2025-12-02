# Tokenization
texto = "Hola, ¿Cómo estás"
tokens = texto.split()
print(tokens) #['Hola,', '¿Cómo', 'estás']

# 2nd example
# Hola - hola
texto = "Hola, ¿Cómo estás"
texto = texto.lower()
tokens = texto.split()
print(tokens) #['hola,', '¿cómo', 'estás']