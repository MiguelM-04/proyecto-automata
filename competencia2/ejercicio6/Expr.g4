grammar Expr;

root: expr EOF;

expr: EOF;
NUM : [0-9]+ ;
MAS : '+' ;
POR : '*' ;
WS : [ \t\r\n]+ -> skip ;