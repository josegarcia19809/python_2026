import pandas as pd

reservaciones = pd.read_csv("data/reservaciones.csv")


print(reservaciones.groupby("nombre_cliente").size().reset_index(name="visitas")
      .sort_values("visitas", ascending=False))