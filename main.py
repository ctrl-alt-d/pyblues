import itertools
import os

import mingus.extra.lilypond as LilyPond
from mingus.core import progressions
from mingus.containers import Bar,Track

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

#basic blues progression 
my_progression = [
    "I",	"I",	"I",	"I",
    "IV",	"IV",	"I",	"I",
    "V",	"V",	"I",	"I",
]

#getting the chords for the progression
my_chords = progressions.to_chords(my_progression)

#add a 4th note on each chord
my_chords = [ my_chord + [my_chord[1]] for my_chord in my_chords ]

#grouping notes as 4x4
all_notes = list(itertools.chain(*my_chords))
all_notes_4x4 = chunks(all_notes,4)

#generating the track
my_track = Track()
for my4notes in all_notes_4x4:
    my_bar = Bar()
    for my_note in my4notes:
        my_bar + my_note
    my_track + my_bar

#exporting
my_lilypond = LilyPond.from_Track(my_track)
_folder = "Scores"
_file = "poc"
_path = os.path.join(_folder,_file)
LilyPond.to_png(my_lilypond, _path )