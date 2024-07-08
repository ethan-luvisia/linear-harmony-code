from manim import *
from manimusic import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
from manim_voiceover.services.gtts import GTTSService

class ExampleCont(MovingCameraScene, VoiceoverScene):
    CONFIG = {"include_sound": True}
    def construct(self):
        # Staff
        pt = 40
        staff = Staff(clefs="g", width=9, partition=pt, bars=[pt * (1 / 3) + 2, pt * (2 / 3) + 2])
        clean_staff = Staff(clefs="g", width=9, partition=pt, bars=[pt * (1 / 3) + 2, pt * (2 / 3) + 2])
        scale_staff1 = Staff(clefs="g", width=9, partition=pt).move_to(1.25 * UP)
        scale_staff1_copy = Staff(clefs="g", width=9, partition=pt).move_to(1.25 * UP)
        scale_staff2 = Staff(clefs="g", width=9, partition=pt).move_to(1.25 * DOWN)
        scale_staff2_copy = Staff(clefs="g", width=9, partition=pt).move_to(1.25 * DOWN)
        clean_staff_again = Staff(clefs="g", width=9, partition=pt, bars=[pt * (1 / 3) + 2, pt * (2 / 3) + 2])
        partitions = staff.get_ticks(number_height=0.16)
        ks_flat = staff.get_flat_signature(1, 3.5 / pt)

        chord1 = Text("D-7").shift(2.5 * LEFT, 1.5 * DOWN)
        chord2 = Text("G7").shift(1.5* DOWN)
        chord3 = Text("Cmaj7").shift(3 * RIGHT, 1.5 * DOWN)

        # Modal Intercahnge Notes 

        notes_octave_up = VGroup(
            Note(staff, "cF1x", (5) / pt),
            Note(staff, "cE1x", (7.66) / pt),
            Note(staff, "cD1x", (10.33) / pt),
            Note(staff, "cC1x", (13) / pt),
            Note(staff, "cBx", (17) / pt),
            Note(staff, "cAb1x", (20.5) / pt),
            Note(staff, "cG1x", (22.8) / pt),
            Note(staff, "cEb1x", (26.5) / pt),
            Note(staff, "cE1xn", (32) / pt)
        )

        # For Scale Comparison
        scale_staff1_notes = VGroup(
            Note(scale_staff1_copy, "cCx", 6/pt),
            Note(scale_staff1_copy, "cDx", 11/pt),
            Note(scale_staff1_copy, "cEx",  16/pt),
            Note(scale_staff1_copy, "cFx", 21/pt),
            Note(scale_staff1_copy, "cGx", 26/pt),
            Note(scale_staff1_copy, "cAx", 31 /pt),
            Note(scale_staff1_copy, "cBx",  36 /pt)
        )

        scale_staff2_notes = VGroup(
            Note(scale_staff2_copy, "cCx", 6/pt),
            Note(scale_staff2_copy, "cDx", 11/pt),
            Note(scale_staff2_copy, "cEbx",  16/pt),
            Note(scale_staff2_copy, "cFx", 21/pt),
            Note(scale_staff2_copy, "cGx", 26/pt),
            Note(scale_staff2_copy, "cAbx", 31 /pt),
            Note(scale_staff2_copy, "cBbx",  36 /pt)
        )



        # Modal Interchange Text
        modal = Text("Modal", font_size=72).move_to(UP)
        interchange = Text("Interchange", font_size=72).move_to(DOWN)

        # Major and Minor Text
        major = Text("C Major", font_size = 40)
        minor = Text("C (Natural) Minor", font_size = 40)
        major.next_to(scale_staff1_copy, 0.7 * DOWN)
        minor.next_to(scale_staff2_copy, 0.7 * DOWN)

        # Speech Service
        self.set_speech_service(GTTSService())

        # MI Text
        self.play(Write(modal), Write(interchange))
        self.wait(1)
        
        self.play(FadeOut(modal), FadeOut(interchange), run_time=1)
        self.wait(0.5)

        # Continuing on with modal interchange Example:
        self.add_sound("4-1.wav")
        
        self.play(Write(clean_staff))
        self.play(self.camera.frame.animate.set(width = staff.width * 1.2))
        self.wait(3)

        for i in range(len(notes_octave_up)):
            self.play(notes_octave_up[i].show_note(Write), run_time=0.2)
            if i == 0:
                self.play(Write(chord1), run_time=0.2)
            elif i == 3:
                self.play(Write(chord2), run_time=0.2)
            elif i == len(notes_octave_up) - 1:
                self.play(Write(chord3), run_time=0.2)
        self.wait(3)
        
        self.wait(2)

        self.add_sound("4-2.wav")
        self.wait(8)
        self.play(Circumscribe(notes_octave_up[5], Circle, True, color=RED), Circumscribe(notes_octave_up[7], Circle, True, color=RED))
        self.wait(7)

        # Clear canvas for the scales
        self.play(FadeOut(chord1, chord2, chord3, staff))
        for i in range(len(notes_octave_up)):
             self.play(FadeOut(notes_octave_up[i]), run_time=0.05)


        # Two Scales Scene
        self.wait(1.2)
        self.add_sound("4-3.wav")
        self.play(
            ReplacementTransform(clean_staff, scale_staff1),
            Write(scale_staff2)
        )
            # Write scales
        for i in range(len(scale_staff1_notes)):
                self.play(
                    scale_staff1_notes[i].show_note(Write),
                    scale_staff2_notes[i].show_note(Write),
                    run_time=0.2
                )
        self.wait(1) 
     
        # Major Minor Text
        self.play(Write(major), Write(minor))
        self.wait(4)
            
            # Color the minor stuff orange :)
        for i in range(len(scale_staff2_notes)):
            if i == 2:
                scale_staff2_notes[i].set_color(ORANGE)
            elif i == 5:
                scale_staff2_notes[i].set_color(ORANGE)
            elif i == 6:
                scale_staff2_notes[i].set_color(ORANGE)
            elif i == 0:
                minor.set_color(ORANGE)

        self.wait(18)
        
        
        for i in range(len(scale_staff2_notes)):
            self.play(FadeOut(scale_staff1_notes[i], run_time=0.1), run_time=0.1)
            if i != 2 and i != 5:
                self.play(FadeOut(scale_staff2_notes[i], run_time=0.1), run_time=0.1)
        self.add_sound("4-4.wav")    

        self.play(FadeOut(scale_staff1, scale_staff1_copy, scale_staff2, scale_staff2_copy, major, minor))

            # Establish Transformation Scene
            

        self.play(Write(clean_staff_again))
        for i in range(len(notes_octave_up)):
            self.play(notes_octave_up[i].show_note(Write), run_time=0.2)
            
            
        self.play(ReplacementTransform(scale_staff2_notes[2], notes_octave_up[5]), FadeToColor(notes_octave_up[5], ORANGE), FadeToColor(notes_octave_up[5][1], ORANGE))
        self.play(ReplacementTransform(scale_staff2_notes[5], notes_octave_up[7]), FadeToColor(notes_octave_up[7], ORANGE))
        # Make Display the Chords 
        G7 = Text("G7").next_to(clean_staff_again, DOWN * 1)
        G7b9b13 = Text("G7(♭9,♭13)").next_to(G7, DOWN * 1).set_color(ORANGE)
        self.wait(6)
        self.play(Write(G7))
        self.wait(2)
        self.play(TransformFromCopy(G7, G7b9b13))
                    

        self.wait(10)