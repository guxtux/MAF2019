from manim import *

class Esfericas(ThreeDScene):
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
        phi0 = PI/4    # ángulo azimutal (plano)

        # Superficie 1: Esfera r = r0
        esfera = Surface(
            lambda u, v: np.array([
                r0 * np.sin(u) * np.cos(v),
                r0 * np.sin(u) * np.sin(v),
                r0 * np.cos(u)
            ]),
            u_range=[0, PI],
            v_range=[0, 2*PI],
            resolution=(30, 30),
            fill_opacity=0.3,
            checkerboard_colors=[BLUE, BLUE]
        )

        # Superficie 2: Cono θ = θ0
        # Ecuación en cartesianas: z = r cosθ0,  ρ = r sinθ0
        cono = Surface(
            lambda u, v: np.array([
                u * np.sin(theta0) * np.cos(v),
                u * np.sin(theta0) * np.sin(v),
                u * np.cos(theta0)
            ]),
            u_range=[0, 3],       # radio hasta 3
            v_range=[0, 2*PI],    # gira alrededor de z
            resolution=(30, 30),
            fill_opacity=0.3,
            checkerboard_colors=[GREEN, GREEN]
        )

        # Superficie 3: Plano φ = φ0
        # En cartesianas: x = u cosφ0, y = u sinφ0
        plano = Surface(
            lambda u, v: np.array([
                u * np.cos(phi0),
                u * np.sin(phi0),
                v
            ]),
            u_range=[-3,3],
            v_range=[-3,3],
            resolution=(2, 30),
            fill_opacity=0.3,
            checkerboard_colors=[RED, RED]
        )

        encabezado_01=Tex(r'Con $(r_{0}=\text{cte}, \theta, \varphi)$', font_size=20).scale(2)
        encabezado_02 = Tex(r'Con $(r, \theta_{0}=\text{cte}, \varphi)$', font_size=20).scale(2)
        encabezado_03 = Tex(r'Con $(r, \theta, \varphi_{0}=\text{cte})$', font_size=20).scale(2)
        encabezado_04 = Tex(r'Las tres superficies constantes', font_size=20).scale(2)

        self.add_fixed_in_frame_mobjects(encabezado_04) #<----- Add this
        encabezado_04.to_corner(UL)
    
        self.play(Create(axes), Write(labels))
        self.wait()
        
        self.play(FadeIn(esfera))
        self.play(FadeIn(cono))
        self.play(FadeIn(plano))
        self.wait(3)