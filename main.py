import os


def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre} desde GitHub Actions!")


if __name__ == "__main__":
    main()