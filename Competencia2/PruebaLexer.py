# Generated from Prueba.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,2,16,6,-1,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,0,0,2,1,1,3,2,1,0,0,15,0,1,1,0,0,0,0,3,1,0,0,0,1,5,1,0,
        0,0,3,10,1,0,0,0,5,6,5,104,0,0,6,7,5,111,0,0,7,8,5,108,0,0,8,9,5,
        97,0,0,9,2,1,0,0,0,10,11,5,109,0,0,11,12,5,117,0,0,12,13,5,110,0,
        0,13,14,5,100,0,0,14,15,5,111,0,0,15,4,1,0,0,0,1,0,0
    ]

class PruebaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'hola'", "'mundo'" ]

    symbolicNames = [ "<INVALID>",
 ]

    ruleNames = [ "T__0", "T__1" ]

    grammarFileName = "Prueba.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


