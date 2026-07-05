# Generated from ./Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,10,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,2,0,2,0,0,
        7,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,
        8,5,0,0,1,8,3,1,0,0,0,0
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'public'", "'class'", "<INVALID>", "'{'", 
                     "'static'", "'void'", "'main'", "'('", "')'", "'int'", 
                     "'='", "<INVALID>", "';'", "'}'", "'['", "']'", "'+'", 
                     "'.'", "'\"'", "':'", "'*'" ]

    symbolicNames = [ "<INVALID>", "PUBLIC", "CLASS", "IDF", "LLAVE_IZQ", 
                      "STATIC", "VOID", "MAIN", "PARENTESIS_IZQ", "PARENTESIS_DER", 
                      "INT", "IGUAL", "NUM", "PUNTO_COMA", "LLAVE_DER", 
                      "CORCHETE_IZQ", "CORCHETE_DER", "MAS", "PUNTO", "COMILLAS", 
                      "DOS_PUNTOS", "ASTER", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    PUBLIC=1
    CLASS=2
    IDF=3
    LLAVE_IZQ=4
    STATIC=5
    VOID=6
    MAIN=7
    PARENTESIS_IZQ=8
    PARENTESIS_DER=9
    INT=10
    IGUAL=11
    NUM=12
    PUNTO_COMA=13
    LLAVE_DER=14
    CORCHETE_IZQ=15
    CORCHETE_DER=16
    MAS=17
    PUNTO=18
    COMILLAS=19
    DOS_PUNTOS=20
    ASTER=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr()
            self.state = 5
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





