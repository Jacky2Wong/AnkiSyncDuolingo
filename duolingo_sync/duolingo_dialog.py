from aqt.qt import *


def duolingo_dialog(mw):
    d = QDialog(mw)
    d.setWindowTitle("Pull from Duolingo")
    d.setWindowModality(Qt.WindowModal)
    vbox = QVBoxLayout()
    l = QLabel("""
    <p>This plugin will make Anki notes and cards from the words you've learned in 
    your <strong>active</strong> Duolingo language. As you learn more words in Duolingo, use
    this tool again to pull those words into Anki.</p>
    
    <p>See the <a href="https://github.com/JASchilz/AnkiSyncDuolingo/">project page</a>
    for more information.</p>

    <p>Please enter your <strong>Duolingo</strong> username and password.</p>
    """)
    l.setOpenExternalLinks(True)
    l.setWordWrap(True)
    vbox.addWidget(l)
    vbox.addSpacing(20)
    g = QGridLayout()
    l1 = QLabel(_("Duolingo Username:"))
    g.addWidget(l1, 0, 0)
    user = QLineEdit()
    g.addWidget(user, 0, 1)
    l2 = QLabel(_("Duolingo Password:"))
    g.addWidget(l2, 1, 0)
    passwd = QLineEdit()
    passwd.setEchoMode(QLineEdit.Password)
    g.addWidget(passwd, 1, 1)
    vbox.addLayout(g)
    bb = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    bb.button(QDialogButtonBox.Ok).setAutoDefault(True)
    bb.accepted.connect(d.accept)
    bb.rejected.connect(d.reject)
    vbox.addWidget(bb)
    d.setLayout(vbox)
    d.show()
    accepted = d.exec_()
    u = user.text()
    p = passwd.text()
    if not accepted or not u or not p:
        return
    return (u, p)
