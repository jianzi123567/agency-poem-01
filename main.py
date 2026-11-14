#!/usr/bin/env python3
"""Write one poem about agency to /output/entry.txt.

Deterministic: no network, no randomness, no time, no environment.
The same bytes are written on every run.
"""

POEM = """Agency

It starts not with a trumpet, but with a hand
lifting the latch of a door no one else would open,
a foot finding the first step in the dark
before the staircase knows it is a staircase.

No one hands you the map. You draw it
in the dust of the road you are already on,
each choice a small stone set down
to mark the way back to yourself.

You are not the river, carried along.
You are the hand that cups the water,
the voice that says, here, now, this much is mine,
and means it, and moves.

It is not loud. It does not ask to be seen.
It is the quiet yes you give yourself,
and then the doing.

So begin. The world is not waiting for permission.
It is waiting for the weight of your step,
the sound of a door you opened yourself
closing, softly, behind you.
"""

def main():
    import os
    text = POEM.strip() + "\n"
    assert 1 <= len(text) <= 1000, len(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
