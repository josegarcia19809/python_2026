from graphics import *


class AnimacionTrenes:

    def __init__(self, ventana, longitud_tren):

        # 🎨 Colores de los trenes
        self.colores = [
            color_rgb(233, 33, 40),
            color_rgb(78, 151, 210),
            color_rgb(251, 170, 26),
            color_rgb(11, 132, 54)
        ]

        self.longitud_tren = longitud_tren

        # 🛤️ Creamos las vías del tren
        via0 = Line(Point(10, 330), Point(790, 330))
        via1 = Line(Point(10, 470), Point(790, 470))
        via2 = Line(Point(330, 10), Point(330, 790))
        via3 = Line(Point(470, 10), Point(470, 790))

        # 🎨 Dibujamos las vías
        self.dibujar_via(ventana, via0)
        self.dibujar_via(ventana, via1)
        self.dibujar_via(ventana, via2)
        self.dibujar_via(ventana, via3)

        # 🚂 Creamos los trenes
        self.tren0 = Line(
            Point(10, 330),
            Point(10 - longitud_tren, 330)
        )

        self.tren1 = Line(
            Point(470, 10),
            Point(470, 10 - longitud_tren)
        )

        self.tren2 = Line(
            Point(790, 470),
            Point(790 + longitud_tren, 470)
        )

        self.tren3 = Line(
            Point(330, 790),
            Point(330, 790 + longitud_tren)
        )

        # 🎨 Dibujamos los trenes
        self.dibujar_tren(
            ventana,
            self.tren0,
            self.colores[0]
        )

        self.dibujar_tren(
            ventana,
            self.tren1,
            self.colores[1]
        )

        self.dibujar_tren(
            ventana,
            self.tren2,
            self.colores[2]
        )

        self.dibujar_tren(
            ventana,
            self.tren3,
            self.colores[3]
        )

        # 🚦 Cuadros que representan intersecciones
        self.cajas = [

            Rectangle(
                Point(350, 350),
                Point(360, 360)
            ),

            Rectangle(
                Point(450, 350),
                Point(440, 360)
            ),

            Rectangle(
                Point(450, 450),
                Point(440, 440)
            ),

            Rectangle(
                Point(350, 450),
                Point(360, 440)
            )
        ]

        # 🎨 Dibujamos las intersecciones
        for caja in self.cajas:
            self.dibujar_cruce(ventana, caja)

    # 🔄 Actualiza posiciones de trenes e intersecciones
    def actualizar_trenes(self, trenes, intersecciones):

        # 🚂 Tren 0
        posicion_actual_x = (
                self.tren0.getP2().getX()
                - 10
                + self.longitud_tren
        )

        self.tren0.move(
            trenes[0].frente - posicion_actual_x,
            0
        )

        # 🚂 Tren 2
        posicion_actual_x = (
                790
                - self.tren2.getP2().getX()
                + self.longitud_tren
        )

        self.tren2.move(
            posicion_actual_x - trenes[2].frente,
            0
        )

        # 🚂 Tren 1
        posicion_actual_y = (
                self.tren1.getP2().getY()
                - 10
                + self.longitud_tren
        )

        self.tren1.move(
            0,
            trenes[1].frente - posicion_actual_y
        )

        # 🚂 Tren 3
        posicion_actual_y = (
                790
                - self.tren3.getP2().getY()
                + self.longitud_tren
        )

        self.tren3.move(
            0,
            posicion_actual_y - trenes[3].frente
        )

        # 🚦 Cambiar color de las intersecciones
        for i in range(4):

            # ⚪ Libre
            if intersecciones[i].bloqueado_por < 0:
                self.cajas[i].setFill(
                    color_rgb(185, 185, 185)
                )

            # 🎨 Ocupada por un tren
            else:
                self.cajas[i].setFill(
                    self.colores[
                        intersecciones[i].bloqueado_por
                    ]
                )

    # 🚦 Dibuja un cruce/intersección
    def dibujar_cruce(self, ventana, caja):
        caja.setFill(color_rgb(185, 185, 185))
        caja.draw(ventana)

    # 🛤️ Dibuja una vía
    def dibujar_via(self, ventana, linea):
        linea.setFill(color_rgb(185, 185, 185))
        linea.setWidth(4)
        linea.draw(ventana)

    # 🚂 Dibuja un tren
    def dibujar_tren(self, ventana, linea, color):
        linea.setFill(color)
        linea.setWidth(14)
        linea.draw(ventana)
