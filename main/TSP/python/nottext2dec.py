class nottext2dec:
    def __init__(self, text=None):
        self.s = 0
        str(text)
        if text is None:
            self.text="The Dragon's Ball"
        else:
            self.text = text

    def notextdec(self):
        for i in self.text:
            if (ord(i) < 110):
                self.s = self.s * 10 + ord(i) - 100
            else:
                self.s = self.s * 100 + ord(i) - 100

        return self.s

    def sumtext(self):
        for i in self.text:
            self.s += ord(i)

        return self.s