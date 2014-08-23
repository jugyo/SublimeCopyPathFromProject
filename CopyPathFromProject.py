import sublime, sublime_plugin

class CopyPathFromProjectCommand(sublime_plugin.TextCommand):
    def run(self, edit, lineNumber=False):
        path = self.view.file_name()
        for folder in self.view.window().folders():
            path = path.replace(folder + '/', '', 1)
        if lineNumber:
          (row, col) = self.view.rowcol(self.view.sel()[0].a)
          path = "%s:%s" % (path, row + 1)
        sublime.set_clipboard(path)
        sublime.status_message('copied: %s' % path)
