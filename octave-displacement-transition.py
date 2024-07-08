from manim import *
from manimusic import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
from manim_voiceover.services.gtts import GTTSService

class Scene1(MovingCameraScene, VoiceoverScene):
    def construct(self):

        octave = Text("Octave", font_size=72).move_to(UP)
        displacement = Text("Displacement", font_size=72).move_to(DOWN)
        non_chord = Text("Non-Chord", font_size=72).move_to(UP)
        tones = Text("Tones", font_size=72).move_to(DOWN)
        self.wait(0.6)
        self.play(Write(octave), Write(displacement))
        self.wait(1)
        self.play(FadeOut(octave), FadeOut(displacement))
        self.wait(0.8)

        