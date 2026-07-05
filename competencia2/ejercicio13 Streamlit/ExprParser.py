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
        4,1,29,10,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,2,0,2,0,0,
        7,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,
        8,5,0,0,1,8,3,1,0,0,0,0
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CREATE'", "'TABLE'", "'INSERT'", "'INTO'", 
                     "'VALUES'", "'SELECT'", "'FROM'", "'WHERE'", "'INNER'", 
                     "'JOIN'", "'ON'", "'SERIAL'", "'PRIMARY'", "'KEY'", 
                     "'VARCHAR'", "'NOT'", "'NULL'", "'INTEGER'", "'DATE'", 
                     "'('", "')'", "','", "';'", "'.'", "'='" ]

    symbolicNames = [ "<INVALID>", "CREATE", "TABLE", "INSERT", "INTO", 
                      "VALUES", "SELECT", "FROM", "WHERE", "INNER", "JOIN", 
                      "ON", "SERIAL", "PRIMARY", "KEY", "VARCHAR", "NOT", 
                      "NULL_", "INTEGER", "DATE", "PARENTESIS_IZQ", "PARENTESIS_DER", 
                      "COMA", "PUNTO_COMA", "PUNTO", "IGUAL", "CADENA", 
                      "IDF", "NUM", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    CREATE=1
    TABLE=2
    INSERT=3
    INTO=4
    VALUES=5
    SELECT=6
    FROM=7
    WHERE=8
    INNER=9
    JOIN=10
    ON=11
    SERIAL=12
    PRIMARY=13
    KEY=14
    VARCHAR=15
    NOT=16
    NULL_=17
    INTEGER=18
    DATE=19
    PARENTESIS_IZQ=20
    PARENTESIS_DER=21
    COMA=22
    PUNTO_COMA=23
    PUNTO=24
    IGUAL=25
    CADENA=26
    IDF=27
    NUM=28
    WS=29

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





