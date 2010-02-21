@echo off
ECHO ----------------------------------------
echo Creating LRC Lyrics Build Folder
rmdir BUILD /S /Q
md BUILD

Echo .svn>exclude.txt
Echo Thumbs.db>>exclude.txt
Echo Desktop.ini>>exclude.txt
Echo dsstdfx.bin>>exclude.txt
Echo exclude.txt>>exclude.txt

ECHO ----------------------------------------
ECHO Building LRC Lyrics Directory...
xcopy "resources" "BUILD\LRC Lyrics\resources" /E /Q /I /Y /EXCLUDE:exclude.txt

del exclude.txt

copy *.py "BUILD\LRC Lyrics\"
copy *.tbn "BUILD\LRC Lyrics\"