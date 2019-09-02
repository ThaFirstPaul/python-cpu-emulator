import traceback

class NoHDDFileError(Exception):
    pass

class writer():
    def __init__(self, file):
        try:
            self.filename = file
            hdd_file = open(self.filename, 'r')
            self.hdd = hdd_file.readlines()
            hdd_file.close()
        except FileNotFoundError:
            raise FileNotFoundError("File '{}' was not found!".format(file))

    def getraw(self):
        return self.hdd

    def get(self, line=-1):
        if line < 0: return self.hdd
        else: return self.hdd[line]

    def length(self):
        return len(self.hdd)

    def write(self, towrite):
        try:
            hdd_file = open(self.filename, 'w')
            
            for i in range(0,1024):
                hdd_file.write(towrite[i])
            hdd_file.close()
        finally:
            hdd_file.close()

    
if __name__ == '__main__':
    w = writer('test.txt')
    while True:
        try:
            theinp = input('>')
            if theinp.isidentifier():
                exec('print({})'.format(theinp))
            else:
                exec(theinp)
            
        except KeyboardInterrupt:
            break
        except Exception:
            traceback.print_exc()
            continue
