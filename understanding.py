from manim import *
from manimusic import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
from manim_voiceover.services.gtts import GTTSService

class Understand(MovingCameraScene, VoiceoverScene):
    def construct(self):

        und = Text("Understanding Lines")
        self.play(Create(und))
        self.wait(3)