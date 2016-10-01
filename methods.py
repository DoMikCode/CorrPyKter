class CorruptionMethod:
    def __init__(self, start_byte, end_byte, interval):
        self.start_byte = start_byte
        self.end_byte = end_byte
        self.interval = interval

    def corrupt(self, byte_array, **kwargs):
        new_byte_array = bytearray(byte_array, 'utf-8')
        for byte in range(self.start_byte, self.end_byte, self.interval):
            n = self.change(new_byte_array[byte], **kwargs)
            new_byte_array[byte] = n
        return bytes(new_byte_array)

    def change(self, byte, **kwargs):
        return byte


class ReplaceMethod(CorruptionMethod):
    def change(self, byte, **kwargs):
        print(byte, kwargs['byte_a'])
        if byte == kwargs['byte_a']:
            byte = kwargs['byte_b']
        return byte
