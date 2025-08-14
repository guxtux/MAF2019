from manim import *
import numpy as np

class ParabolicCylinder(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        axes = ThreeDAxes()
        self.add(axes)

        def parametric_surface_function(u, v):
            return np.array([u, v, u**2])

        # def parametric_surface_function_2(u, v):
        #     return np.array([u, v, -u**2])

        cylinder_surface = Surface(
            parametric_surface_function,
            resolution=(20, 20),
            u_range=[-2, 2],
            v_range=[-2, 2]
        )

        # cylinder_surface_2 = Surface(
        #     parametric_surface_function_2,
        #     resolution=(20, 20),
        #     u_range=[-2, 2],
        #     v_range=[-2, 2]
        # )


        cylinder_surface.set_fill(BLUE, opacity=0.5)
        #cylinder_surface_2.set_fill(PURE_RED, opacity=0.5)

        self.play(Create(cylinder_surface))
        self.wait(2)
        self.play(Rotate(cylinder_surface, angle=PI/2, axis=RIGHT))
        # self.play(Rotate(cylinder_surface_2, angle=PI/2, axis=RIGHT)) # Example animation
        self.wait(2)