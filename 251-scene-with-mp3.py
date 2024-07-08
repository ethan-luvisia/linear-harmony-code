from manim import *
from manimusic import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
from manim_voiceover.services.gtts import GTTSService

class Example(MovingCameraScene, VoiceoverScene):
    CONFIG = {"include_sound": True}
    def construct(self):
        
        pt = 36
        staff = Staff(width = 9, height = 1, partition = pt, bars = [pt * (1 / 3) + 2, pt * (2 / 3) + 2])
        other_staff = Staff(width = 9, height = 1, partition = pt, bars = [pt * (1 / 3) + 2, pt * (2 / 3) + 2])
        lower_staff = Staff(width = 9, height = 1, partition = pt, bars = [pt * (1 / 3) + 2, pt * (2 / 3) + 2])
        lower_staff.move_to(DOWN)
        upper_staff = Staff(width = 9, height = 1, partition = pt, bars = [pt * (1 / 3) + 2, pt * (2 / 3) + 2])
        upper_staff.move_to(UP)
        new_upper_staff = Staff(width = 9, height = 1, partition = pt, bars = [pt * (1 / 3) + 2, pt * (2 / 3) + 2])
        new_upper_staff.move_to(UP)
        second_other_staff = Staff(width = 9, height = 1, partition = pt, bars = [pt * (1 / 3) + 2, pt * (2 / 3) + 2])

        octave = Text("Octave", font_size=72).move_to(UP)
        displacement = Text("Displacement", font_size=62).move_to(DOWN)
        diatonic = Text("Diatonic", font_size=60).next_to(staff, UP * 5)
        diatonic_underline = Underline(diatonic)
        diatonic_def = Text("Staying in/Derived from", font_size=35).next_to(staff, UP * 2.2)
        dd_cont = Text("the home key.", font_size=40).next_to(staff, UP * 0.1)

        ex1 = Text("Example 1" , font_size=36).next_to(lower_staff, DOWN * 1).shift(LEFT * 2.7)
        ex2 = Text("Example 2" , font_size=36).next_to(other_staff, UP * 4.5).shift(LEFT * 2.7)


        #measure 1 notes
        notes = VGroup(
            Note(staff, "cF1x", 4/pt),
            Note(staff, "cE1x", 6.66 /pt),
            Note(staff, "cD1x",  9.33 /pt),
            Note(staff, "cC1x", 12/pt),
            Note(staff, "cBx", 16/pt),
            Note(staff, "cAx", 18.5 /pt),
            Note(staff, "cGx",  21 /pt),
            Note(staff, "cFx", 24/pt),
            Note(staff, "cEx", 27.5 / pt)
        )

        notes_octave_up = VGroup(
            Note(staff, "cF1x", 4/pt),
            Note(staff, "cE1x", 6.66 /pt),
            Note(staff, "cD1x",  9.33 /pt),
            Note(staff, "cC1x", 12/pt),
            Note(staff, "cBx", 16/pt),
            Note(staff, "cA1x", 18.5 /pt),
            Note(staff, "cG1x",  21 /pt),
            Note(staff, "cF1x", 24/pt),
            Note(staff, "cE1x", 27.5 / pt)
        )

        notes_ls = VGroup(
            Note(lower_staff, "cF1x", 4/pt),
            Note(lower_staff, "cE1x", 6.66 /pt),
            Note(lower_staff, "cD1x",  9.33 /pt),
            Note(lower_staff, "cC1x", 12/pt),
            Note(lower_staff, "cBx", 16/pt),
            Note(lower_staff, "cAx", 18.5 /pt),
            Note(lower_staff, "cGx",  21 /pt),
            Note(lower_staff, "cFx", 24/pt),
            Note(lower_staff, "cEx", 27.5 / pt)
        )

        notes_other_staff = VGroup(
            Note(upper_staff, "cF1x", 4/pt),
            Note(upper_staff, "cE1x", 6.66 /pt),
            Note(upper_staff, "cD1x",  9.33 /pt),
            Note(upper_staff, "cC1x", 12/pt),
            Note(upper_staff, "cBx", 16/pt),
            Note(upper_staff, "cA1x", 18.5 /pt),
            Note(upper_staff, "cG1x",  21 /pt),
            Note(upper_staff, "cF1x", 24/pt),
            Note(upper_staff, "cE1x", 27.5 / pt)
        )

        #Underline animation
        
        # Initial Chords

        chords = VGroup(
            ChordLine(staff, "Dx|C1x|F1x", 4 / pt, glob = "c"),
            ChordLine(staff, "Gx|Bx|F1x", 16 / pt, glob = "c"),
            ChordLine(staff, "Cx|Bx|E1x", 28 / pt, glob = "c")
            )
        
        chord1 = Text("D-7").shift(2.5 * LEFT, 1.5 * DOWN)
        chord2 = Text("G7").shift(1.5* DOWN)
        chord3 = Text("Cmaj7").shift(3 * RIGHT, 1.5 * DOWN)
        roman1 = Text("II-7").shift(2.5 * LEFT, 2.25 * DOWN).set_fill("#90EE90", opacity=0.75)
        roman2 = Text("V7").shift(2.25* DOWN).set_fill("#90EE90", opacity=0.75)
        roman3 = Text("Imaj7").shift(3 * RIGHT, 2.25 * DOWN).set_fill("#90EE90", opacity=0.75)
        strong11 = Text("3rd")
        strong12 = Text("root")
        strong21 = Text("3rd")
        strong22 = Text("root")
        strong31 = Text("3rd")

        partition = staff.get_ticks()

        # Voiceover seting
        self.set_speech_service(GTTSService())
        
        self.play(Write(other_staff))
        self.wait(0.3)
        self.play(self.camera.frame.animate.set(width = staff.width * 1.2))
        self.wait(0.8)

        # Write chord analysis

       
        self.add_sound("1-3.wav")
        self.play(Write(chord1),
                Write(chord2),
                Write(chord3)
            )
        self.wait(7.5)

        self.play(chords[0].show_chord(Write))

        for i in range(1, len(chords)):
            base_chord = chords[i - 1]
            target_chord = chords[i]
            self.play(
                *[
                TransformFromCopy(
                    base_note.get_parts("body", "stem"),
                    target_note.get_parts("body", "stem"),
                    run_time = 2.0
                )
                for base_note, target_note in zip(base_chord, target_chord)
                ],
                LaggedAnim(
                    0.8,
                    *ShowAdditionLinesChord(target_chord, Write),
                )
            )
        self.wait(2)
        self.play(TransformFromCopy(chord1, roman1),
                  TransformFromCopy(chord2, roman2),
                  TransformFromCopy(chord3, roman3)
                  )
        self.play(FadeOut(chords, target_chord, base_chord, chords[2], staff), FadeIn(other_staff))
        self.wait(1)

        #Displaying Chord Progression, then Voice leading
        self.add_sound("1-4.wav")
        self.wait(16)



        # Connecting Thirds
        self.add_sound("1-5.wav")
        self.wait(3.4)
        self.play(FadeIn(notes[0]))
        for i in range(1, len(notes)):
            base_note = notes[i - 1]
            target_note = notes[i]
            self.play(
                TransformFromCopy(
                    base_note.get_parts("body"),
                    target_note.get_parts("body")
                ),

                *ShowAdditionLinesNote(target_note, Write),
                run_time = 0.25
            )

        self.wait(11)
        
        self.add_sound("2-1.wav")
        self.wait(13)
        self.play(Write(diatonic), Write(diatonic_underline))
        self.play(Write(diatonic_def))
        self.play(Write(dd_cont))
        self.wait(1.7)
        self.play(FadeOut(diatonic), FadeOut(diatonic_underline), FadeOut(diatonic_def), FadeOut(dd_cont))
        self.wait(1)

        # Strong chord tones, green highlight
        self.add_sound("2-2.wav")
        self.wait(3.8)
        for i in range(len(notes)):
            if i % 2 == 0:
                self.play(notes[i].animate.set_fill(GREEN, opacity=1), run_time=0.1)
        self.wait(2)
        
        # Removing beat 2 & 4 notes
        for i in range(len(notes)):
            if i % 2 == 1:
                self.play(notes[i].animate.set_fill(WHITE, opacity=0), run_time=0.1)
        self.wait(6)


        self.add_sound("2-3.wav")
        for i in range(len(notes)):
            if i % 2 == 1:
                self.play(notes[i].animate.set_fill(RED, opacity=1), run_time=0.1)
        self.wait(10)

        self.add_sound("2-4.wav")
        self.wait(6)
        for i in range(len(notes)):
            self.play(notes[i].animate.set_fill(WHITE, opacity=1), run_time=0.1)

        
        self.wait(8)
        self.add_sound("2-5.wav")
        self.wait(11)
            

        # Octave Displacement Scene
        self.add_sound("3-1.wav")
        
        self.wait(6)

        
        for i in range(5, len(notes)):
            self.play(Transform(notes[i], notes_octave_up[i]), run_time=0.3)
            if i == 5:
                self.play(notes_octave_up[5].show_note(Write), run_time=0.1)
        self.wait(3)

            # Octave Displacement MP3
        self.wait(3)

        self.add_sound("only-one.wav")
        self.wait(1.3)

                
        self.play(FadeOut(chord1, chord2, chord3, roman1, roman2, roman3), run_time=0.5)
        self.wait(0.5)

        
        for i in range(len(notes)):
            self.play(FadeOut(notes[i], notes_octave_up[i]), run_time=0.1)
            if i == len(notes) - 1:
                self.play(FadeOut(staff), FadeIn(staff), run_time = 0.01)
        self.wait(0.5)

        self.play(
            other_staff.animate.move_to(UP),
            TransformFromCopy(other_staff, lower_staff)   
        )

        self.wait(0.5)

        self.add_sound("previous-step-shorter.wav")
                
        for i in range(len(notes)):
            self.play(notes_other_staff[i].show_note(Write), notes_ls[i].show_note(Write), run_time=0.1)

        
        self.play(Write(ex1), Write(ex2))

        self.wait(2)
        
        # Implement Boxes that highlight each example and coordinate wait times
        box1 = Rectangle()
        
        


        self.wait(4)
        self.add_sound("excerpt-1.wav")
        self.play(lower_staff.animate.set_color(GREEN), ex1.animate.set_color(GREEN))
        self.wait(5)
        self.play(lower_staff.animate.set_color(WHITE), ex1.animate.set_color(WHITE))
        self.wait(0)
        self.play(other_staff.animate.set_color(GREEN), ex2.animate.set_color(GREEN))
        self.wait(0.3)
        self.add_sound("octave-displacement-piano.wav")
        self.wait(4.8)
        self.play(other_staff.animate.set_color(WHITE), ex2.animate.set_color(WHITE))

        #there used to be a wait1 here

        self.add_sound("this-is-cool.wav")
        for i in range(len(notes)):
            if i % 2 == 0:
                self.play(
                notes_other_staff[i].animate.set_fill(GREEN, opacity = 1),
                notes_ls[i].animate.set_fill(GREEN, opacity = 1),
                run_time = 0.25
                )
            elif i % 2 == 1:
                self.play(
                    notes_other_staff[i].animate.set_fill(RED, opacity = 1),
                    notes_ls[i].animate.set_fill(RED, opacity = 1),
                    run_time = 0.25
                )

        self.wait(6)

        for i in range(len(notes)):
            self.play(
                FadeOut(notes_other_staff[i], notes_ls[i], run_time=0.1),
                )
            
        self.play(
            Transform(other_staff, other_staff),
            Transform(lower_staff, other_staff),
            FadeOut(lower_staff, other_staff),
            *[FadeOut(mob)for mob in self.mobjects]
        )
            

        self.wait(2)
