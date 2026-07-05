grammar Expr;

root: expr EOF ;    

expr: EOF;
NMAP:'nmap';
SUDO:'sudo';
TCPDUMP:'tcpdump';
SS:'ss';
CURL:'curl';
DIG:'dig';
JOURNALCTL:'journalctl';
GREP:'grep';
UFW:'ufw';
DENY:'deny';
FROM:'from';
MX:'MX';
TODAY:'today';
FLAG_LARGA:'--'[a-zA-Z]+;
FLAG_CORTA:'-'[a-zA-Z]+;
IP_CIDR:NUM_OCTETO'.'NUM_OCTETO'.'NUM_OCTETO'.'NUM_OCTETO'/'[0-9]+;
IP:NUM_OCTETO'.'NUM_OCTETO'.'NUM_OCTETO'.'NUM_OCTETO;
RUTA:'/' [a-zA-Z0-9_./]+;
DOMINIO:[a-zA-Z0-9]+ ('.'[a-zA-Z0-9]+)+;
CADENA:'"' ~["\r\n]* '"';
IDF: [a-zA-Z_][a-zA-Z0-9_]* ;
fragment NUM_OCTETO:[0-9]+;
NUM:[0-9]+;
WS:[ \t\r\n]+ -> skip;