#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pynagios import Plugin, make_option, Response, WARNING, CRITICAL, UNKNOWN, OK

import subprocess
import os

# Is apparmor enabled ?
class StatusCheck(Plugin):
	status_result = 0
	status_command = [ '/usr/sbin/aa-status', '--enabled' ]

	def doApiGet(self):
		if os.getuid() != 0:
			status_command.insert(0, 'sudo')

		self.status_result = subprocess.call(status_command)

	def check(self):
		try:

			self.doApiGet()
			return self.parseResult()

		except Exception as e:
			return Response(UNKNOWN, "Error occurred: " + str(e))

	def parseResult(self, data=None):
		return self.response_for_value(self.status_result)

# Is the given process enforced ?
class EnforcedCheck(Plugin):
	process_found = False
	process = make_option("--process", dest="process", help="The name of the process to find", type="string")

	def doApiGet(self):
		ps_command = [ 'ps', '-eo', 'cmd,label' ]
		rs = subprocess.check_output(ps_command)

		for line in rs.split('\n'):
			if self.options.process in line and 'enforce' in line:
				self.process_found = True
				break

	def check(self):
		if not self.options.process:
			return Response(UNKNOWN, "Process option not given")

		try:
			self.doApiGet()
			return self.parseResult()

		except Exception as e:
			return Response(UNKNOWN, "Error occurred: " + str(e))

	def parseResult(self, data=None):
		if self.process_found == True:
			return Response(OK, "Process %s found in enforced mode" % self.options.process)

		return Response(CRITICAL, "Process not %s found in enforced mode" % self.options.process)
