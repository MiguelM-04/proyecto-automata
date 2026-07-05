grammar Expr;

root: expr EOF;

expr: EOF;
IF: 'if';
ID: [a-z]+;
MAYOR:'>';
NUM: [0-9]+;
WS : [ \t\r\n]+ -> skip ;