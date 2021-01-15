%{
#include <stdio.h>
#include <stdlib.h>


#define YYDEBUG 1
%}

%token EQUAL
%token IDENTIFIER
%token CONSTANT
%token MAIN
%token IN
%token OUT
%token IF
%token FOR
%token BREAK
%token NUMBER
%token CHAR
%token BOOL
%token TRUE
%token FALSE
%token SEMICOLON
%token COMA
%token DOT
%token PLUS
%token MINUS
%token MULTIPLY
%token DIVISION
%token NOT
%token MOD
%token LEFT_ROUND_PARENTHESIS
%token RIGHT_ROUND_PARENTHESIS
%token LEFT_SQUARE_PARENTHESIS
%token RIGHT_SQUARE_PARENTHESIS
%token LEFT_CURLY_PARENTHESIS
%token RIGHT_CURLY_PARENTHESIS
%token SMALLER
%token SMALLER_OR_EQUAL
%token GREATER
%token GREATER_OR_EQUAL
%token DIFFERENT
%token OR
%token AND
%token ARE_EQUAL



%start program

%%


program : MAIN cmpstmt
cmpstmt : LEFT_CURLY_PARENTHESIS stmtlist RIGHT_CURLY_PARENTHESIS ;
stmtlist : stmt | stmt stmtlist;
stmt : decl SEMICOLON | assignment SEMICOLON | iostmt SEMICOLON | ifstmt | forstmt SEMICOLON | cmpstmt ;
decl : type IDENTIFIER ;
assignment : term EQUAL expression ;
for_assignment : type term EQUAL expression ;
iostmt : IN LEFT_ROUND_PARENTHESIS IDENTIFIER RIGHT_ROUND_PARENTHESIS | OUT LEFT_ROUND_PARENTHESIS CONSTANT RIGHT_ROUND_PARENTHESIS;
ifstmt : IF LEFT_ROUND_PARENTHESIS compCondition RIGHT_ROUND_PARENTHESIS cmpstmt ;
forstmt : FOR LEFT_ROUND_PARENTHESIS for_assignment SEMICOLON compCondition SEMICOLON assignment RIGHT_ROUND_PARENTHESIS cmpstmt ;
relation : SMALLER | GREATER | DIFFERENT | ARE_EQUAL | GREATER_OR_EQUAL | SMALLER_OR_EQUAL;
expression : term | term PLUS expression | term MINUS expression | term MULTIPLY expression | term DIVISION expression | term MOD expression ;
term : IDENTIFIER | CONSTANT | IDENTIFIER LEFT_SQUARE_PARENTHESIS term RIGHT_SQUARE_PARENTHESIS  ;
type : primitiveType | arrayDeclaration ;
primitiveType : NUMBER | BOOL ;
arrayDeclaration : primitiveType LEFT_SQUARE_PARENTHESIS CONSTANT RIGHT_SQUARE_PARENTHESIS  ;
compCondition : condition | condition AND condition | condition OR condition | NOT compCondition | compCondition AND compCondition
condition : expression relation expression ;


%%

yyerror(char *s)
{
    printf("%s\n",s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
    if(argc>1) yyin :  fopen(argv[1],"r");
    if(argc>2 && !strcmp(argv[2],"-d")) yydebug: 1;
    if(!yyparse()) fprintf(stderr, "\tO.K.\n");
}