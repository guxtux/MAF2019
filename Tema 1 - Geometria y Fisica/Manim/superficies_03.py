from manim import *

class Cilindricas(ThreeDScene):
    def construct(self):
        # Escena 3D
        self.set_camera_orientation(phi=70*DEGREES, theta=30*DEGREES)

        # Ejes 3D
        axes = ThreeDAxes(
            x_range=[-3,3,1],
            y_range=[-3,3,1],
            z_range=[-3,3,1],
        )

         # Etiquetas de ejes
        labels = axes.get_axis_labels(
            Tex("$x$"), Tex("$y$"), Tex("$z$")
        )

        # Parámetros de las superficies
        r0 = 2         # radio de la esfera
        theta0 = PI/6  # ángulo polar (cono)
        
        # Superficie 1: Circunferencias r = r0
        # --- 1) Circunferencia en el plano xy (rho constante)
        circ = Circle(
            radius=2,
            color=YELLOW,
            fill_opacity=0.3
            # checkerboard_colors=[TEAL_E, TEAL_E]
                    ).move_to(ORIGIN)
        
        # --- 2) Cilindro (rho constante extendido en z)
        cilindro = Cylinder(
            radius=2,
            height=3.5,
            direction=OUT,
            color=TEAL_E,
            fill_opacity=0.4
        )

        # --- 3) Plano meridiano (phi constante)
        phi_plane = Surface(
            lambda u, v: [u, u*0, v],
            u_range=[-3, 3],
            v_range=[-2, 2],
            checkerboard_colors=[MAROON_C, MAROON_E],
            fill_opacity=0.5
        )

        # Rotamos alrededor del eje z para que esté en phi=phi0
        phi0 = 45 * DEGREES
        phi_plane.rotate(phi0, axis=OUT)  # OUT es el eje z en Manim

        # --- 4) Plano horizontal (z constante)
        z_plane = Surface(
            lambda u, v: [u, v, 1],
            u_range=[-3, 3],
            v_range=[-3, 3],
            checkerboard_colors=[YELLOW_B, YELLOW_C],
            fill_opacity=0.5
        )

        encabezado_01=Tex(r'Con $(r_{0}=\text{cte}, \phi, z)$', font_size=20).scale(2)
        encabezado_02 = Tex(r'Con $(r, \phi_{0}=\text{cte}, z)$', font_size=20).scale(2)
        encabezado_03 = Tex(r'Con $(r, \phi, z_{0}=\text{cte})$', font_size=20).scale(2)
        encabezado_04 = Tex(r'Las tres superficies constantes', font_size=20).scale(2)

        self.add_fixed_in_frame_mobjects(encabezado_04) #<----- Add this
        encabezado_04.to_corner(UL)

        self.play(Create(axes), Write(labels))
        self.wait()
        
        # self.play(FadeIn(circ))
        # self.wait(2)
        self.play(FadeIn(cilindro))
        self.wait(2)
        self.play(FadeIn(phi_plane))
        self.wait(2)
        self.play(FadeIn(z_plane))
        self.wait(2)