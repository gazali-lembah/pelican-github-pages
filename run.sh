# cd output
# git init
# # git remote add origin https://github.com/gazali-lembah/gazali-lembah.github.io.git
# git add --all
# git commit -m "inital commit"
# git push origin main

# cd ..
# git add .
# git commit -m "First commit."
# git push -u origin master

#!/bin/bash
lastcommit=`git log origin/main -1 --oneline`
make publish
cd output && git add -A && git commit -m "$lastcommit" && git push origin main
exit 0