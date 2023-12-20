class Encryption:
    def __init__(self, file_name, key):
        self.file = file_name
        self.file_bin = []
        self.file_bin_e = []
        self.file_bin_new_e = []
        self.file_e = ""
        self.key = key
        for f in self.file.read():
            self.file_bin.append(int(bin(f)[2:]))

    def show_binary(self):
        print(self.file_bin)

    def key_to_binary(self):
        l = []
        for i in self.key:
            l.append(str(bin(ord(i))[2:]))
        return l

    def encryption(self):
        key_binary = self.key_to_binary()
        counter = 0
        for i in self.file_bin:
            for k in key_binary:
                if counter == 0:
                    i = bin(int(str(i), 2) + int(str(k), 2))
                elif counter == 1:
                    i = bin(int(str(i), 2) + int(str(k), 2))

            self.file_bin_e.append(i[2:])

        count = 0
        len_of_key = len(self.key)
        for x in self.file_bin_e:
            s = bin(int(str(x), 2) + int(str(key_binary[count]), 2))
            if count == len_of_key - 1:
                count = 0
            else:
                count += 1
            self.file_bin_new_e.append(s[2:])
        
        for e in self.file_bin_new_e:
            self.file_e += str(hex(int(e, 2))).strip("0x2")
            if len(str(hex(int(e, 2))).strip("0x2"))>3:
                len_check += 1
        print(self.file_e)

#Max password length is 30
en = Encryption(open("e", mode="rb"), "samosamo")
en.encryption()
