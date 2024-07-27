def toBits(text) -> list[str]:
    text_in_binary: list[str] = []

    for symbol in text:
        binary: str = bin(ord(symbol))[2:]
        text_in_binary.append((8-len(binary))*"0" + binary) # Makes all binary strings 8 bits long
    
    return text_in_binary


def encryption(text_in_binary, key_in_binary) -> str:
    symbol_count = 0
    len_of_key = len(key_in_binary)
    encrypted_text: str = ""

    value: int = 0
    for key_symbol in key_in_binary:
        value = value + int(key_symbol, 2)

    for symbol in text_in_binary:
        encrypted_text += chr(int(symbol, 2) + value + int(key_in_binary[symbol_count], 2))

        symbol_count += 1
        if symbol_count == len_of_key:
            symbol_count = 0
    
    return encrypted_text


def decryption(encrypted_text, key_in_binary) -> str:
    decrypted_text: str = ""
    symbol_count = 0
    len_of_key = len(key_in_binary)

    value: int = 0
    for symbol in key_in_binary:
        value = value + int(symbol, 2)
    
    for symbol in encrypted_text:
        decrypted_text += str(chr(ord(symbol) - value - int(key_in_binary[symbol_count], 2)))

        symbol_count += 1
        if symbol_count == len_of_key:
            symbol_count = 0
        
    return decrypted_text


def main() -> None:
    text = "jkjijfus1234~"
    key = "SamoJeKralj" # MIN length is 6 and MAX is 30

    text_in_binary: list[str] = toBits(text)
    key_in_binary: list[str] = toBits(key)
    encrypted_text: str = encryption(text_in_binary, key_in_binary)
    print(encrypted_text)
    decrypted_text: str = decryption(encrypted_text, key_in_binary)
    print(decrypted_text)


if __name__ == "__main__":
    main()