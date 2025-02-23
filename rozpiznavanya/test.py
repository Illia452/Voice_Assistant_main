import sys, os, subprocess, inspect


pFileName = os.path.abspath(inspect.getfile(inspect.currentframe()))
pFileDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print ( 'pFileName = %s\n' % pFileName)
print ('pFileDir = %s' % pFileDir)
subprocess.Popen(r'explorer /select,%s' % pFileName)
if (pFileName.endswith(".png") or pFileName.endswith(".py") or pFileName.endswith(".txt")):
    # subprocess.call([r'C:\Program Files\Notepad++\notepad++.exe',  pFileName])
    subprocess.Popen([r'C:\Program Files\Notepad++\notepad++.exe',  pFileName])