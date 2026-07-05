grammar Expr;

root: expr EOF;

expr: EOF;
PRINT: 'print';
CADENA:'"' ~["\r\n]* '"' ;
WS : [ \t\r\n]+ -> skip ;