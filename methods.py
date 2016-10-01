class CorruptionMethod:
    def __init__(self, start_byte, end_byte, interval):
        self.start_byte = start_byte
        self.end_byte = end_byte
        self.interval = interval

    def corrupt(self, byte_array, settings):
        new_byte_array = bytearray(byte_array)
        for byte in range(self.start_byte, self.end_byte, self.interval):
            n = self.change(new_byte_array[byte], settings)
            new_byte_array[byte] = n
        return bytes(new_byte_array)

    def change(self, byte, kwargs):
        return byte


class ReplaceMethod(CorruptionMethod):
    def change(self, byte, settings):
        if byte == settings[0]:
            byte = settings[1]
        return byte

class AddMethod(CorruptionMethod):
    def change(self, byte, settings):
        if byte + settings[0] > 255: return byte + settings[0] - 255
        elif byte + settings[0] < 0: return 255 + byte + settings[0]
        else: return byte + settings[0]

class XorMethod(CorruptionMethod):
    def change(self, byte, settings):
        return byte ^ settings[0]

class SwapMethod(CorruptionMethod):
    def corrupt(self, byte_array, settings):
        new_byte_array = bytearray(byte_array)
        oldi = -1
        amount = settings[1]
        for byte in range(self.start_byte, self.end_byte, self.interval):
            if amount > 0:
                new = new_byte_array[byte:byte+settings[0]]
                newi = byte
                if oldi >= 0:
                    temp = old
                    new_byte_array[oldi:oldi+settings[0]] = new
                    new_byte_array[newi:newi+settings[0]] = temp
                old = new
                oldi = newi
                amount -= 1
        return bytes(new_byte_array)

class ReverseMethod(CorruptionMethod):
    def corrupt(self, byte_array, settings):
        new_byte_array = bytearray(byte_array)
        amount = settings[1]
        for byte in range(self.start_byte, self.end_byte, self.interval):
            if amount > 0:
                new_byte_array[byte:byte+settings[0]] = new_byte_array[byte:byte+settings[0]][::-1]
                amount -= 1
        return bytes(new_byte_array)