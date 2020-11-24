@ECHO OFF
python D:\python\github_autocreate_repo.py %1 %2
cd
cd /D "%2"
git init
git add README.md
git commit -m "Initial commit"
git remote add origin "https://github.com/your-username-here/%1"
git branch -M main
git push -u origin main
code .
pause