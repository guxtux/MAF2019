from manim import *

class PlanosConstantes3D(ThreeDScene):
    def construct(self):
        # Configuración inicial de la cámara
        self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES, zoom=0.8)

        # Sistema de coordenadas 3D
        axes = ThreeDAxes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            z_range=[0, 5, 1],
            x_length=5,
            y_length=5,
            z_length=5,
        ).move_to(ORIGIN)

        # Etiquetas de ejes
        labels = axes.get_axis_labels(
            Tex("$x$"), Tex("$y$"), Tex("$z$")
        )

        # encabezado_01 = Tex(r'Con $(x_{0}=\text{cte}, y, z)$', font_size=20).to_edge(UP).scale(2)
        # encabezado_02 = Tex(r'Con $(x, y_{0}=\text{cte}, z)$', font_size=20).to_edge(UP).scale(2)
        # encabezado_03 = Tex(r'Con $(x, y, z_{0}=\text{cte})$', font_size=20).to_edge(UP).scale(2)
        encabezado_04 = Tex('Intesección de los tres planos', font_size=20).to_edge(UP).scale(2)

        self.add_fixed_in_frame_mobjects(encabezado_04)
        self.play(Create(axes), Write(labels))
        self.wait()

        # Planos: x = 3, y = 2, z = 4
        plano_x = Surface(
            lambda u, v: axes.c2p(3, u, v),
            u_range=[0, 5],
            v_range=[0, 5],
            fill_opacity=0.6,
            checkerboard_colors=[BLUE, BLUE],
        )

        plano_y = Surface(
            lambda u, v: axes.c2p(u, 2, v),
            u_range=[0, 5],
            v_range=[0, 5],
            fill_opacity=0.6,
            checkerboard_colors=[GREEN, GREEN],
        )

        plano_z = Surface(
            lambda u, v: axes.c2p(u, v, 4),
            u_range=[0, 5],
            v_range=[0, 5],
            fill_opacity=0.6,
            checkerboard_colors=[RED, RED],
        )

        # Mostrar planos uno por uno
        self.play(FadeIn(plano_x))
        self.wait(2)

        self.play(FadeIn(plano_y))
        self.wait(2)
        
        self.play(FadeIn(plano_z))
        self.wait(2)

        # Punto de intersección (3, 2, 4)
        punto = Dot3D(point=axes.c2p(3, 2, 4), color=YELLOW, radius=0.1)
        # label_punto = MathTex("(3, 2, 4)").next_to(punto, UP).scale(0.7)

        self.play(FadeIn(punto))
        self.wait(2)
