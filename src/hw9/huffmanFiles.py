import os
from encode_decode import encode_f, decode_f
from work_with_bytes import byte_to_bit, bit_to_byte


class HuffmanFile:
    def __init__(self, path: str):
        self.path = path
        self.format = self.__find_format()
        self.file_opened = None
        self.__open_file()

    def __find_format(self):
        if self.path.endswith("txt"):
            return "txt"
        elif self.path.endswith("bin"):
            return "bin"
        raise InvalidFormat("file isn't txt or bin")

    def __open_file(self):
        try:
            if self.format == "txt":
                self.file_opened = open(self.path, "a+", encoding="utf-8")
            else:
                self.file_opened = open(self.path, "ab+")
        except:
            print("error: unable to open file")

    def to_txt(self):
        if self.format == "txt":
            print("Already txt")
            return False
        if self.file_opened == None:
            print("file isn't open")
            return False

        # prepare for reading after writing
        self.file_opened.seek(0)
        # save text from bin file
        # self.file_opened.read() -> class <bytes>
        # byte_to_bit(self.file_opened.read()) -> class <str>
        bin_text = byte_to_bit(self.file_opened.read())
        old_path = self.path
        new_path = self.path[:-3] + "txt"

        self.close()
        os.remove(old_path)

        with open(new_path, "w", encoding="utf-8") as f:
            f.write(decode_f(bin_text))

        self.path = new_path
        self.format = "txt"
        self.__open_file()
        return True

    def to_bin(self):
        if self.format == "bin":
            print("Already bin")
            return False
        if self.file_opened == None:
            print("file isn't open")
            return False

        self.file_opened.seek(0)
        # class utf_text is str
        utf_text = self.file_opened.read()
        old_path = self.path
        new_path = self.path[:-3] + "bin"

        self.close()
        os.remove(old_path)

        with open(new_path, "wb") as f:
            f.write(bit_to_byte((encode_f(utf_text))))

        self.path = new_path
        self.format = "bin"
        self.__open_file()
        return True

    def write(self, msg):
        """
        write to the end of the line
        """
        if self.file_opened == None:
            print("file isn't open")
            return False
        if self.format == "bin":
            print("only for txt")
            return False
        self.file_opened.write(msg)
        return True

    def close(self):
        if self.file_opened != None:
            self.file_opened.close()
            self.file_opened = None
            self.path = ""

    def __del__(self):
        self.close()
