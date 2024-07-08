from manim import *
from manimusic import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
from manim_voiceover.services.gtts import GTTSService

class Scene1(MovingCameraScene, VoiceoverScene):
    CONFIG = {"include_sound": True}
    def construct(self):
        linear_harmony = Text("Linear Harmony", font_size=70).shift(UP * 1.2)
        definition = Text("Single lines of music", font_size=50).shift(DOWN * 1)
        definition2 = Text("creating harmonic structures", font_size=50).shift(DOWN * 1.8)

        self.play(Write(linear_harmony))
        self.add_sound("definition.wav")
        self.play(self.camera.frame.animate.scale(0.8))
        self.wait(2)
        self.play(Write(definition), run_time=1)
        self.play(Write(definition2), run_time=1)
        self.wait(5)
        self.play( *[FadeOut(mob)for mob in self.mobjects])