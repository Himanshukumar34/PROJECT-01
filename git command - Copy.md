###### git command



command for git

 1. cd--------------- command for change directory

2\. pwd--------- present working directory(folder)

3\. git config --list ---------------for check name of the folder and email id

4\. git add . ------means adding file in staging area means git track the files now

5\. git commit -m"hy " ---------means save changes premanently 

6\.git log -----------means commit history

7\. git add index.html ------adding a separate file not all files

9\. ls------ means kitni file or folder hai us folder me

10\. git clone---- a repositires

11\. touch ----- for create a file

12\. git mv file.txt fil2.txt  ------ change name of a file 

13\. git rm --cached file.txt --- means untracked the file

14\. git remote --- for check name os repositories

15\. git remote -v ------ for checking push and pull link 

16\. git restore file.py ------ means restore all the change / means undo all the changes

17\. git checkout-b branch_name  ------means making  a new branch 

18\. git checkout file ----- means open file name branch 

19\. git branch ---- means show me all branches of git 

20\. git log --all --graph ---- this command use for see all the commit on branches 

21\. git merge filename  ----- means merge a branch into main cofirm that you will open second branch

22\. git diff --- use when you modifeid a file and before commit and add you run this command for see what you change in your files

23\. git branch -v ---- means show last commit all the branhes with name 

24\. git branch --merged ------ means show all the braches which is already merged 

25\. git branch --no-merged ------means show those files which is not merged in main 

26\. git branch -d file_name ------- delete the branch which is merged already in main otherwise is not merged it is give error

27\. git push -u (link name ) ---------git push the code on any server 






GIT DANGEOUR COMMANDS 

git reset --hard
git push --force
git clean -fd
git rm 
git rebase



===================================================================================================================================================
**** NOTES OF GIT ****


<!-- first question -->

Q.1 what is git ?

Ans= git is a version control system
* easily recover files after delete
* roll back to previous state
A Version Control System is a tool that tracks and manages changes in files so
 developers can maintain different versions of a project.

<!--  second question  -->

Q.2 Why Version Control System is Used?

Ans=1️⃣ Track changes in code
2️⃣ Restore old versions
3️⃣ Work with a team
4️⃣ Avoid losing code
5️⃣ Manage project history

A Centralized Version Control System (CVCS) is a type of version control system where all
project files and history are stored in one central server.
Developers connect to that server to get and update files.



<!-- third question -->

Q.3 write three stages of git ?

Ans= Three stages of git
1. working directory
2. staging area
3. repository


<!-- foruth question -->

Q.4 what is git init ?

Ans =intailize a folder  a repositories ki uske pass ap ek track karne ke lie ek git tracking system hai


<!-- fifth question -->



Q.5 git cylcle?

Ans untracked --- tracked --- modified --- staged
1, add file --- means git track your file now this changes to untracked file to tracked file and all thing are ok
2. modifeid --- means now you change in the file in tracked file now you add the file and then commit and the file are back to there previuos stats means tracked stage


<!-- sixth question -->

Q.6 notes ka point
Ans 1. U -- means untracked
2. A -- now add but not  commited
3. blank means commited




<!-- eighth question -->


Q.8 what is git conflict ?
Ans = IT occurs when teo branches are merge and when merge conflict happens when Git tries to combine two versions of the same file... but the changes are on the same lines and they don't match.Git gets confused and says:
"I don't know which change is correct — you decide!"It's like two friends editing the same sentence in a story at the same time:Friend A changes: "The cat is black" → "The cat is white"  
Friend B changes: "The cat is black" → "The cat is sleeping"


<!-- ninth question -->

Q.9 What is git branches ?
Ans = A branch is like a separate copy of your project where you can play safely.
Main branch = the "official" version everyone sees  
New branch = your private playground
You can change anything in your playground. Nothing breaks the main version until you decide to mix your changes back in.





