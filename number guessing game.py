import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0

    print("Selamat datang di permainan tebak angka!")
    print("Saya telah memilih angka antara 1 dan 100. Coba tebak angkanya!")

    while True:
        try:
            guess = int(input("Masukkan tebakan Anda: "))
            attempts += 1

            if guess < target_number:
                print("Tebakan Anda terlalu rendah. Coba angka yang lebih tinggi.")
            elif guess > target_number:
                print("Tebakan Anda terlalu tinggi. Coba angka yang lebih rendah.")
            else:
                print(f"Selamat! Anda berhasil menebak angka {target_number} dalam {attempts} percobaan.")
                break

        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

number_guessing_game()
