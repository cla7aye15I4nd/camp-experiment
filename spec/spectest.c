#include <stdio.h>
#include <sys/time.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/time.h>
#include <sys/resource.h>
#include <sys/wait.h>

struct rusage rusage;
struct timeval start, end;
pid_t pid;

static inline int run(const char *file, char *const *argv)
{
    pid_t pid = fork();
    if (pid == 0)
    {
        execvp(file, argv);
        exit(1);
    }
    else if (pid > 0)
    {
        int status;
        wait4(pid, &status, 0, &rusage);
        gettimeofday(&end,NULL);
        return status;
    }
    else
    {
        perror("fork");
        return 1;
    }
}


int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: exe_file args\n");
        printf("e.g: perlbench_s -I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1\n");
        return 1;
    }

    int time_used, cpu_time_used, memory_used, signum;

    gettimeofday(&start, NULL);  // 运行前计时

    printf("Running ");
    for (int i = 1; i < argc; ++i)
        printf("%s%c", argv[i], " \n"[i + 1 == argc]);

    int ret = run(argv[1], (char *const *)&argv[1]);
    ret = WEXITSTATUS(ret);

    time_used = (int) (end.tv_sec * 1000 + end.tv_usec / 1000 - start.tv_sec * 1000 -
                       start.tv_usec / 1000);
    cpu_time_used =
            rusage.ru_utime.tv_sec * 1000 + rusage.ru_utime.tv_usec / 1000 +
            rusage.ru_stime.tv_sec * 1000 + rusage.ru_stime.tv_usec / 1000;

    memory_used = rusage.ru_maxrss;

    printf("time used:     %6d ms\n", time_used);
    printf("cpu time used: %6d ms\n", cpu_time_used);
    printf("memory used:   %6d kb\n", memory_used);
    printf("exit code:     %6d\n", signum);
    return 0;
}