import pandas as pd

df_reservaciones = pd.read_csv("data/reservaciones.csv")
df_resenias = pd.read_csv("data/resenas.csv")

# Convertir fechas y horas (importante para cálculos)
# df_reservaciones["hora_inicio"] = pd.to_datetime(
#     df_reservaciones["hora_inicio"], format="%H:%M"
# )
#
# df_reservaciones["hora_fin"] = pd.to_datetime(
#     df_reservaciones["hora_fin"], format="%H:%M"
# )

df_reservaciones["inicio"] = pd.to_datetime(
    df_reservaciones["fecha"].astype(str) + " " + df_reservaciones["hora_inicio"]
)

df_reservaciones["fin"] = pd.to_datetime(
    df_reservaciones["fecha"].astype(str) + " " + df_reservaciones["hora_fin"]
)
df_reservaciones["fecha"] = pd.to_datetime(df_reservaciones["fecha"])

print(df_reservaciones.head())


def menu():
    print("\n📊 MENÚ DE REPORTES")
    print("1. 🔥 Horas con más reservaciones")
    print("2. 📅 Reservaciones por día")
    print("3. ❌ Total por estado")
    print("4. 👥 Clientes con más reservaciones")
    print("5. 🪑 Mesas más utilizadas")
    print("6. ⏱️ Tiempo promedio de estancia")
    print("7. 👨‍👩‍👧 Promedio de personas por reservación")
    print("8. 📊 Reservaciones por número de personas")
    print("9. 🚫 Cantidad de no-shows")
    print("10. 📈 Reservaciones por día y estado")
    print("11. 👥 Promedio de calificación")
    print("0. Salir")


def ejecutar_opcion(opcion):
    if opcion == "1":
        print("\n🔥 Horas pico")
        print(df_reservaciones.groupby("hora_inicio").size().sort_values(ascending=False))

    elif opcion == "2":
        print("\n📅 Reservaciones por día")
        print(df_reservaciones.groupby("fecha").size())

    elif opcion == "3":
        print("\n❌ Total por estado (confirmadas, canceladas, no_show)")
        print(df_reservaciones.groupby("estado").size())

    elif opcion == "4":
        print("\n👥 Clientes frecuentes")
        print(df_reservaciones.groupby("nombre_cliente").size().sort_values(
            ascending=False))

    elif opcion == "5":
        print("\n🪑 Mesas más utilizadas")
        print(df_reservaciones.groupby("numero_mesa").size().sort_values(ascending=False))

    elif opcion == "6":
        # print("\n⏱️ Tiempo promedio de estancia (minutos)")
        # promedio = (df_reservaciones["hora_fin"] - df_reservaciones["hora_inicio"]).mean()
        # print(promedio.total_seconds() / 60)
        print("\n⏱️ Tiempo promedio de estancia (minutos)")
        promedio = (df_reservaciones["fin"] - df_reservaciones["inicio"]).mean()
        print(promedio.total_seconds() / 60)

    elif opcion == "7":
        print("\n👨‍👩‍👧 Promedio de personas")
        print(df_reservaciones["numero_personas"].mean())

    elif opcion == "8":
        print("\n📊 Reservaciones por número de personas")
        print(df_reservaciones.groupby("numero_personas").size())

    elif opcion == "9":
        print("\n🚫 No-shows")
        print(df_reservaciones[df_reservaciones["estado"] == "no_show"].shape[0])

    elif opcion == "10":
        print("\n📈 Reservaciones por día y estado")
        print(df_reservaciones.groupby(["fecha", "estado"]).size())

    elif opcion == "11":
        print("\n👥 Promedio de calificación")
        print(df_resenias["calificacion"].mean())

    elif opcion == "0":
        print("👋 Saliendo...")
        return False

    else:
        print("❌ Opción inválida")

    return True


# Bucle principal
continuar = True
while continuar:
    menu()
    opcion = input("Selecciona una opción: ")
    continuar = ejecutar_opcion(opcion)
