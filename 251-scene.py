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
        displacement = Text("Displacement", font_size=72).move_to(DOWN)


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
        self.wait(1)
        self.play(self.camera.frame.animate.set(width = staff.width * 1.2))
        self.wait(1)

        # Write chord analysis

        with self.voiceover(text="Many great examples of linear harmony can be shown using the following chord progression  called a major two five one, which you might be familiar with.") as tracker:
            self.play(Write(chord1),
                    Write(chord2),
                    Write(chord3)
                )

        self.play(chords[0].show_chord(Write))

        for i in range(1, len(chords)):
            base_chord = chords[i - 1]
            target_chord = chords[i]
            self.play(
                *[
                TransformFromCopy(
                    base_note.get_parts("body", "stem"),
                    target_note.get_parts("body", "stem"),
                    run_time = 2
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
        with self.voiceover(text="It’s especially popular for improvising in jazz music. The roots of this chord progression move down in fifths, making it pretty convenient for building lines that connect smoothly into each other. Here’s some examples of this.") as tracker:
            self.wait(tracker.duration + 1)



        # Connecting Thirds

        with self.voiceover(text="We have incredible options for lines in the 251 department, but for now we’ll add a simple melody to our progression and listen to it with the bass notes.") as tracker:
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

        self.wait(1)
        
        with self.voiceover(text="This is a great sounding line, and what’s pretty neat is that If we take a look at the role that each of these notes play,") as tracker:
            for i in range(len(notes)):
                if i % 2 == 0:
                    self.play(notes[i].animate.set_fill(GREEN, opacity=1), run_time=0.1)
            self.wait(tracker.duration)


        with self.voiceover(text="you can see that the thirds and roots of the chords are placed on strong positions,  beats one and three highlighted in green") as tracker:
            for i in range(len(notes)):
                if i % 2 == 1:
                    self.play(notes[i].animate.set_fill(WHITE, opacity=0), run_time=0.1)
            self.wait(tracker.duration)

        with self.voiceover(text="These strong chord tones are then connected together with notes on the weak beats 2 and 4 that have a natural tendency to resolve downwards. In each of the chords the second and the seventh are doing the connections on the weak beats, highlighted in red. All of this is done with just downwards steps!") as tracker:
            for i in range(len(notes)):
                if i % 2 == 1:
                    self.play(notes[i].animate.set_fill(RED, opacity=1), run_time=0.1)
            self.wait(tracker.duration)

            for i in range(len(notes)):
                    self.play(notes[i].animate.set_fill(WHITE, opacity=1), run_time=0.1)
            

        # Octave Displacement Scene

        with self.voiceover(text="Now that we know more on how lines can form harmony, let’s explore more of the potential in this chord progression with a new concept.") as tracker:
            self.wait(tracker.duration)

        with self.voiceover(text="We’ll shift just a few notes and see what our new melody sounds like."):
            for i in range(5, len(notes)):
                self.play(Transform(notes[i], notes_octave_up[i]), run_time=0.3)
                if i == 5:
                    self.play(notes_octave_up[5].show_note(Write), run_time=0.1)
            self.wait(tracker.duration)

            # Octave Displacement MP3
            self.wait(2)

            with self.voiceover(text="Only one real change really occurred here:") as tracker:
                
                self.play(FadeOut(chord1, chord2, chord3, roman1, roman2, roman3), run_time=0.5)
                self.wait(0.5)

                for i in range(len(notes)):
                    self.play(FadeOut(notes[i], notes_octave_up[i]), run_time=0.1)
                    if i == len(notes) - 1:
                        self.play(FadeOut(staff), FadeIn(staff), run_time = 0.01)
                self.wait(tracker.duration)

                self.play(
                    other_staff.animate.move_to(UP),
                    TransformFromCopy(other_staff, lower_staff)   
                )

                self.wait(0.5)

            with self.voiceover(text="Our previous step down by a major second after the note B, was replaced by a leap up to the same note A in a higher octave.") as tracker:
                
                for i in range(len(notes)):
                    self.play(notes_other_staff[i].show_note(Write), notes_ls[i].show_note(Write), run_time=0.1)

                self.wait(2)
        
                

                self.wait(tracker.duration)

            with self.voiceover(text="This is a fantastic technique called Octave displacement, and as the name suggests, it adds spice to musical lines by creating a leap with what would’ve been a stepwise sequence.") as tracker:
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
                self.wait(tracker.duration)

            for i in range(len(notes)):
                self.play(
                    FadeOut(notes_other_staff[i], notes_ls[i], run_time=0.1),
                    )

            self.wait(1)
            
            self.play(
                Transform(other_staff, other_staff),
                Transform(lower_staff, other_staff),
                FadeOut(lower_staff, other_staff),
                *[FadeOut(mob)for mob in self.mobjects]
            )
            

            self.wait(2)



            