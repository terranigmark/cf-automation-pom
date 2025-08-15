import os


def main():
    name = os.getenv("USERNAME")
    prin(f"Hola, {name}! Estoy en GitHub Actions!")


if __name__ == "__main__":
    main()