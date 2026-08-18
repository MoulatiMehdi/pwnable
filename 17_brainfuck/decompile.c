
typedef struct struct_0
{
    char field_0;
} struct_0;

extern struct_0 *p;

void do_brainfuck(char a0)
{
    char v0; // al

    switch (a0)
    {
        case 43:
            p->field_0 = p->field_0 + 1;
            break;
        case 44:
            v0         = getchar();
            p->field_0 = v0;
            break;
        case 45:
            p->field_0 = p->field_0 - 1;
            break;
        case 46:
            putchar(p->field_0);
            break;
        case 60:
            p = (char *)p - 1;
            break;
        case 62:
            p = p + 1;
            break;
        case 91:
            puts("[ and ] not supported.");
            break;
    }
    return;
}

typedef struct FILE
{
} FILE;

extern FILE        *stdin;
extern FILE        *stdout;
extern unsigned int p;
extern char         tape;

unsigned int main(unsigned int a0, unsigned int a1)
{
    unsigned long      v4;       // ldt
    unsigned long      v5;       // gdt
    unsigned short     v6;       // gs
    unsigned long long v7;       // 4136
    unsigned long long v8;       // 4122
    unsigned int       v0;       // [bp-0x41c]
    unsigned int       i;        // [bp-0x410]
    char               v2[1024]; // [bp-0x40c]
    unsigned int       v3;       // [bp-0xc]

    v0 = a1;
    v7 = _ccall(v4, v5, (unsigned int)v6, 20);
    v3 = *((int *)(unsigned int)v7);
    setvbuf(stdout, NULL, 2, 0);
    setvbuf(stdin, NULL, 1, 0);
    p = &tape;
    puts("welcome to brainfuck testing system!!");
    puts("type some brainfuck instructions except [ ]");
    memset(v2, 0, 0x400);
    fgets(v2, 0x400, stdin);
    for (i = 0; i < strlen(v2); i += 1)
    {
        do_brainfuck(v2[i]);
    }
    v8 = _ccall(v4, v5, (unsigned int)v6, 20);
    if (!(v3 ^ *((int *)(unsigned int)v8)))
        return 0;
    __stack_chk_fail(); /* do not return */
}
