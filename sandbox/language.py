def WordIgnore(word):
        ignoreWords=['very','really','literally','so']
        for part in ignoreWords:
                if part == word:
                        return True
        return False

def negatory(word):
        negations=['not','wont','cant']
        for part in negations:
                if part == word:
                        return True
        return False

def synonyms(wordA,wordB):
        if wordA == wordB:
                return True
        elif wordA == 'bad':
                if wordB == 'terrible':
                        return True
                if wordB == 'horrible':
                        return True
        else:
                return False
