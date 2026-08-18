since all the environemt variable are removed. we can only use the `sh` built-in commnad to solve this puzzle


- the .c file checks one character `/` , `=` and `\`` , which  means we can use it inside the string. 
this will prevent us from using the path to the binary files, assign the environement variable.

- the shell concatenate the the quoted string and make it one string : 
for example : 
    `fla'g'` becomes `flag`

we can use this to pypass the check that is used inside the .c
so we can pass any string has more than 1 character in our solution. 

there also the `read` command that will read the input and put the result in a environment variable.

which means if we redirect the flag file to stdin of the read function we will assign the text inside the file to the env variable. 

