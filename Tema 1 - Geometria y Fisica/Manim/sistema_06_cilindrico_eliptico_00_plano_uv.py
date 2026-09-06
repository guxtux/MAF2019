from manim import *
import numpy as np


class CoordenadasElipticas(Scene):

    def construct(self):

        # Change background and set axes/graphs to contrasting colors
        self.camera.background_color = WHITE
        
        # ============================================================
        # PARÁMETROS DEL SISTEMA
        # ============================================================

        a = 1.5

        # Escala visual
        escala = 1.45

        # Valores de u para las elipses
        valores_u = [0.75, 1.0, 1.5, 2.0]

        # Valores de v para las hipérbolas
        valores_v = [
            np.pi / 6,
            np.pi / 4,
            np.pi / 3,
            2 * np.pi / 3,
            3 * np.pi / 4,
            5 * np.pi / 6
        ]

        # ============================================================
        # TÍTULO
        # ============================================================

        titulo = MathTex(
            r"\text{Sistema de coordenadas elíptico}",
            font_size=34,
            color=BLACK
        )
        titulo.to_edge(UL)

        self.play(Write(titulo))

        # ============================================================
        # EJES CARTESIANOS
        # ============================================================

        eje_x = Arrow(
            LEFT * 6,
            RIGHT * 6,
            buff=0,
            stroke_width=2,
            color=BLACK
        )

        eje_y = Arrow(
            DOWN * 3.8,
            UP * 3.8,
            buff=0,
            stroke_width=2,
            color=BLACK
        )

        etiqueta_x = MathTex("x", font_size=28, color=BLACK)
        etiqueta_y = MathTex("y", font_size=28, color=BLACK)

        etiqueta_x.next_to(eje_x.get_end(), RIGHT, buff=0.1)
        etiqueta_y.next_to(eje_y.get_end(), UP, buff=0.1)

        self.play(
            Create(eje_x),
            Create(eje_y),
            Write(etiqueta_x),
            Write(etiqueta_y)
        )

        # ============================================================
        # FOCOS
        # ============================================================

        foco_izq = Dot(
            point=LEFT * a * escala,
            radius=0.055,
            color=BLACK
        )

        foco_der = Dot(
            point=RIGHT * a * escala,
            radius=0.055,
            color=BLACK
        )

        etiqueta_foco_izq = MathTex("(-a,0)", font_size=22, color=BLACK)
        etiqueta_foco_der = MathTex("(a,0)", font_size=22, color=BLACK)

        etiqueta_foco_izq.next_to(
            foco_izq,
            DOWN,
            buff=0.12
        )

        etiqueta_foco_der.next_to(
            foco_der,
            DOWN,
            buff=0.12
        )

        self.play(
            FadeIn(foco_izq),
            FadeIn(foco_der),
            Write(etiqueta_foco_izq),
            Write(etiqueta_foco_der)
        )

        # ============================================================
        # FAMILIA u = CONSTANTE
        #
        # x = a cosh(u) cos(v)
        # y = a sinh(u) sin(v)
        #
        # Son ELIPSES
        # ============================================================

        elipses = VGroup()

        for u in valores_u:

            def elipse_func(t, u=u):
                x = a * np.cosh(u) * np.cos(t)
                y = a * np.sinh(u) * np.sin(t)

                return np.array([
                    escala * x,
                    escala * y,
                    0
                ])

            elipse = ParametricFunction(
                elipse_func,
                t_range=[0, TAU],
                stroke_width=2,
                color=BLACK
            )

            elipses.add(elipse)

        self.play(
            LaggedStart(
                *[Create(e) for e in elipses],
                lag_ratio=0.25
            ),
            run_time=3
        )

        # ============================================================
        # ETIQUETAS DE LAS ELIPSES
        # ============================================================

        etiquetas_u = VGroup()

        for u in valores_u:

            x = 0
            y = escala * a * np.sinh(u)

            etiqueta = MathTex(
                rf"u={u:g}",
                font_size=22,
                color=BLACK
            )

            etiqueta.move_to(
                np.array([0, y, 0])
            )

            etiquetas_u.add(etiqueta)

        self.play(
            LaggedStart(
                *[Write(e) for e in etiquetas_u],
                lag_ratio=0.2
            )
        )

        # ============================================================
        # FAMILIA v = CONSTANTE
        #
        # x = a cosh(u) cos(v)
        # y = a sinh(u) sin(v)
        #
        # Son HIPÉRBOLAS
        # ============================================================

        hiperbolas = VGroup()

        # Extensión del parámetro u
        u_max = 2.6

        for v in valores_v:

            def hiperbola_func(t, v=v):
                x = a * np.cosh(t) * np.cos(v)
                y = a * np.sinh(t) * np.sin(v)

                return np.array([
                    escala * x,
                    escala * y,
                    0
                ])

            hiperbola = ParametricFunction(
                hiperbola_func,
                t_range=[-u_max, u_max],
                stroke_width=1.8,
                color=BLACK
            )

            hiperbolas.add(hiperbola)

        self.play(
            LaggedStart(
                *[Create(h) for h in hiperbolas],
                lag_ratio=0.15
            ),
            run_time=4
        )

        # ============================================================
        # HIPÉRBOLAS SOBRE LOS EJES
        #
        # v = 0, pi/2, pi, 3pi/2
        # ============================================================

        valores_ejes = [
            0,
            np.pi / 2,
            np.pi,
            3 * np.pi / 2
        ]

        hiperbolas_ejes = VGroup()

        for v in valores_ejes:

            def hiperbola_eje(t, v=v):
                x = a * np.cosh(t) * np.cos(v)
                y = a * np.sinh(t) * np.sin(v)

                return np.array([
                    escala * x,
                    escala * y,
                    0
                ])

            curva = ParametricFunction(
                hiperbola_eje,
                t_range=[-u_max, u_max],
                stroke_width=2.0,
                color=BLACK
            )

            hiperbolas_ejes.add(curva)

        self.play(
            Create(hiperbolas_ejes),
            run_time=2
        )

        # ============================================================
        # ETIQUETAS PARA v
        # ============================================================

        etiquetas_v = VGroup()

        posiciones_v = [
            (np.pi / 6,  RIGHT * 4.5 + UP * 2.2),
            (np.pi / 4,  RIGHT * 4.0 + UP * 1.2),
            (np.pi / 3,  RIGHT * 3.0 + UP * 0.35),
            (2*np.pi/3, LEFT * 3.0 + UP * 0.35),
            (3*np.pi/4, LEFT * 4.0 + UP * 1.2),
            (5*np.pi/6, LEFT * 4.5 + UP * 2.2)
        ]

        for v, posicion in posiciones_v:

            etiqueta = MathTex(
                rf"v={self.frac_pi(v)}",
                font_size=21,
                color=BLACK
            )

            etiqueta.move_to(posicion)

            etiquetas_v.add(etiqueta)

        self.play(
            LaggedStart(
                *[Write(e) for e in etiquetas_v],
                lag_ratio=0.15
            )
        )

        # ============================================================
        # ETIQUETAS ESPECIALES
        # ============================================================

        v0 = MathTex("v=0", font_size=21, color=BLACK)
        v0.move_to(RIGHT * 5.0 + DOWN * 0.35)

        vpi = MathTex("v=\\pi", font_size=21, color=BLACK)
        vpi.move_to(LEFT * 5.0 + DOWN * 0.35)

        vpi2 = MathTex("v=\\frac{\\pi}{2}", font_size=21, color=BLACK)
        vpi2.move_to(UP * 3.45 + RIGHT * 0.45)

        v3pi2 = MathTex(
            "v=\\frac{3\\pi}{2}",
            font_size=21, color=BLACK
        )
        v3pi2.move_to(DOWN * 3.25 + RIGHT * 0.45)

        self.play(
            Write(v0),
            Write(vpi),
            Write(vpi2),
            Write(v3pi2)
        )

        # ============================================================
        # MOSTRAR LAS ECUACIONES
        # ============================================================

        ecuaciones = VGroup(
            MathTex(
                r"x=a\cosh u\cos v",
                font_size=25,
                color=BLACK
            ),
            MathTex(
                r"y=a\sinh u\sin v",
                font_size=25,
                color=BLACK
            )
        )

        ecuaciones.arrange(DOWN, buff=0.12)
        ecuaciones.to_corner(UL)
        ecuaciones.shift(DOWN * 0.45)

        fondo_ec = BackgroundRectangle(
            ecuaciones,
            fill_opacity=0.85,
            buff=0.12,
            color=WHITE
        )

        self.play(
            FadeIn(fondo_ec),
            Write(ecuaciones)
        )

        # ============================================================
        # PAUSA FINAL
        # ============================================================

        self.wait(3)

    # ================================================================
    # FUNCIÓN AUXILIAR PARA ESCRIBIR FRACCIONES DE PI
    # ================================================================

    def frac_pi(self, valor):

        valores = {
            np.pi / 6: r"\frac{\pi}{6}",
            np.pi / 4: r"\frac{\pi}{4}",
            np.pi / 3: r"\frac{\pi}{3}",
            2 * np.pi / 3: r"\frac{2\pi}{3}",
            3 * np.pi / 4: r"\frac{3\pi}{4}",
            5 * np.pi / 6: r"\frac{5\pi}{6}"
        }

        return valores.get(valor, str(valor))