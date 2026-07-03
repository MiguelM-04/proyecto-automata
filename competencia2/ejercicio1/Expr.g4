grammar Expr;

root: expr EOF;

expr: EOF;
MAS: '+';
NUM: [0-9]+;
WS : [ \t\r\n]+ -> skip ;