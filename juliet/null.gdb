run

if ((unsigned long long)data) == 0
    print "UAF detected"
end
if ((unsigned long long)twoIntsStructPointer) == 0
    print "UAF detected"
end

quit
# gdb --batch --command uaf.gdb --args dataset/testcases/CWE476_NULL_Pointer_Dereference/CWE476_NULL_Pointer_Dereference__struct_33.badout