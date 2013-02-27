import sublime, sublime_plugin

class CopyPathFromProjectCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        path = self.view.file_name()
        for folder in self.view.window().folders():
            path = path.replace(folder + '/', '', 1)
        sublime.set_clipboard(path)
        sublime.status_message('copied: %s' % path)
