grammar Expr;

root: expr EOF;

expr: EOF;

IDENT: [a-z];
IGUAL: '=';
NUM: [0-9]+;
WS : [ \t\r\n]+ -> skip ;