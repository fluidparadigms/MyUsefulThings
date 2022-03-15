builddir:=foo
slink:=pythonRunner

all: run
#all: build

run: $(slink)
	./$(slink)
	@echo ''

test: $(builddir)/build.ninja
	meson test -C $(builddir)

build: $(builddir)/build.ninja
	ninja -C $(builddir)
	@echo ''
	@echo ''

$(builddir)/build.ninja:
	meson $(builddir)

$(builddir)/pythonRunner: build

$(slink): $(builddir)/pythonRunner
	ln -s $< $@

clean:
	 rm -fr $(builddir) $(slink)

.PHONY: all build clean run

.SUFFIXES:

