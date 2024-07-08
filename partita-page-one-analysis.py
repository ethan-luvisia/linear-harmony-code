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
        chord2 = ChordLine(staff, "cC#x|cGlx|cAx|cE1x", 0.6, 0)
        chord3 =  ChordLine(staff, "cA-1x|cDx|cFx", 0.6, 0)
        chord4 =  ChordLine(staff, "cBb-1x|cDx|cFx", 0.6, 0)
        # For smoothness of green animation 
        chord4[0].set_color(GREEN)
        chord5 =  ChordLine(staff, "cA-1x|cC#x|cEx|cAx", 0.6, 0)
        passing1 =  ChordLine(staff, "cA-1x|cC#x|cEx|cGx", 0.6, 0)
        chord6 =  ChordLine(staff, "cDx|cFx|cAx", 0.6, 0)
        chord7 =  ChordLine(staff, "cEx|cGx|cBbx|cC1x", 0.6, 0)
        chord8 =  ChordLine(staff, "cFx|cAx|cC1x|cF1x", 0.6, 0)
        note_g = Note(staff, "cGrx", 0.6, 0).set_color(RED)

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
        self.wait(4)
        self.play(chord1[0].animate.set_color(GREEN))
        self.wait(0.6)
        self.play(chord1[1].animate.set_color(GREEN))
        self.wait(0.5)
        self.play(chord1[2].animate.set_color(GREEN))
        self.wait(2.5)
        # measure1 mp3
        self.add_sound("p1.wav")
        self.wait(4)
        self.play(chord1[0].animate.set_color(WHITE), chord1[1].animate.set_color(WHITE), chord1[2].animate.set_color(WHITE), run_time=1)

        

        # D to A
        self.add_sound("5-4.2.wav")
        self.play(Transform(chord1[0], chord2[0]), Transform(chord1[1], chord2[1]), Transform(chord1[2], chord2[2]), Write(chord2[3]), FadeOut(chord_text1), FadeIn(chord_text2), FadeOut(roman_text1), FadeIn(roman_text2), Write(chord2.additional_lines))
        self.wait(6)
        self.play(chord2[0].animate.set_color(GREEN))
        self.wait(0.6)
        self.play(chord2[2].animate.set_color(GREEN))
        self.wait(0.6)
        self.play(chord2[3].animate.set_color(GREEN))
        self.wait(4)
        self.play(chord2[1].animate.set_color(GREEN))
        self.wait(3)
        #measure 1 music 2
        self.add_sound("p2.wav")
        self.wait(4)
        self.add_sound("5-4.3.wav")
        self.wait(10)
        self.play(chord2[0].animate.set_color(WHITE), chord2[1].animate.set_color(WHITE), chord2[2].animate.set_color(WHITE), chord2[3].animate.set_color(WHITE), run_time=1)
        self.wait(1)
        
        # A - d - Bb
        self.add_sound("5-4.4project.wav")
        self.play(Transform(chord1[0], chord3[0]), Transform(chord1[1], chord3[1]), Transform(Measure1, Measure2), FadeIn(chord3[2]), FadeOut(chord2[2]), FadeOut(chord1[2]), FadeOut(chord2[0]), FadeOut(chord2[1]), FadeOut(chord2[3]), FadeOut(chord_text2), FadeIn(chord_text3), FadeOut(roman_text2), FadeIn(roman_text3), Write(chord3.additional_lines))
        self.wait(4)
        #color third and root
        self.play(chord1[0].animate.set_color(GREEN), chord3[1].animate.set_color(GREEN), chord3[2].animate.set_color(GREEN))
        self.wait(1)
        # Move to Bb
        self.play(FadeOut(staff.additional_lines[1]), Transform(chord1[0], chord4[0]), FadeOut(chord_text3), FadeIn(chord_text4), FadeOut(roman_text3), FadeIn(roman_text4))
        self.wait(8)

        self.wait(2.5)
        self.add_sound("5-4.5.wav")
        self.play(FadeIn(note_g))
        self.wait(1.2)
        # VI to V/V
        # self.play(Transform(chord1[0], chord5[1]), Transform(chord1[1], chord5[2]), Transform(chord4[0], chord5[0]), FadeOut(chord_text4), FadeOut(roman_text4), FadeIn(chord_text5), FadeIn(roman_text5), Write(chord5[0].additional_lines))
        self.play(FadeOut(chord1[0], chord1[1], chord3[1], note_g, chord3[2]), FadeOut(chord_text4), FadeIn(chord_text5), FadeOut(roman_text4), FadeIn(roman_text5))
        self.play(chord5.show_chord(Write))
        self.wait(3)
        # self.play(Transform(chord1[0], chord7[0]), Transform(chord1[1], chord7[1]), Transform(chord1[2], chord7[2]), FadeOut(chord_text6), FadeOut(roman_text6), FadeIn(chord_text7), FadeIn(roman_text7), chord7[2].show_note(Write))
        self.wait(2.8)