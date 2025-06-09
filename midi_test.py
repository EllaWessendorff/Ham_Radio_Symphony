import mido
import time

# Change this to your IAC Driver port name exactly as it appears in MIDI Studio
MIDI_PORT_NAME = 'IAC Driver Bus 1'

def main():
    try:
        outport = mido.open_output(MIDI_PORT_NAME)
        print(f"Opened MIDI output port: {MIDI_PORT_NAME}")
    except IOError:
        print(f"Could not open MIDI output port: {MIDI_PORT_NAME}")
        return

    # Send a middle C note on (note 60) with velocity 100
    note_on = mido.Message('note_on', note=60, velocity=100)
    outport.send(note_on)
    print("Sent Note ON")

    time.sleep(1)  # Hold note for 1 second

    # Send the note off
    note_off = mido.Message('note_off', note=60)
    outport.send(note_off)
    print("Sent Note OFF")

    outport.close()

if __name__ == "__main__":
    main()
