import secrets as sec
import string as str

# genera letras, digitos, caracteres
letra = str.ascii_letters
dig = str.digits
carac = str.punctuation


def generador_contraseñas(long):
    combinacion = letra + dig + carac  # mezcla digitos, letras, caracteres
    while True:
        pwd = ''.join(
            sec.choice(combinacion) for i in range(long))  # escoge elementos de 'combinacion' segun la longitud
        if (any(char in carac for char in pwd) and
                any(char in dig for char in pwd) and
                any(char in letra for char in pwd)):  # verifica si tiene algun digito, caracter, letra

            return pwd


contraseña = generador_contraseñas(12)  # longitud de la contraseña
print('Contraseña generada:')
print(contraseña)
print("hjgj")
