# Git menual

##  Frequently used Git commands

1. commit
2. push
3. pull
4. clone
5. checkout
6. add
7. branch
8. log
9. diff
10. fetch
11. merge
12. init
13. status
14. reset
15. tag
16. rebase
17. rm
18. show
19. bisect
20. grep
21. mv
22. ​

## 1. solve command



### A. have problem about crlf



-> git config --global core.autocrlf true



### B. have problem about ssl certificate



-> git config --global http.sslverify false



### C. Delete File on Git Web



-> git rm -r --cached Filename

-> git commit -m " "

-> git push origin master



## 2. Branch and Merge command



### A. Make branch & checkout function



-> git checkout -b name

it means (git branch name + git checkout name)



### B. delete branch



-> git branch -d name



## 3. Check Version and Return command



### A. print log

-> git log



### B. Version-specific differences in logs

-> git log -p



### C. compare before Add to after Add

-> git diff



### D. Version-specific differentces in context

-> git diff 'version id1'..'version id2'



### E. Return previous version

-> git reset --hard "version id"



### F. Commit canceled and made into a new version

->git revert "version id"