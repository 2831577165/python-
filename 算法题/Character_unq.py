class ChracterUnq:
    def character_unq(self):
        s = 'hdasujhdiawhda'
        q = set(s)
        if len(s) > len(q):
            return False
        else:
            return True

if __name__ == '__main__':
    print(ChracterUnq().character_unq())