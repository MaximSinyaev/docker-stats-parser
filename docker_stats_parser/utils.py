import unicodedata, re, itertools, sys

all_chars = (chr(i) for i in range(sys.maxunicode))
categories = {'Cc', 'Cf', 'Cn', 'Co', 'Cs'}
control_chars = ''.join(c for c in all_chars if unicodedata.category(c) in categories) 
# or equivalently and much more efficiently
control_chars = ''.join(map(chr, itertools.chain(range(0x00,0x20), range(0x7f,0xa0))))

additional_chars = r'\x7f' + r'\x1b[2J' + r'\x1b' + u'\x1b[1;1H' + u'\x1b[?25l' + u'\x1b[?25h'
# control_chars = ''.join([control_chars, additional_chars])


control_char_re = re.compile('[%s]' % re.escape(control_chars))



def remove_control_chars(s):
    return control_char_re.sub('', s)

def is_float(element: any) -> bool:
    #If you expect None to be passed:
    if element is None: 
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False
