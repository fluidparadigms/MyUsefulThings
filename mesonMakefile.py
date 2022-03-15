#!/usr/bin/env python3
from pathlib import Path

def makeMesonMakefile(makefileFile=Path('Makefile')):
	if makefileFile.exists():
		print('Makefile exists! Overwrite? y/[n] ',end='')
		resp=input()
		if resp.strip().lower() != 'y':
			print('Not overwriting',makefileFile,'Exiting...')
			return
	dirname=Path().absolute().name
	with open(makefileFile,'w') as f:
		f.write('builddir:=foo\n')
		f.write('slink:='+dirname+'\n')
		f.write('\n')
		f.write('all: run\n')
		f.write('#all: build\n')
		f.write('\n')
		f.write('run: $(slink)\n')
		f.write('\t./$(slink)\n')
		f.write("\t@echo ''\n")
		f.write('\n')
		f.write('test: $(builddir)/build.ninja\n')
		f.write('\tmeson test -C $(builddir)\n')
		f.write('\n')
		f.write('build: $(builddir)/build.ninja\n')
		f.write('\tninja -C $(builddir)\n')
		f.write("\t@echo ''\n")
		f.write("\t@echo ''\n")
		f.write('\n')
		f.write('$(builddir)/build.ninja:\n')
		f.write('\tmeson $(builddir)\n')
		f.write('\n')
		f.write('$(builddir)/'+dirname+': build\n')
		f.write('\n')
		f.write('$(slink): $(builddir)/'+dirname+'\n')
		f.write('\tln -s $< $@\n')
		f.write('\n')
		f.write('clean:\n')
		f.write('\t rm -fr $(builddir) $(slink)\n')
		f.write('\n')
		f.write('.PHONY: all build clean run\n')
		f.write('\n')
		f.write('.SUFFIXES:\n')
		f.write('\n')




if __name__ == '__main__':
	makeMesonMakefile()

