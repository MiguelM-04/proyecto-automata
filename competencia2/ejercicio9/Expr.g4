grammar Expr;

root: expr EOF;

expr: EOF;
IF : 'if' ;
ID : [a-zA-Z]+ ;
MAYOR : '>' ;
NUM: [0-9]+;
PAR_IZQ : '(' ;
PAR_DER : ')' ;
WS : [ \t\r\n]+ -> skip ;