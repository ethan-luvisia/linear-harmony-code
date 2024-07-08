from manim import *
from manimusic import *

class Example(MovingCameraScene):
    def construct(self):
        # Staff
        pt = 40
        staff = Staff(clefs="g", width=13, partition=pt, bars=[2])
        partitions = staff.get_ticks(number_height=0.16)
        ks_flat = staff.get_flat_signature(1, 3.5 / pt)

        
        

        # Notes
        melody_l = Melody(staff, "D.|D.|E|F|G|A|Bb|C#|Bb|A|G|E1.|G",   0.15, 0, increment = 2 / 40, glob="cu")
        chord = ChordLine(staff, "D|F|A", 0.2, merge_stems=True)
        
        # Scene
        self.play(ShowStaff(staff))
        self.wait(0.5)

        self.play(Write(chord), self.camera.frame.animate.move_to(chord).set(width = chord[0].width * 30))
        self.wait(0.5)