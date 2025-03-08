def int_to_char():
    try:
        num = int(input("Enter an integer (0-255): "))  # Kullanıcıdan bir tam sayı al
        if 0 <= num <= 255:
            char = chr(num)  # Tam sayıyı karaktere çevir
            if char.isprintable():  # Eğer karakter ekrana basılabilir bir karakterse
                print(f"The corresponding character is: {char}")
            else:  # Eğer görünmeyen bir karakterse, ASCII kodunu gösterelim
                print(f"The corresponding character is a non-printable ASCII character (Code: {num})")
        else:
            print("Error: Please enter a number between 0 and 255.")
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    int_to_char()
