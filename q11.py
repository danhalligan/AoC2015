from string import ascii_lowercase
import re

class Password:
    def __init__(self, passwd):
        letters = list(ascii_lowercase)
        map =  {letters[i]: i for i in range(len(letters))}
        self.passwd = [map[x] for x in passwd]
    
    def increment(self):
        self._increment(self.passwd)
        return self
    
    def _increment(self, num):
        if (num[-1] < 25):
             num[-1] += 1
        else:
            num[-1] = 0
            num[:-1] = self._increment(num[:-1])
        return num
    
    def __str__(self):
        return ''.join([ascii_lowercase[x] for x in self.passwd])
    
    def __repr__(self):
        return str(self)
    
    def __len__(self):
        return len(self.passwd)
    
    def valid(self):
        return self.condition1() and self.condition2() and self.condition3()
    
    def condition1(self):
        for i in range(len(self) - 2):
            if (self.passwd[i:(i+3)] == [self.passwd[i], self.passwd[i]+1, self.passwd[i]+2]):
                return True
        return False
    
    def condition2(self):
        return not(bool(re.search(r'[iol]', str(self))))
    
    def condition3(self):
        return bool(re.search(r'(.)\1.*(.)\2', str(self)))
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.increment()
        while not self.valid():
            self.increment()
        return self


# Password('abcdefgz').increment()


# Password('hijklmmn').condition1()
# Password('hijklmmn').condition2()

# Password('abbceffg').condition3()
# Password('abbceffg').condition1()

# Password('abbcegjk').condition3()


# passwd = Password('abcdefgh')
# next(passwd)

# passwd = Password('ghijklmn')
# next(passwd)

passwd = Password('vzbxkghb')
next(passwd)
next(passwd)
