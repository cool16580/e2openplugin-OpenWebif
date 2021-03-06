#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import localtime, strftime
from urllib import quote
from Plugins.Extensions.OpenWebif.controllers.i18n import tstrings


class renderEvtBlock:
	def __init__(self):
		self.template = """
		<div class="event" data-ref="%s" data-id="%s" data-toggle="modal" data-target="#EventModal" onClick="loadeventepg('%s', '%s');return false;">
			<div style="width:40px; float:left; padding: 0 3px">%s%s</div>
			<div style="width:144px; float:left">
				<div class="title">%s</div>%s
			</div>
			<div style="clear:left"></div>
		</div>
		"""

	def render(self, event):
		if event['title'] != event['shortdesc']:
			shortdesc = '<div class="desc">%s</div>' % (event['shortdesc'])
		else:
			shortdesc = ''

		if event['timerStatus'] != '':
			timerEventSymbol = '<div class="%s">%s</div>' % (event['timerStatus'], tstrings['timer'])
		else:
			timerEventSymbol = ''
		return self.template % (
			quote(event['ref'], safe=' ~@#$&()*!+=:;,.?/\''),
			event['id'],
			event['id'],
			quote(event['ref'], safe=' ~@#$&()*!+=:;,.?/\''),
			strftime("%H:%M", localtime(event['begin_timestamp'])),
			timerEventSymbol,
			event['title'],
			shortdesc
		)
