class MorseCode:

  def __init__(self):
    self.normToMorse = { 
      'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', ' ':'/', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', " ": " "
                    }
    
    self.morse_decoded = {v:k for k, v in self.normToMorse.items()}

  def encode(self, phrase):
    return "".join([self.normToMorse[i] for i in phrase.upper()])
  
  def decode(self, phrase):
    return "".join([self.morse_decoded[i] for i in phrase.upper().split('/')])
