grammar Expr;
root: expr EOF;
expr: EOF;

INT: 'int';
IDENT: [a-z]+;
IGUAL: '=';
NUM: [0-9]+;
WS : [ \t\r\n]+ -> skip ;