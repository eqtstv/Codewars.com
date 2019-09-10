class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key.decode('utf-8')
        self.alph = alphabet.decode('utf-8')+alphabet.decode('utf-8')
    
    def match_key_to_text(self, text):
        fixed_key = self.key
        if len(self.key) >= len(text):
            fixed_key = ''.join([self.key[i] for i in range(len(text))])
        else:
            i = 0
            while len(fixed_key)!= len(text):
                fixed_key += fixed_key[i]
                i += 1
        return fixed_key

    def encode(self, text):
        text = text.decode('utf-8')
        fixed_key = self.match_key_to_text(text)
        text_pos_encoded = [self.alph.index(text[i]) + self.alph.index(fixed_key[i]) if text[i] in self.alph else text[i] for i in range(len(text))]
        encoded = ''.join([self.alph[index] if type(index) is int else index for index in text_pos_encoded])
        return encoded.encode('utf-8')

    def decode(self, text):
        text = text.decode('utf-8')
        fixed_key = self.match_key_to_text(text)
        text_pos_decoded = [self.alph.index(text[i]) - self.alph.index(fixed_key[i]) if text[i] in self.alph else text[i] for i in range(len(text))]
        decoded = ''.join([self.alph[index] if type(index) is int else index for index in text_pos_decoded])
        return decoded.encode('utf-8')