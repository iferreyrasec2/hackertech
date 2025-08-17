def fuerza_bruta_cesar(mensaje_cifrado):
    alfabeto = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'á',
        'é', 'í', 'ó', 'ú', ',', '.', ' '
    ]
    longitud_alfabeto = len(alfabeto)
    
    print("\nResultados de fuerza bruta para el mensaje:")
    print("------------------------------------------")
    
    for desplazamiento in range(1, longitud_alfabeto):
        mensaje_descifrado = []
        
        for caracter in mensaje_cifrado.lower():
            if caracter in alfabeto:
                indice_original = alfabeto.index(caracter)
                indice_descifrado = (indice_original - desplazamiento) % longitud_alfabeto
                mensaje_descifrado.append(alfabeto[indice_descifrado])
            else:
                mensaje_descifrado.append(caracter)  # Mantener caracteres no encontrados en el alfabeto
        
        print(f"Desplazamiento {desplazamiento}: {''.join(mensaje_descifrado)}")

# Solicitar mensaje al usuario
mensaje = input("Ingrese el mensaje cifrado: ")
fuerza_bruta_cesar(mensaje)