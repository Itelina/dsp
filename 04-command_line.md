# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

pwd
print working directory
hostname
my computer's network name
mkdir
make directory
cd
change directory
ls
list directory
rmdir
remove directory
pushd
push directory
popd
pop directory
cp
copy a file or directory
mv
move a file or directory
less
page through a file
cat
print the whole file
xargs
execute arguments
find
find files. Syntax: Syntax: find STARTDIR -name WILDCARD -print
grep
find things inside files
man
read a manual page
apropos
find what man page is appropriate
env
look at your environment
echo
print some arguments
export
export/set a new environment variable
exit
exit the shell
sudo
DANGER! become super user root DANGER!
chmod
change permission modifiers
chown
change ownership

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

'ls' provides a list of directory contents.
'ls -a' include directory entrires whose names begin with a dot (.)
'ls -l' lists in the long format.
'ls-lh' uses unit suffixes; Bype, Kilobyte, Megabyte, Gigabyte, Terabyte and Petabyte in order to reduce the number of digits to three or less using base 2 for sizes. 

'ls -al' include directory entries whose names begin with a dot (.) and list them in long format.
'ls -alh' include directory entires whose names begin with a dot (.), lists them in long format, and represents the unit suffixes to represent size.

---


---

What does `xargs` do? Give an example of how to use it.

xargs: contruct argument list(s) and execute utility
Example usage: find /path -type f -print | xargs rm
---
