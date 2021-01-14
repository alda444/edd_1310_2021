def cuenta_regresiva(num):
    if num >= 0:
        print(f"Esto comienza en {num} segundos")
        cuenta_regresiva(num-1)
    else:
        print("Empezamos")

def main():
    cuenta_regresiva(10)

main()
