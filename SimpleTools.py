import sublime, sublime_plugin
import webbrowser, re

class DuplicateLineUpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.regions = []

		for region in self.view.sel():
			self.regions.append(sublime.Region(region.begin(), region.end()))
			if region.empty():
				line = self.view.line(region)
				self.view.insert(edit, line.begin(), self.view.substr(line) + '\n')
			else:
				self.view.insert(edit, region.begin(), self.view.substr(region))
		
		self.view.sel().clear()
		for region in self.regions:
			self.view.sel().add(region)

class BreakIntoLinesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for selection in reversed(self.view.sel()):
			current_line_region = self.view.line(selection)
			current_line = self.view.substr(current_line_region)
			
			replacement = current_line.replace('; ', ';\n').replace('	', '\n') #.replace(',',',\n')
			self.view.replace(edit, current_line_region, replacement)

class ScopeToClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		scope = self.view.scope_name(self.view.sel()[0].begin()).strip()
		sublime.set_clipboard(scope);
		sublime.status_message('Scope: ' + scope)
		print (scope)

class NewFileWithCurrentSyntaxTypeCommand(sublime_plugin.WindowCommand):
	def run(self):
		syntax = self.window.active_view().settings().get('syntax')
		newFile = self.window.new_file()
		newFile.set_syntax_file(syntax)
		#sublime.error_message("%s" % syntax)

"""
class GetHelpCommand(sublime_plugin.TextCommand):
	def run(self, view):
		keyword = self.view.substr(self.view.word(self.view.sel()[0].begin()))
		scope = self.view.syntax_name(self.view.sel()[0].begin()).strip()

		scope = self.view.syntax_name(self.view.sel()[0].begin())
		for match in re.finditer(r"(?sim)(source\.cfscript\.cfc)|(meta\.tag\.block\.cf)|text\.html\.cfm|(text\.html)", scope):
			if match.group(0) == 'source.cfscript.cfc':
				# sublime.status_message('CFML help: ' + keyword + ' [' + scope + ']')
				print ('CFML script help: ' + keyword + ' [' + scope + ']')
				#webbrowser.open_new_tab('http://www.cfquickdocs.com/cf7/?getDoc=' + keyword)
				webbrowser.open_new_tab('https://learn.adobe.com/wiki/display/coldfusionen/' + keyword)
				break
			elif match.group(0) == 'text.html.cfm':
				# sublime.status_message('CFML help: ' + keyword + ' [' + scope + ']')
				print ('CFML help: ' + keyword + ' [' + scope + ']')
				#webbrowser.open_new_tab('http://www.cfquickdocs.com/cf7/?getDoc=' + keyword)
				webbrowser.open_new_tab('https://learn.adobe.com/wiki/display/coldfusionen/' + keyword)
				break
			elif match.group(0) == 'text.html':
				print ('HTML Help: ' + keyword + ' [' + scope + '] ' + match.group(0))
				break
			elif match.group(0) == 'source.cfm':
				#webbrowser.open_new_tab('http://www.cfquickdocs.com/cf7/?getDoc=' + keyword)
				#webbrowser.open_new_tab('http://cfdocs.org/' + keyword)
				sublime.status_message('get cfm help: ' + keyword + '[' + scope + ']')
				break
			elif match.group(0) == 'text.html':
				#webbrowser.open_new_tab('http://reference.sitepoint.com/html/' + keyword)
				sublime.status_message('get html help: ' + keyword + '[' + scope + ']')
				break
			elif match.group(0) == 'source.js':
				#webbrowser.open_new_tab('http://reference.sitepoint.com/javascript/' + keyword)
				sublime.status_message('get js help: ' + keyword)
				break
			elif match.group(0) == 'source.css':
				#webbrowser.open_new_tab('http://reference.sitepoint.com/css/' + keyword)
				sublime.status_message('get css help: ' + keyword)
				break
			elif match.group(0) != '':
				print 'no match: ' + match.group(0)
				break
"""


"""
class OpenFileUnderCursorCommand(sublimeplugin.WindowCommand):
  def run(self, window, args):
	curdir = os.getcwdu()
	view = window.activeView()
	for region in view.sel():
	  s = view.substr(region)
	  if(s != ''):
		f = curdir + '\\' + s

		if(os.path.exists(f)):
		  window.openFile(f)
		else:
		  sublime.errorMessage('The file under cursor does not exists in the directory of the current file')
	  else:
		# f = curdir + '\\' + str(args[1])
		word_under_cursor = view.substr(view.word(view.sel()[0].begin()))
		dot_pos = view.find('\.',view.sel()[0].begin())
		if(dot_pos):
		  f = view.substr(view.word(dot_pos))

	  if(os.path.exists(f)):
		window.openFile(f)
	  else:
		sublime.errorMessage('The file under cursor does not exists in the directory of the current file')
"""