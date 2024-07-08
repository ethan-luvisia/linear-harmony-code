from manim import *
from manimusic import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
from manim_voiceover.services.gtts import GTTSService

class CircleScene(MovingCameraScene, VoiceoverScene):
    def construct(self):

        circle = Circle().set_color(LIGHT_BROWN).shift(UP * 0.3)
        ethanluvisia = Text("Ethan Luvisia", font_size=40).next_to(circle, DOWN * 1.3).set_color(LIGHT_BROWN)
        self.wait(0.6) 
        self.play(Create(circle), self.camera.frame.animate.scale(0.5), run_time=1.2)
        self.wait(1)
        self.play(Write(ethanluvisia))
        self.wait(10)
        self.play(FadeOut(circle))
        self.wait(0.8)
        

        