break printLine
    command 1
    set $flag = ($rdi >> 32) & 0xdeadbeef
    if $flag == 0xdeadbeef
        print "UAF detected"
    end
    continue
end

break printStructLine
    command 2
    set $flag = ($rdi >> 32) & 0xdeadbeef
    if $flag == 0xdeadbeef
        print "UAF detected"
    end
    continue
end

run
if (((unsigned long long)data >> 32) & 0xdeadbeef) == 0xdeadbeef
    print "UAF detected"
end

quit
# gdb --batch --command uaf.gdb --args dataset/testcases/CWE416_Use_After_Free/CWE416_Use_After_Free__new_delete_array_struct_12.badout