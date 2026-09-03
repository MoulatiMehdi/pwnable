#include <fcntl.h>
# include <unistd.h>

int main(int argc, char *argv[])
{

    char buf [1024];
    int fd = open("this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong", O_RDONLY);
    int bytes = read(fd,buf,1024);
    write(1,buf,bytes);
    return 0;
}
