from manim import *
import numpy as np

class CilindricoParabolico(ThreeDScene):
    def construct(self):
        #config.frame_width =20
        # Ejes 3D
        
        ###############################################################
        # Cámara
        ###############################################################

        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-45 * DEGREES,
            zoom=0.9,
        )

        ###############################################################
        # Ejes
        ###############################################################

        axes = ThreeDAxes(
            x_range=[-6,6,1],
            y_range=[-6,6,1],
            z_range=[-4,4,1],

            x_length=10,
            y_length=10,
            z_length=8
        )

        labels = axes.get_axis_labels()

        self.play(Create(axes))
        self.play(Write(labels))

        ###############################################################
        # Parámetros
        ###############################################################

        zmin = -3
        zmax = 3

        vmax = 2.8
        umax = 2.8

        ###############################################################
        # Funciones paramétricas
        ###############################################################

        def surface_u(c):

            return Surface(

                lambda v,z : np.array([

                    0.5*(c**2-v**2),
                    c*v,
                    z

                ]),

                u_range=[-vmax,vmax],
                v_range=[zmin,zmax],

                resolution=(40,40),

                fill_opacity=0.35,

                checkerboard_colors=[
                    BLUE_D,
                    BLUE_E
                ],

                stroke_color=BLUE,
                stroke_width=1.2

            )


        def surface_v(c):

            return Surface(

                lambda u,z : np.array([

                    0.5*(u**2-c**2),
                    u*c,
                    z

                ]),

                u_range=[-umax,umax],
                v_range=[zmin,zmax],

                resolution=(40,40),

                fill_opacity=0.35,

                checkerboard_colors=[
                    GREEN_D,
                    GREEN_E
                ],

                stroke_color=GREEN,
                stroke_width=1.2

            )

        # --- 3) Plano horizontal (z constante)
        ###############################################################
        # Plano z = 3
        ###############################################################

        plane_z3 = Surface(

            lambda x, y: np.array([
                x,
                y,
                2.5
            ]),

            u_range=[-5, 5],
            v_range=[-5, 5],

            resolution=(20,20),

            fill_color=YELLOW,
            fill_opacity=0.25,

            checkerboard_colors=[
                YELLOW_D,
                YELLOW_E
            ],

            stroke_color=YELLOW,
            stroke_width=1.0,
        )



        ###############################################################
        # Superficies
        ###############################################################

        u1 = surface_u(1.2)
        u2 = surface_u(-1.2)
        

        v1 = surface_v(1.2)
        v2 = surface_v(-1.2)

        ###############################################################
        # Texto
        ###############################################################

        title = Text("Cilíndrico Parabólico", font_size=34).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)

        ###############################################################
        # Animación
        ###############################################################

        self.play(
            FadeIn(u1),
            FadeIn(u2),
            run_time=2
        )

        self.play(
            FadeIn(v1),
            FadeIn(v2),
            run_time=2
        )

        self.play(
            FadeIn(plane_z3),
            run_time=2
        )

        ###############################################################
        # Rotación automática
        ###############################################################

        self.begin_ambient_camera_rotation(rate=0.18)

        self.wait(10)

        self.stop_ambient_camera_rotation()

        self.wait() 
