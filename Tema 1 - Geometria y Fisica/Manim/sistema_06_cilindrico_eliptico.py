from manim import *
import numpy as np


class CilindricasElipticas(ThreeDScene):

    def construct(self):

        ############################################################
        # Cámara
        ############################################################

        self.set_camera_orientation(
            phi=68 * DEGREES,
            theta=-45 * DEGREES,
            zoom=0.55
        )

        ############################################################
        # Ejes
        ############################################################

        axes = ThreeDAxes(
            x_range=[-4,4,1],
            y_range=[-4,4,1],
            z_range=[-3,3,1],
            x_length=8,
            y_length=8,
            z_length=6
        )

        labels = axes.get_axis_labels(
            Tex("x"),
            Tex("y"),
            Tex("z")
        )

        self.add(axes, labels)

        ############################################################
        # Parámetros
        ############################################################

        zmin = -2.5
        zmax = 2.5

        ############################################################
        # Superficies u = constante
        # (Cilindros elípticos)
        ############################################################

        u_values = [0.35, 1.25]

        cilindros_elipticos = VGroup()

        for u0 in u_values:

            superficie = Surface(

                lambda v, z: np.array([

                    np.cosh(u0) * np.cos(v),
                    np.sinh(u0) * np.sin(v),
                    z
                ]),

                u_range=[0, TAU],
                v_range=[zmin, zmax],
                resolution=(48, 18),
                checkerboard_colors=[ BLUE_D, BLUE_E ],

                fill_opacity=0.35,
                stroke_color=BLUE,
                stroke_width=0.5

            )

            cilindros_elipticos.add(superficie)

        ############################################################
        # Superficies v = constante
        # (Cilindros hiperbólicos)
        ############################################################

        v_values = [
            25*DEGREES,
            55*DEGREES,
            125*DEGREES,
            155*DEGREES
        ]

        umax = 1.45

        cilindros_hiperbolicos = VGroup()

        for v0 in v_values:

            superficie = Surface(

                lambda u, z: np.array([

                    np.cosh(u) * np.cos(v0),
                    np.sinh(u) * np.sin(v0),
                    z

                ]),

                u_range=[0, umax],
                v_range=[zmin, zmax],

                resolution=(30, 18),

                checkerboard_colors=[ RED_D, RED_E ],

                fill_opacity=0.35,
                stroke_color=RED,
                stroke_width=0.5

            )

            cilindros_hiperbolicos.add(superficie)

        ############################################################
        # Plano z = constante
        ############################################################

        z0 = 0.8

        plano = Surface(

            lambda u, v: np.array([

                np.cosh(u) * np.cos(v),
                np.sinh(u) * np.sin(v),
                z0

            ]),

            u_range=[0, umax],
            v_range=[0, TAU],

            resolution=(30, 60),

            checkerboard_colors=[ GREEN_D, GREEN_E ],

            fill_opacity=0.55,
            stroke_color=GREEN,
            stroke_width=0.4

        )

        ############################################################
        # Animación
        ############################################################

        self.play(
            LaggedStart(
                *[Create(s) for s in cilindros_elipticos],
                lag_ratio=0.15
            ),
            run_time=3
        )

        self.play(
            LaggedStart(
                *[Create(s) for s in cilindros_hiperbolicos],
                lag_ratio=0.15
            ),
            run_time=3
        )

        self.play(
            FadeIn(plano),
            run_time=2
        )

        ############################################################

        self.begin_ambient_camera_rotation(rate=0.18)
        self.wait(10)
        self.stop_ambient_camera_rotation()
        self.wait()