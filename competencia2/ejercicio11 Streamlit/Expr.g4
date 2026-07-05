grammar Expr;

root: expr EOF ;    

expr: EOF;
PUBLIC:'public';
CLASS:'class';
IDF: [a-zA-Z]+ ;
LLAVE_IZQ:'{';
STATIC:'static';
STRING:'String';
VOID:'void';
MAIN:'main';
PARENTESIS_IZQ:'(';
PARENTESIS_DER:')';
INT:'int';
IGUAL:'=';
NUM: [0-9]+ ;
PUNTO_COMA:';';
LLAVE_DER:'}';
CORCHETE_IZQ:'[';
CORCHETE_DER:']';
MAS:'+';
PUNTO:'.';
COMILLAS:'"';
DOS_PUNTOS:':';
ASTER: '*';
WS: [ \t\r\n]+ -> skip ;