@echo off

call python -m art text "Doc 2 HTML"
call python setup.py install
if not exist "doc_html" mkdir doc_html
for %%f in (doc_html\*) do (del %%f)
copy *.ipynb doc_html
cd doc_html
echo --------------------------
for %%f in (*.ipynb) do (
echo %%f is running!
call python -m nbconvert --to html --execute %%f --no-prompt --log-level=ERROR
if ERRORLEVEL 1 (echo %%f Failed! & cd .. & exit /b 0) else (echo %%f Done!)
echo --------------------------
del %%f
)
cd ..
call python otherfile\version_check.py
