grammar Expr;

root: expr EOF ;    

expr: EOF;
UPDATE: 'UPDATE';
SET: 'SET';
WHERE: 'WHERE';
IGUAL: '=';
PUNTO_COMA: ';';
COMA: ',';
CADENA: '\'' ~['\r\n]* '\'' ;
IDF: [a-zA-Z_][a-zA-Z0-9_]* ;
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;