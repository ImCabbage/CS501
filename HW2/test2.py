#!/usr/bin/env python  # test2.py
import os, subprocess
from io import StringIO
os.mkdir('life')
os.chdir('life')
os.mkdir('Eukarya')
os.mkdir('Bacteria')
open('methanobacteria~', 'w').close()
open('halobacteria', 'w').close()
open('halobacteria~', 'w').close()
os.chdir('Bacteria')
open('cyanobacteria~', 'w').close()
open('spirochetes~', 'w').close()
os.chdir(os.pardir+os.sep+'Eukarya')
os.mkdir('Animals')
os.chdir('Animals')
open('pigs', 'w').close()
open('pigs~', 'w').close()
open('men', 'w').close()
open('men~', 'w').close()
os.chdir(os.pardir+os.sep+os.pardir+os.sep+os.pardir)
output = StringIO()
for label in ['Before:', 'After:']:
    print('',file=output); print(label,file=output)
    print(os.listdir('life'),file=output)
    print(os.listdir('life'+os.sep+'Bacteria'),file=output)
    print(os.listdir('life'+os.sep+'Eukarya'),file=output)
    print(os.listdir('life'+os.sep+'Eukarya'+os.sep+'Animals'),file=output)
    subprocess.call('./clean.py')
import shutil
shutil.rmtree('life')


key = """
Before:
['Bacteria', 'Eukarya', 'halobacteria', 'halobacteria~', 'methanobacteria~']
['cyanobacteria~', 'spirochetes~']
['Animals']
['men', 'men~', 'pigs', 'pigs~']

After:
['Bacteria', 'Eukarya', 'halobacteria', 'methanobacteria~']
['cyanobacteria~', 'spirochetes~']
['Animals']
['men', 'pigs']
"""

print('The desired output is:')
print(key)
print('Your output is:')
print(output.getvalue())
if key==output.getvalue():
    print('test2 is passed!')
else:
    print('test2 is failed!')
