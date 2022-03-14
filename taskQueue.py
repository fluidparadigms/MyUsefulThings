#!/usr/bin/env python3

import cmd
import subprocess

class cmd_line(cmd.Cmd):
	intro = 'Type help or ? to list commands.\n'
	prompt = '> '
	file = None
	taskList=[]

	def do_exit(self, arg):
		'quit the program'
		return True
	def do_add(self, arg):
		'add a job to the queue'


if __name__ == '__main__':
	cmd_line().cmdloop()

