import sqlite3


def conectar():
    return sqlite3.connect("data/restaurante.db")


def mostrar_menu():
    print("\n📊 MENÚ DE REPORTES")
    print("1. 🔥 Horas pico")
    print("2. 📅 Reservaciones por día")
    print("3. ❌ Total por estado")
    print("4. 👥 Clientes con más reservaciones")
    print("5. 🪑 Mesas más utilizadas")
    print("6. ⏱️ Tiempo promedio de estancia")
    print("7. 👨‍👩‍👧 Promedio de personas")
    print("8. 📊 Reservaciones por número de personas")
    print("9. 🚫 No-shows")
    print("10. 📈 Reservaciones por día y estado")
    print("11. ⭐ Promedio de calificación")
    print("0. Salir")

def imprimir_resultados(resultados):
    if not resultados:
        print("Sin resultados")
    else:
        for fila in resultados:
            print(" | ".join(str(x) for x in fila))

def ejecutar_consulta(sql):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(sql)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados


# def imprimir_resultados(resultados):
#     for fila in resultados:
#         print(fila)


def ejecutar_opcion(opcion):
    if opcion == "1":
        print("\n🔥 Horas pico")
        sql = """
              SELECT hora_inicio, COUNT(*)
              FROM reservaciones
              GROUP BY hora_inicio
              ORDER BY COUNT(*) DESC; \
              """

    elif opcion == "2":
        print("\n📅 Reservaciones por día")
        sql = """
              SELECT fecha, COUNT(*)
              FROM reservaciones
              GROUP BY fecha
              ORDER BY fecha; \
              """

    elif opcion == "3":
        print("\n❌ Total por estado")
        sql = """
              SELECT estado, COUNT(*)
              FROM reservaciones
              GROUP BY estado; \
              """

    elif opcion == "4":
        print("\n👥 Clientes con más reservaciones")
        sql = """
              SELECT c.nombre, COUNT(*)
              FROM reservaciones r
                       JOIN clientes c ON r.cliente_id = c.id
              GROUP BY c.nombre
              ORDER BY COUNT(*) DESC; \
              """

    elif opcion == "5":
        print("\n🪑 Mesas más utilizadas")
        sql = """
              SELECT m.numero_mesa, COUNT(*)
              FROM reservaciones r
                       JOIN mesas m ON r.mesa_id = m.id
              GROUP BY m.numero_mesa
              ORDER BY COUNT(*) DESC; \
              """

    elif opcion == "6":
        print("\n⏱️ Tiempo promedio de estancia (minutos)")
        sql = """
              SELECT AVG((strftime('%s', hora_fin) - strftime('%s', hora_inicio)) / 60.0)
              FROM reservaciones; \
              """

    elif opcion == "7":
        print("\n👨‍👩‍👧 Promedio de personas")
        sql = """
              SELECT AVG(numero_personas)
              FROM reservaciones; \
              """

    elif opcion == "8":
        print("\n📊 Reservaciones por número de personas")
        sql = """
              SELECT numero_personas, COUNT(*)
              FROM reservaciones
              GROUP BY numero_personas
              ORDER BY numero_personas; \
              """

    elif opcion == "9":
        print("\n🚫 No-shows")
        sql = """
              SELECT COUNT(*)
              FROM reservaciones
              WHERE estado = 'no_show'; \
              """

    elif opcion == "10":
        print("\n📈 Reservaciones por día y estado")
        sql = """
              SELECT fecha, estado, COUNT(*)
              FROM reservaciones
              GROUP BY fecha, estado
              ORDER BY fecha; \
              """

    elif opcion == "11":
        print("\n⭐ Promedio de calificación")
        sql = """
              SELECT AVG(calificacion)
              FROM resenas; \
              """

    elif opcion == "0":
        print("👋 Saliendo...")
        return False

    else:
        print("❌ Opción inválida")
        return True

    resultados = ejecutar_consulta(sql)
    imprimir_resultados(resultados)

    return True


# 🔁 Loop principal
def main():
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        continuar = ejecutar_opcion(opcion)


# Ejecutar programa
main()
