class PolybiusSquare:

    def __init__(self, word: str):
        self.word = word
        if 65 <= min([ord(i) for i in self.word]) <= 122:
            self.b = [['A', 'B', 'C', 'D', 'E'],
                      ['F', 'G', 'H', 'I', 'K'],
                      ['L', 'M', 'N', 'O', 'P'],
                      ['Q', 'R', 'S', 'T', 'U'],
                      ['V', 'W', 'X', 'Y', 'Z']]
        elif 1040 <= min([ord(i) for i in self.word]) <= 1103:
            self.b = [['А', 'Б', 'В', 'Г', 'Д', 'Е'],
                      ['Ё', 'Ж', 'З', 'И', 'Й', 'К'],
                      ['Л', 'М', 'Н', 'О', 'П', 'Р'],
                      ['С', 'Т', 'У', 'Ф', 'Х', 'Ц'],
                      ['Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
                      ['Э', 'Ю', 'Я', '-', '+', '=']]
        self.matrixHeight, self.matrixWidth = len(self.b), len(self.b[0])
        self.coordinate_horizontal, self.coordinate_vertical = [], []
        self.answer = []
        self.len = len(self.word)
        self.non_repeat_word = str()
        for i in range(len(self.word)):
            if not self.word[i] in self.word[0:i]:
                self.non_repeat_word += (self.word[i])

    def methods(self, decrypting: bool, method: int) -> str:
        if method == 1:
            if decrypting:
                self.answer = []
                for i in range(len(self.coordinate_horizontal)):
                    if self.coordinate_vertical[i] - 1 <= self.matrixHeight:
                        self.coordinate_vertical[i] -= 1
                    else:
                        self.coordinate_vertical[i] = self.matrixHeight
                    self.answer.append(
                        self.b
                        [self.coordinate_vertical[i] - 1]
                        [self.coordinate_horizontal[i] - 1]
                    )
            else:
                for i in range(len(self.coordinate_horizontal)):
                    if self.coordinate_vertical[i] + 1 <= self.matrixHeight:
                        self.coordinate_vertical[i] += 1
                    else:
                        self.coordinate_vertical[i] = 1
                    self.answer.append(
                        self.b
                        [self.coordinate_vertical[i] - 1]
                        [self.coordinate_horizontal[i] - 1]
                    )
            return ''.join(self.answer)
        else:
            if decrypting:
                self.answer, self.coordinate_vertical, self.coordinate_horizontal = [], [], []
                self.change_b()
                for k in range(len(self.word)):
                    symbol = self.word[k:len(self.word) - (len(self.word) - 1 - k)]
                    self.enumeration(symbol)

                for i in range(len(self.coordinate_horizontal)):
                    if self.coordinate_vertical[i] - 1 <= self.matrixHeight:
                        self.coordinate_vertical[i] -= 1
                    else:
                        self.coordinate_vertical[i] = 1
                    self.answer.append(
                        self.b
                        [self.coordinate_vertical[i] - 1]
                        [self.coordinate_horizontal[i] - 1]
                    )
            else:
                self.answer, self.coordinate_vertical, self.coordinate_horizontal = [], [], []
                self.change_b()
                for k in range(len(self.word)):
                    symbol = self.word[k:len(self.word) - (len(self.word) - 1 - k)]
                    self.enumeration(symbol)
                for i in range(len(self.coordinate_horizontal)):
                    if self.coordinate_vertical[i] + 1 <= self.matrixHeight:
                        self.coordinate_vertical[i] += 1
                    else:
                        self.coordinate_vertical[i] = self.matrixHeight
                    self.answer.append(
                        self.b
                        [self.coordinate_vertical[i] - 1]
                        [self.coordinate_horizontal[i] - 1]
                    )
        return ''.join(self.answer)

    def change_b(self) -> None:
        print(*self.b, sep='\n', end='\n\n')
        b2 = ' '.join(self.non_repeat_word).split()
        for u in range(len(self.b)):
            b2.extend(self.b[u])
        b2 = ''.join(b2).upper()

        b3 = str()
        for i in range(len(b2)):
            if not b2[i] in b2[0:i]:
                b3 += (b2[i])
        b3.upper()
        b2, loc = [], 0
        for i in range(len(self.b)):
            for j in range(len(self.b[0])):
                if j == len(self.b[0]) - 1:
                    loc += 1
            b2.extend([' '.join(b3[(j + 1) * (loc - 1):(j + 1) * loc]).upper().split()])
        self.coordinate_horizontal, self.coordinate_vertical = [], []
        self.b = b2

    def enumeration(self, symbol: str) -> tuple:
        for j in range(self.matrixHeight):
            for i in range(self.matrixWidth):
                if self.b[i][j].count(symbol.upper()) == 1:
                    self.coordinate_horizontal.append(j + 1)
                    self.coordinate_vertical.append(i + 1)
                    return self.coordinate_vertical, self.coordinate_horizontal

    def coordinate(self, word: str, decrypting: bool, method: int) -> str:
        self.word = word
        self.coordinate_vertical, self.coordinate_horizontal = [], []
        for k in range(len(self.word)):
            symbol = self.word[k:len(self.word) - (len(self.word) - 1 - k)]
            if symbol.lower() != 'j':
                self.coordinate_vertical, self.coordinate_horizontal = self.enumeration(symbol)
            else:
                self.coordinate_vertical, self.coordinate_horizontal = self.enumeration('i')
        return self.methods(decrypting, method)


if __name__ == '__main__':
    input_word = input()
    polybius_squareus = PolybiusSquare(input_word)

    polybius_1_encrypted = polybius_squareus.coordinate(input_word, False, 1)
    polybius_1_decrypted = polybius_squareus.coordinate(polybius_1_encrypted, True, 1)

    polibius_2_encrypted = polybius_squareus.coordinate(input_word, False, 2)
    polibius_2_decrypted = polybius_squareus.coordinate(polibius_2_encrypted, True, 2)

    print('Введенное слово                  '
          '{}\nЗашифованое слово Методом 1      '
          '{}\nЗашифованое слово Методом 2      '
          '{}\nРасшифрованное слово Методом 1   '
          '{}\nРасшифрованное слово Методом 2   {}'
          ''.format(
                    input_word.upper(),
                    polybius_1_encrypted,
                    polibius_2_encrypted,
                    polybius_1_decrypted,
                    polibius_2_decrypted)
                   )
