from manim import *
from manimusic import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
from manim_voiceover.services.gtts import GTTSService

class Scene1(MovingCameraScene, VoiceoverScene):
    def construct(self):

        lh = Text("Linear Harmony", font_size=72).move_to(UP)
        irm = Text("In Real Music", font_size=72).move_to(DOWN)
        non_chord = Text("Non-Chord", font_size=72).move_to(UP)
        tones = Text("Tones", font_size=72).move_to(DOWN)
        self.wait(0.6) 
        self.play(Write(lh), Write(irm), self.camera.frame.animate.scale(0.8), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(lh), FadeOut(irm)) 
        self.wait(0.8)
        

        