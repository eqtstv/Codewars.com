def decodeMorse(morse_code):
    morse_list = morse_code.strip().split(' ')
    decoded = ''.join([x.replace(x, MORSE_CODE[x]) if x else ' ' for x in morse_list]).replace('  ', ' ')
    return decoded