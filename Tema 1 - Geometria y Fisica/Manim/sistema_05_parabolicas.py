from manim import *
import numpy as np


class Parabolicas(ThreeDScene):
    def construct(self):

        ###########################################################
        # Cámara
        ###########################################################

        self.set_camera_orientation(
            phi=68*DEGREES,
            theta=-45*DEGREES,
            zoom=0.55
        )

        ###########################################################
        # Ejes
        ###########################################################

        axes = ThreeDAxes(
            x_range=[-5,5,1],
            y_range=[-5,5,1],
            z_range=[-5,5,1],
            x_length=8,
            y_length=8,
            z_length=8
        )

        labels = axes.get_axis_labels(
            Tex("x"),
            Tex("y"),
            Tex("z")
        )

        self.add(axes,labels)

        ###########################################################
        # Parámetros
        ###########################################################

        phi_min = 0
        phi_max = TAU

        rmax = 3.2

        ###########################################################
        # Familia u = constante
        ###########################################################

        u_values = [0.8, 2.3]

        superficies_u = VGroup()

        for u0 in u_values:

            superficie = Surface(

                lambda v,phi: np.array([
                    u0*v*np.cos(phi),
                    u0*v*np.sin(phi),
                    0.5*(u0**2-v**2)
                ]),

                u_range=[0.05, rmax],
                v_range=[phi_min, phi_max],

                resolution=(36, 60),
                checkerboard_colors=[BLUE_D, BLUE_E],
                fill_opacity=0.45,
                stroke_width=0.5,
                stroke_color=BLUE
            )

            superficies_u.add(superficie)

        ###########################################################
        # Familia v = constante
        ###########################################################

        v_values = [0.8, 2.3]

        superficies_v = VGroup()

        for v0 in v_values:

            superficie = Surface(

                lambda u,phi: np.array([
                    u*v0*np.cos(phi),
                    u*v0*np.sin(phi),
                    0.5*(u**2 - v0**2)

                ]),

                u_range=[0.05,rmax],
                v_range=[phi_min,phi_max],

                resolution=(36, 60),
                checkerboard_colors=[RED_D, RED_E],
                fill_opacity=0.45,
                stroke_width=0.5,
                stroke_color=RED
            )

            superficies_v.add(superficie)

        ###########################################################
        # Plano φ = constante
        ###########################################################

        phi0 = 40*DEGREES

        plano_phi = Surface(

            lambda u,v: np.array([

                u*v*np.cos(phi0),
                u*v*np.sin(phi0),
                0.5*(u**2 - v**2)
            ]),

            u_range=[0,rmax],
            v_range=[0,rmax],

            resolution=(40, 40),
            checkerboard_colors=[GREEN_D, GREEN_E],
            fill_opacity=0.55,
            stroke_color=GREEN,
            stroke_width=0.5
        )

        ###########################################################
        # Animación
        ###########################################################

        self.play(Create(superficies_u),run_time=3)
        self.play(Create(superficies_v),run_time=3)
        self.play(FadeIn(plano_phi),run_time=2)
        self.begin_ambient_camera_rotation(rate=0.18)
        self.wait(10)
        self.stop_ambient_camera_rotation()
        self.wait()