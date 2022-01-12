import eel
import wx
import jinja2 as jinja2

eel.init("web")

# Start the index.html file
eel.start(
    'templates/index.html',
    jinja_templates='templates'
)

@eel.expose
def pythonFunction(wildcard="*"):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path