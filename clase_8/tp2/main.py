from clase_cliente import Cliente
BD = {}
import json
def main():
    cliente = Cliente("admin123", "Nicolas", 23)
    print(cliente)
    cliente.login(BD)
    cliente.mostrar_informacion()
    if opcion == 3:
        mostrar_usuarios(BD)
    sistema.crear_usuario("nicolas", "admin123") # - Cliente(usuario, contraseña)
                                                 # BD[...] = Cliente
                                                 
                                                 
main()                                             
# cd - Me muevo por la terminal
# ls - Listo los archivos / carpetas de donde estoy "parado".