def input_to_int(input):
    return int(str(input).strip())
    
def int_to_hex(int):
    i_hex = ('0' if int<0 else 'FF' if int>255 else hex(int)[2:])
    return i_hex

def rgb(r, g, b):
    r, g, b = input_to_int(r), input_to_int(g), input_to_int(b)
    r_hex, g_hex, b_hex = int_to_hex(r), int_to_hex(g), int_to_hex(b)
    rgb = [r_hex, g_hex, b_hex]
    rgb = ['0' + val if len(val) == 1 else val for val in rgb] 
    string = ''.join(rgb).upper()
    
    return string