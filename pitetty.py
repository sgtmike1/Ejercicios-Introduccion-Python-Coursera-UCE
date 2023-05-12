print("Bievenidos a PITETTY ONLINE -  ")
print("""
 __      __       .__                                  __
/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/
       \/       \/          \/            \/     \/
__________.__  __          __    __
\______   \__|/  |_  _____/  |__/  |_ ___.__.
 |     ___/  \   __\/ __ \   __\   __<   |  |
 |    |   |  ||  | \  ___/|  |  |  |  \___  |
 |____|   |__||__|  \___  >__|  |__|  / ____|
                        \/            \/     """)

print("Para comenzar te vamos a pedir una serie de datos personales (que prometemos no robar)")
nombre = str(input("Escribe tu nombre aqui: "))
bienV = "Bienvenido!"
aDD = "Solo unas preguntas más y estaras participando de PITETTY"
print("*--*--*-*-*--*--*-*-*--*--*-*-*--*--*-*-*--*--*-*-")
print(bienV, nombre, aDD)
print("*--*--*-*-*--*--*-*-*--*--*-*-*--*--*-*-*--*--*-*-")
fechaNac = int(input("En que año naciste?"))
edad = 2023 - fechaNac - 1
aDD2 = "Tu edad segun el año digitado es:"
print(aDD2, edad),
print("*--*--*-*-*--*--*-*-*--*--*-*-*--*--*-*-*--*--*-*-")
print("Dinos tu estatura en metros.")
estatura = float(input("Ingrese aqui su estatura:"))
estatura_cm = estatura * 100
aDD3 = "Tu estatura en CM es:"
print(aDD3, estatura_cm)
print("*--*--*-*-*--*--*-*-*--*--*-*-*--*--*-*-*--*--*-*-")
telefono = int(input("Ingresa un numero de telefono para poder registrarte: "))
aDD4 = "Tu telefono es: "
print(aDD4, telefono)
print("*--*--*-*-*--*--*-*-*--*--*-*-*--*--*-*-*--*--*-*-")
telefono2 = str(input("Ingresa tu correo electronico:"))
aDD5 = "El correo ingresado es:"
print(aDD5 + telefono2 + " Gracias por registrarte")
print("*--*--*-*-*--*--*-*-*--*--*-*-*--*--*-*-*--*--*-*-")
print("""""
|  | _______  ______ ______ |__|/  |______
|  |/ /\__  \ \____ \\____ \|  \   __\__  \
|    <  / __ \|  |_> >  |_> >  ||  |  / __ \_
|__|_ \(____  /   __/|   __/|__||__| (____  /
     \/     \/|__|   |__|                 \/ """"")
print("Te has registrado en PITETTY CORRECTAMENTE!")
