import time


def decoradora(function):
    def wrapper(*args, **kwargs):
        inicio = time.time()

        resultado = function(*args, **kwargs)

        tiempo_total = time.time() - inicio
        print(f"La demora de ejecución fue de: {tiempo_total}")

        return resultado

    return wrapper


@decoradora
def division(a, b):
    time.sleep(2)  # Pausa la ejeción del código por 1 segundo
    division = a / b
    return division


print(division(20, 2))
print(division(10, 5))
