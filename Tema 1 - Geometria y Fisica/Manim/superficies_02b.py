from manim import *

class SistemaEsferico(ThreeDScene):
    def construct(self):
        # Ejes 3D
        axes = ThreeDAxes(
            x_range=[-3,3,1],
            y_range=[-3,3,1],
            z_range=[-3,3,1],
        )

        # Parámetros de superficies
        r0 = 2         # radio de la esfera
        theta0 = PI/6  # ángulo polar (cono)
        phi0 = PI/4    # ángulo azimutal (plano)

        # --- Superficie 1: Esfera r = r0 ---
        esfera = Surface(
            lambda u, v: np.array([
                r0 * np.sin(u) * np.cos(v),
                r0 * np.sin(u) * np.sin(v),
                r0 * np.cos(u)
            ]),
            u_range=[0, PI],
            v_range=[0, 2*PI],
            resolution=(30, 30),
            fill_opacity=0.4,
            checkerboard_colors=[BLUE, BLUE]
        )

        # --- Superficie 2: Cono θ = θ0 ---
        cono = Surface(
            lambda u, v: np.array([
                u * np.sin(theta0) * np.cos(v),
                u * np.sin(theta0) * np.sin(v),
                u * np.cos(theta0)
            ]),
            u_range=[0, 3],
            v_range=[0, 2*PI],
            resolution=(30, 30),
            fill_opacity=0.4,
            checkerboard_colors=[GREEN, GREEN]
        )

        # --- Superficie 3: Plano φ = φ0 ---
        plano = Surface(
            lambda u, v: np.array([
                u * np.cos(phi0),
                u * np.sin(phi0),
                v
            ]),
            u_range=[-3,3],
            v_range=[-3,3],
            resolution=(2, 30),
            fill_opacity=0.4,
            checkerboard_colors=[RED, RED]
        )

        # Configuración de cámara
        self.set_camera_orientation(phi=70*DEGREES, theta=30*DEGREES)

        # --- Animación paso a paso ---
        self.play(Create(axes))               # 1. Aparecen los ejes
        self.wait(1)

        self.play(FadeIn(esfera))             # 2. Esfera
        self.wait(1)

        self.play(FadeIn(cono))               # 3. Cono
        self.wait(1)

        self.play(FadeIn(plano))              # 4. Plano meridiano
        self.wait(2)

        # Rotación final para visualizar todo el sistema
        self.begin_3dillusion_camera_rotation(rate=0.2)
        self.wait(6)
        self.stop_3dillusion_camera_rotation()
