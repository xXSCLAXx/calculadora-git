"""Calculadora sencilla para usar desde la consola."""


def calcular(numero1: float, operador: str, numero2: float) -> float:
    """Realiza una operación básica y devuelve el resultado."""
    if operador == "+":
        return numero1 + numero2
    if operador == "-":
        return numero1 - numero2
    if operador == "*":
        return numero1 * numero2
    if operador == "/":
        if numero2 == 0:
            raise ValueError("No se puede dividir entre cero.")
        return numero1 / numero2
    raise ValueError("Operador no válido. Usa +, -, * o /.")


def main() -> None:
    """Ejecuta la calculadora interactiva."""
    print("Calculadora sencilla")
    print("Escribe 'salir' como operador para terminar.")

    while True:
        try:
            numero1 = float(input("\nPrimer número: "))
            operador = input("Operación (+, -, *, /): ").strip()

            if operador.lower() == "salir":
                print("¡Hasta luego!")
                break

            numero2 = float(input("Segundo número: "))
            resultado = calcular(numero1, operador, numero2)
            print(f"Resultado: {resultado:g}")
        except ValueError as error:
            print(f"Error: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\n¡Hasta luego!")
            break


if __name__ == "__main__":
    main()
