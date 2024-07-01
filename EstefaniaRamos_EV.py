import os
os.system("cls")
#1.Registrar vehiculos
#2.ingresar datos vehiculo
#3.Calcular automaticamente
#4.listar los vehiculos
#6.Salir del programa
vehiculos = [
    ["marca","año","kilometraje","costo reparacion","impuesto","total"]
]
marcas = ["Toyota","Ford","Chevrolet"]
def registrar_vehiculo():
    while True:
        try:
            marca = input("ingrese la marca del vehiculo: ")
            ano = int(input("ingrese el año de fabricacion: "))
            kilometraje = int(input("ingrese el kilometraje: "))
            costo_reparacion = float(input("ingrese el costo de reparacion: "))
            if len(marca) <1 or ano <0 or kilometraje <0 or costo_reparacion <0:
                print("Error,ingrese los datos nuevamente")
                return
            impuesto = round(0.08 * costo_reparacion)
            total = round(costo_reparacion + impuesto)
            vehiculos.append([marca, ano, kilometraje, costo_reparacion, impuesto, total])
            if marca not in marcas:
                marcas.append(marca)
            break
        except ValueError:
            print("Error,favor ingrese numeros")
        except Exception as e:
            print(f"Error: {e}")
def listar_vehiculos():
    for vehiculo in vehiculos:
        print(f"{vehiculo[0]:<20} | {vehiculo[1]:<20} | {vehiculo[2]:<20} | {vehiculo[3]:<20} | {vehiculo[4]:<20} | {vehiculo[5]:<20}\n")
        print("----------*10")
def imprimir_orden_reparacion():
    contador=1
    for marca in marcas:
        print(f"{contador} - {marca}")
        contador+=1
    try:
        opc = int(input("Ingrese la marca para imprimir orden (0 para todo): "))-1
        if opc < -1 or opc >= len(marcas):
            print("NO ES VALIDO")
            return
        marca_seleccionada = marcas[opc] if opc != -1 else "todas"
        with open(f"orden_reparacion_{marca_seleccionada}.txt", "w") as archivo:
            archivo.write(f"orden de reparación para: {marca_seleccionada}\n")
            for vehiculo in vehiculos:
                if opc == -1 or vehiculo[0] == marca_seleccionada:
                    archivo.write(f"{vehiculo[0]:<20} | {vehiculo[1]:<20} | {vehiculo[2]:<20} | {vehiculo[3]:<20} | {vehiculo[4]:<20} | {vehiculo[5]:<20}\n")
                    archivo.write("----------------------------------------------------------------------------------------------------------------------\n")
            archivo.write("FIN\n")
        print(f"archivo'orden_reparacion_{marca_seleccionada}.txt' generado con exito")
    except ValueError:
        print("error, ingrese un valor numerico")
    except Exception as e:
        print(f"error inesperado: {e}")
def menu():
    menu = """
    ----- Taller de Mecanica Automotriz -----
    1.-registrar vehiculo
    2.-listar vehiculos
    3.-imprimir orden de reparacion
    4.-salir
    Opcion a elegir: """
    return input(menu)
def menu_general():
    while True:
        try:
            opcion = int(menu())
            if opcion == 4:
                print("Saliendo del programa")
                break
            elif opcion == 1:
                registrar_vehiculo()
                input("vehiculo registrado con exito\nEnter para continuar")
            elif opcion == 2:
                listar_vehiculos()
                input("listado completo\nEnter para continuar")
            elif opcion == 3:
                imprimir_orden_reparacion()
                input("Archivo txt generado. presione Enter para continuar")
            else:
                print("INGRESE NUEVAMENTE NO ES VALIDO ")
        except ValueError:
            print("Error, ingrese un valor numerico")
        except Exception as e:
            print(f"Error inesperado: {e}")

menu_general()

