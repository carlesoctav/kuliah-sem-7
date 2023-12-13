EOF = 3
digits = set(list("0123456789"))
lettersdigitsunderscore = set(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789"))
letters = set(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
ws = set(list(" \t\n\r"))
badidentifiertoken = 1
notAChar = 2


import io
import copy

class StreamReader:

    def __init__(self, instream):
        self.instream = instream
        self.nextChars = ""
        self.EOF = False
        self.line = 1
        self.column = 0
        self.charsRead = 0


    def readChar(self):

        if len(self.nextChars) > 0:
            nextChar = self.nextChars[0]
            self.nextChars = self.nextChars[1:]

        else:
            nextChar = self.instream.read(1)

        if nextChar == "":
            nextChar = chr(EOF)

        elif nextChar == '\n':
            self.line+=1
            self.column = 0

        else:
            self.column+=1


        if nextChar == chr(EOF):
            self.EOF = True

        self.charsRead += 1

        return nextChar

    def unreadChar(self, ch):
        if len(ch) == 0:
            return

        if len(ch) != 1:
            raise Exception(notAChar)

        self.EOF = False

        self.nextChars = ch + self.nextChars

        if ch == '\n':
            self.line-=1
        else:
            self.column-=1

        self.charsRead -= 1

    def numCharsRead(self):
        # return the number of characters read. This is useful when backtracking is performed
        # in case no progress is being made in reading the stream.
        return self.charsRead

    def eof(self):
        return self.EOF

    def readUpTo(self, delimiter):
        result = ""

        done = False

        while not done and not self.eof():

            c = self.readChar()

            if not self.eof():
                result += c

            if result[-len(delimiter):] == delimiter:
                done = True

        return result

    def readInt(self):
        number = ""

        self.skipWhiteSpace()

        digit = self.readChar()

        while digit in digits:
            number += digit
            digit = self.readChar()

        self.unreadChar(digit)

        return int(number)

    def readIdentifier(self):
        id = ""

        self.skipWhiteSpace()

        c = self.readChar()

        if not c in letters:
            print("Bad identifier token found in source file starting with", c, "at line", self.line, "and column", self.column)
            raise Exception(badidentifiertoken)

        while c in lettersdigitsunderscore:
            id += c
            c = self.readChar()

        self.unreadChar(c)

        return id

    def skipWhiteSpace(self):
        c = self.readChar()

        while c in ws:
            c = self.readChar()

        self.unreadChar(c)


    def peek(self, value):
        # Skip white space, then look for the value as the next characters in the input file.
        # Remember the read characters, but return true if they are found and false otherwise.

        readChars = ""

        self.skipWhiteSpace()

        done = False

        while len(readChars) < len(value) and not done:
            c = self.readChar()
            if c == EOF:
                done = True
            else:
                readChars += c

        for i in range(len(readChars)-1,-1,-1):
            self.unreadChar(readChars[i])

        if readChars == value:
            return True

        return False

    def skipComments(self):
        # skip comments

        while self.peek("(*"):
            self.readUpTo("*)")

    def getLineNumber(self):
        return self.line

    def getColNumber(self):
        return self.column

    def getToken(self):
        self.skipWhiteSpace()
        c = self.readChar()

        if c in digits:
            self.unreadChar(c)
            return self.readInt()

        if c in letters:
            self.unreadChar(c)
            return self.readIdentifier()

        return c
    


epsilon = ""

class NPDA:
    def __init__(self, delta, startStateId, stackStartSym, finalStates):
        self.delta = delta
        self.startStateId = startStateId
        self.stackStartSym = stackStartSym
        self.finalStates = finalStates

    # This is a working recursive version of accepts
    #def accepts(self,strm):

        #def matchTop(aStackTop, stack):
            #return stack[-1] == aStackTop

        #def getTransitions(stateId, stack):
            #transitionList = []

            #for aStateId, anInputSym, aStackTop in self.delta.keys():
                #if stateId == aStateId and matchTop(aStackTop, stack):
                    #transitionList.append((anInputSym, aStackTop))

            #return transitionList

        #def popPush(aStackTop, pushOnStack, stack):
            #newstack = stack[:]
            #for x in aStackTop:
                #newstack.pop()
            #for x in pushOnStack[::-1]:
                #newstack.append(x)
            #return newstack


        #def acceptsSuffix(stateId, stack):

            #c = strm.readChar()
            ##print(stateId, c, stack)

            #if strm.eof() and stateId in self.finalStates:
                ##print(stateId)
                #return True

            #strm.unreadChar(c)

            #for anInputSym, aStackTop in getTransitions(stateId, stack):
                #for toStateId, pushOnStack in self.delta[(stateId, anInputSym, aStackTop)]:
                    #if anInputSym == epsilon and acceptsSuffix(toStateId,popPush(aStackTop,pushOnStack,stack)):
                            #return True
                    #else: # not an epsilon transition
                        #c = strm.readChar()
                        #if c == anInputSym and acceptsSuffix(toStateId,popPush(aStackTop,pushOnStack,stack)):
                            #return True
                        #strm.unreadChar(c)

            #return False

        #return acceptsSuffix(self.startStateId, [self.stackStartSym])

    # This is an iterative version of accepts that works. It maintains
    # a stack of instantaneous descriptions that have yet to be explored.
    def accepts(self,strm):

        def matchTop(aStackTop, stack):
            return stack[-1] == aStackTop

        def getTransitions(stateId, stack):
            transitionList = []

            for aStateId, anInputSym, aStackTop in self.delta.keys():
                if stateId == aStateId and matchTop(aStackTop, stack):
                    transitionList.append((anInputSym, aStackTop))

            return transitionList

        def popPush(aStackTop, pushOnStack, stack):
            newstack = stack[:]
            for x in aStackTop:
                newstack.pop()
            for x in pushOnStack[::-1]:
                newstack.append(x)
            return newstack


        stateId = self.startStateId
        pdaStack = [self.stackStartSym]

        # This is the instantaneous description stack. It starts with the start state
        # instantaneous description.
        ID = [(stateId, strm, pdaStack)]
        

        while not len(ID) == 0:
            print(f"==>> ID: {ID}")
            stateId, strm, pdaStack = ID.pop()
            print((stateId, strm, pdaStack))
            c = strm.readChar()
            
            if strm.eof() and stateId in self.finalStates:
                return True

            strm.unreadChar(c)

            for anInputSym, aStackTop in getTransitions(stateId, pdaStack):
                print(f"==>> anInputSym: {anInputSym}")
                print(f"==>> aStackTop: {aStackTop}")
                for toStateId, pushOnStack in self.delta[(stateId, anInputSym, aStackTop)]:
                    if anInputSym == epsilon:
                        print("is there any lambda")
                        ID.append((toStateId,copy.deepcopy(strm),popPush(aStackTop,pushOnStack,pdaStack)))
                    else: # not an epsilon transition
                        c = strm.readChar()
                        if c == anInputSym:
                            ID.append((toStateId,copy.deepcopy(strm),popPush(aStackTop,pushOnStack,pdaStack)))
                        strm.unreadChar(c)

        return False


def main():

    # delta = {}

    # # delta[(statedId, inputsym, stacktop)] = (newstateid, stacktop')
    # #This is a^n b^n
    # #delta[(0, "a", "0")] = set([(1,"10")])
    # #delta[(0, epsilon, "0")] = set([(3, "")])
    # #delta[(1,"a","1")] = set([(1,"11")])
    # #delta[(1,"b","1")] = set([(2,"")])
    # #delta[(2,"b","1")] = set([(2,"")])
    # #delta[(2,epsilon,"0")] = set([(3,"")])
    # #npda = NPDA(delta,0,"0",set([3]))

    # #This is ww^R the a word with its reverse appended. Language of a's and b's.
    # delta[(0,"a","a")] = set([(0,"aa")])
    # delta[(0,"b","a")] = set([(0,"ba")])
    # delta[(0,"a","b")] = set([(0,"ab")])
    # delta[(0,"b","b")] = set([(0,"bb")])
    # delta[(0,"a","z")] = set([(0,"az")])
    # delta[(0,"b","z")] = set([(0,"bz")])

    # delta[(0,epsilon,"a")] = set([(1,"a")])
    # delta[(0,epsilon,"b")] = set([(1,"b")])

    # delta[(1,"a","a")] = set([(1,"")])
    # delta[(1,"b","b")] = set([(1,"")])

    # delta[(1,epsilon,"z")] = set([(2,"z")])

    delta = {
        (0, 'a', ''):set([(1, 'a'), ( 4, '')]),
        (1, 'a', ''): set([(1, 'a')]),
        (1, 'b', 'a'): set([(2, '')]),
        (2, 'b', 'a'): set([(2, '')]),
        (2, 'c', ''): set([(3, '')]),
        (3, 'c', ''): set([(3, '')]),
        (3, '', 'z'): set([(7, '')]),
        (4, 'a', ''): set([(4, 'a')]),
        (4, 'b', ''): set([(5, 'b')]),
        (5, 'b', ''): set([(5, 'b')]),
        (5, 'c', 'b'): set([(6, '')]),
        (6, 'c', 'b'): set([(6, '')]),
        (6, '', 'z'): set([(7, '')]),
    }


    npda = NPDA(delta,0,"z",set([7]))

    x = input("Please enter a string of a's and b's: ")

    if npda.accepts(StreamReader(io.StringIO(x))):
        print("Yes, in the language.")
    else:
        print("Nope! Not in the language.")

if __name__ == "__main__":
    main()
