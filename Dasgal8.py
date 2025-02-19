''' Admin@DESKTOP-P8RVAUA MINGW64 ~
$ mk dir
bash: mk: command not found

Admin@DESKTOP-P8RVAUA MINGW64 ~
$ dir
3D\ Objects
AppData
Application\ Data
Cisco\ Packet\ Tracer\ 8.2.1
Contacts
Cookies
Desktop
Documents
Downloads
Favorites
IntelGraphicsProfiles
Links
Local\ Settings
Music
My\ Documents
NTUSER.DAT
NTUSER.DAT{95f0a7ae-2c6c-11ed-94e9-7412b3e07656}.TM.blf
NTUSER.DAT{95f0a7ae-2c6c-11ed-94e9-7412b3e07656}.TMContainer00000000000000000001.regtrans-ms
NTUSER.DAT{95f0a7ae-2c6c-11ed-94e9-7412b3e07656}.TMContainer00000000000000000002.regtrans-ms
NetHood
Pictures
PrintHood
Recent
Saved\ Games
Searches
SendTo
Start\ Menu
Templates
Videos
VirtualBox\ VMs
WireframeSketcher
eclipse
eclipse-workspace
ntuser.dat.LOG1
ntuser.dat.LOG2
ntuser.ini
source

Admin@DESKTOP-P8RVAUA MINGW64 ~
$ cd Lab5
bash: cd: Lab5: No such file or directory

Admin@DESKTOP-P8RVAUA MINGW64 ~
$ mk dir Lab5
bash: mk: command not found

Admin@DESKTOP-P8RVAUA MINGW64 ~
$ cd Lab5
bash: cd: Lab5: No such file or directory

Admin@DESKTOP-P8RVAUA MINGW64 ~
$ touch Lab5

Admin@DESKTOP-P8RVAUA MINGW64 ~
$ cd Lab5
bash: cd: Lab5: Not a directory

Admin@DESKTOP-P8RVAUA MINGW64 ~
$ git init
Initialized empty Git repository in C:/Users/Admin/.git/

Admin@DESKTOP-P8RVAUA MINGW64 ~ (master)
$ mkdir Lab5
mkdir: cannot create directory ‘Lab5’: File exists

Admin@DESKTOP-P8RVAUA MINGW64 ~ (master)
$ mkdir Lab5

Admin@DESKTOP-P8RVAUA MINGW64 ~ (master)
$ cd Lab5

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ touch readme.txt

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "chigga"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'Admin@DESKTOP-P8RVAUA.(none)')

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git init
Initialized empty Git repository in C:/Users/Admin/Lab5/.git/

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git push origin master
error: src refspec master does not match any
error: failed to push some refs to 'origin'

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m ""chigga
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'Admin@DESKTOP-P8RVAUA.(none)')

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git config --global user.email "Cbuyantkhuu@gmail.com"

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git config --global user.name "BuyantkhuuB232270104"

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git push origin master
error: src refspec master does not match any
error: failed to push some refs to 'origin'

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        readme.txt

nothing added to commit but untracked files present (use "git add" to track)

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git add .

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "chigga"
[master (root-commit) 9efbed0] chigga
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 readme.txt

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git push origin master
fatal: 'origin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git branch Buynt

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git checkout Buynt
Switched to branch 'Buynt'

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (Buynt)
$ git add .

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (Buynt)
$ git add Dasgal1.py

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (Buynt)
$ git commit -m "gulpgulp"
[Buynt 53aa709] gulpgulp
 7 files changed, 31 insertions(+)
 create mode 100644 Dasgal1.py
 create mode 100644 Dasgal2.py
 create mode 100644 Dasgal3.py
 create mode 100644 Dasgal4.py
 create mode 100644 Dasgal5.py
 create mode 100644 Dasgal6.py
 create mode 100644 Dasgal7.py

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (Buynt)
$ git add Dasgal2.py

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (Buynt)
$ git commit -m "CHiigg"
On branch Buynt
nothing to commit, working tree clean

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (Buynt)
$ git checkout master
Switched to branch 'master'

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git add .

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git add Dasgal3.py
fatal: pathspec 'Dasgal3.py' did not match any files

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git merge Buynt
Updating 9efbed0..53aa709
Fast-forward
 Dasgal1.py |  2 ++
 Dasgal2.py |  3 +++
 Dasgal3.py |  2 ++
 Dasgal4.py |  5 +++++
 Dasgal5.py |  3 +++
 Dasgal6.py |  5 +++++
 Dasgal7.py | 11 +++++++++++
 7 files changed, 31 insertions(+)
 create mode 100644 Dasgal1.py
 create mode 100644 Dasgal2.py
 create mode 100644 Dasgal3.py
 create mode 100644 Dasgal4.py
 create mode 100644 Dasgal5.py
 create mode 100644 Dasgal6.py
 create mode 100644 Dasgal7.py

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ ^[[200~https://github.com/BuyantkhuuB232270104/Lab5.git
bash: https://github.com/BuyantkhuuB232270104/Lab5.git: No such file or directory

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ https://github.com/BuyantkhuuB232270104/Lab5.git
bash: https://github.com/BuyantkhuuB232270104/Lab5.git: No such file or directory

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git push origin
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.


Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git push --set-upstream origin master
fatal: 'origin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ https://github.com/BuyantkhuuB232270104/Lab5.git
bash: https://github.com/BuyantkhuuB232270104/Lab5.git: No such file or directory

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git add Dasgal3.py

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "OO"
On branch master
nothing to commit, working tree clean

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git add Dasgal4
fatal: pathspec 'Dasgal4' did not match any files

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$
Display all 5078 possibilities? (y or n)

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git add Dasgal4.py

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean
Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean
Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean
Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean
Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean
Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean
Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean
Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean
Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git commit -m "UU"
On branch master
nothing to commit, working tree clean
Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ ^[[200~https://github.com/BuyantkhuuB232270104/Lab5.git
bash: https://github.com/BuyantkhuuB232270104/Lab5.git: No such file or directory

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ https://github.com/BuyantkhuuB232270104/Lab5.git
bash: https://github.com/BuyantkhuuB232270104/Lab5.git: No such file or directory

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git remote add origin https://github.com/BuyantkhuuB232270104/Lab5.git

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git push origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/BuyantkhuuB232270104/Lab5.git'

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git remote add origin https://github.com/BuyantkhuuB232270104/Lab5.git
error: remote origin already exists.

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
$ git push --set-upstream origin master
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 12 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (12/12), 1.09 KiB | 1.09 MiB/s, done.
Total 12 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/BuyantkhuuB232270104/Lab5.git
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.

Admin@DESKTOP-P8RVAUA MINGW64 ~/Lab5 (master)
'''