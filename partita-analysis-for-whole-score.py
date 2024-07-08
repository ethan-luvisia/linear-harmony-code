from manim import *
from manimusic import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
from manim_voiceover.services.gtts import GTTSService

class Scene1(MovingCameraScene, VoiceoverScene):
    CONFIG = {"include_sound": True}
    def construct(self):


        pt = 6
        staff = Staff(clefs = "g", width = 4.3, height = 1.7, partition = pt).shift(UP * 1.3)
        staff_copy = Staff(clefs = "g", width = 4.3, height = 1.7, partition = pt).shift(UP * 1.3)
        partitions = staff.get_ticks(number_height = 0.16).set_color(YELLOW)
        # self.add(staff, partitions)

        chord1 = ChordLine(staff, "cDx|cFx|cAx", 0.6, 0)
        chord2 = ChordLine(staff, "cC#x|cGx|cAx|cE1x", 0.6, 0)
        chord3 =  ChordLine(staff, "cAx|cDx|cFx", 0.6, 0)
        chord4 =  ChordLine(staff, "cBbx|cDx|cFx", 0.6, 0)
        chord5 =  ChordLine(staff, "cA-1x|cC#x|cEx|cAx", 0.6, 0)
        passing1 =  ChordLine(staff, "cA-1x|cC#x|cEx|cGx", 0.6, 0)
        chord6 =  ChordLine(staff, "cDx|cFx|cAx", 0.6, 0)
        chord7 =  ChordLine(staff, "cEx|cGx|cBbx|cC1x", 0.6, 0)
        chord8 =  ChordLine(staff, "cFx|cAx|cC1x|cF1x", 0.6, 0) 

        # Underlining?
        d = VGroup(
            Dot().next_to(chord1, DOWN * 0.5),
            Dot().next_to(chord1, DOWN * 0.5)
        )

        line = Line(d[0], d[1])

        

        chord_text1 = Text("d", font_size = 90).next_to(staff, DOWN * 4.5)
        chord_text2 = Text("A/C#", font_size = 90).next_to(staff, DOWN * 4.5)
        chord_text3 = Text("d", font_size = 90).next_to(staff, DOWN * 4.5)
        chord_text4 = Text("B♭", font_size = 90).next_to(staff, DOWN * 4.5)
        chord_text5 = Text("A", font_size = 90).next_to(staff, DOWN * 4.5)
        ctpassing1 = Text("A7", font_size = 90).next_to(staff, DOWN * 4.5)
        chord_text6 = Text("d", font_size = 90).next_to(staff, DOWN * 4.5)
        chord_text7 = Text("C7", font_size = 90).next_to(staff, DOWN * 4.5)
        ul = Underline(chord_text1).next_to(chord_text1, DOWN * 1.5)
        ul.width = 2

        roman_text1 = Text("i", font_size = 90).next_to(staff, DOWN * 11).set_color(LIGHTER_GRAY)
        roman_text2 = Text("V6", font_size = 90).next_to(staff, DOWN * 11)
        roman_text3 = Text("i", font_size = 90).next_to(staff, DOWN * 11)
        roman_text4 = Text("VI", font_size = 90).next_to(staff, DOWN * 11)
        roman_text5 = Text("V", font_size = 90).next_to(staff, DOWN * 11)
        rpassing1 = Text("V7", font_size = 90).next_to(staff, DOWN * 11)
        roman_text6 = Text("i", font_size = 90).next_to(staff, DOWN * 11)
        roman_text7 = Text("V7/III", font_size = 90).next_to(staff, DOWN * 11)
        roman_text8 = Text("III", font_size = 90).next_to(staff, DOWN * 11)

        # Draw Main Canvas

        

        self.play(ShowStaff(staff_copy), self.camera.frame.animate.move_to(RIGHT * 3.9), Write(chord_text1), Write(roman_text1))
        self.add_sound("5-4.1.wav")
        # Underline
        self.play(Write(ul))

        

        self.wait(1)
        # self.add_sound("Measures.wav")
        self.play(chord1.show_chord(Write))
        chord1[1].save_state()
        chord1[2].save_state()
        staff.save_state()
        self.wait(15)
        
        self.wait(5)
        

        # D to A
        self.add_sound("5-4.2.wav")
        self.play(Transform(chord1[1], chord2[1]), Transform(chord1[2], chord2[2]), chord2[1].show_note(Write), chord2[2].show_note(Write), FadeOut(chord_text1), FadeIn(chord_text2), FadeOut(roman_text1), FadeIn(roman_text2))
        self.wait(2.6)
        # C64 to D/G
        self.play(Transform(chord1[1], chord3[1]), Transform(chord1[2], chord2[2]), FadeOut(chord2[1]), FadeOut(chord2[2]), FadeOut(chord_text2), FadeIn(chord_text3), FadeOut(roman_text2), FadeIn(roman_text3))
        self.wait(2.6)
        # Restore G
        self.play(Restore(chord1[2]), Transform(chord1[1], chord4[1]), FadeOut(staff), FadeOut(chord_text3), FadeIn(chord_text4), FadeOut(roman_text3), FadeIn(roman_text4))
        self.wait(1.6)
        self.play(Transform(chord1[1], passing1[1]))
        self.play(Transform(chord1[1], chord5[1]), FadeOut(chord_text4), FadeIn(chord_text5), FadeOut(roman_text4), FadeIn(roman_text5))
        self.wait(2.5)

        # VI to V/V
        self.play(Transform(chord1[0], chord6[0]), Transform(chord1[1], chord6[1]), Transform(chord1[2], chord6[2]), FadeOut(chord_text5), FadeOut(roman_text5), FadeIn(chord_text6), FadeIn(roman_text6))
        self.wait(2.8)
        self.play(Transform(chord1[0], chord7[0]), Transform(chord1[1], chord7[1]), Transform(chord1[2], chord7[2]), FadeOut(chord_text6), FadeOut(roman_text6), FadeIn(chord_text7), FadeIn(roman_text7), chord7[2].show_note(Write))
        self.wait(2.8)