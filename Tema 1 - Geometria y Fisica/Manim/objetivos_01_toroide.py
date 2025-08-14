from manim import *
#Manim Example | Creating Torus

class Toroide(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
                          x_range=[-6, 6, 1],
                          y_range=[-6, 6, 1],
                          z_range=[-3, 3, 1],
                          # x_min=-6,
                          # x_max=6,
                          # y_min=-6,
                          # y_max=6,
                          # z_min=-3,
                          # z_max=3,
                          axis_config={
                              "stroke_color": WHITE,
                              "stroke_width": 4,
                              "include_tip": True,
                              "include_ticks": True,
                              "tick_size": 0.1
                          },
                          x_axis_config={
                              "stroke_color": WHITE,
                              "stroke_width": 4,
                              "include_tip": True,
                              "include_ticks": True,
                              "tick_size": 0.1
                          },
                          y_axis_config={
                              "stroke_color": WHITE,
                              "stroke_width": 4,
                              "include_tip": True,
                              "include_ticks": True,
                              "tick_size": 0.1
                          },
                          z_axis_config={
                              "stroke_color": WHITE,
                              "stroke_width": 4,
                              "include_tip": True,
                              "include_ticks": True,
                              "tick_size": 0.1
                          })
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)
        self.add(axes)

        torus = Torus(major_radius=2, minor_radius=0.55, checkerboard_colors=[RED_D, RED_E]
            #,  color=BLUE, resolution=(201,201),fill_opacity=0.8, gloss=0.3, shadow=0.4
            )
        self.play(Create(torus), run_time=3)

        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(7)
        self.stop_ambient_camera_rotation()

        self.wait()