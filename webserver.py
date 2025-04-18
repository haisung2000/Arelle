# webserver.py
from arelle import Cntlr

Cntlr.Cntlr(logFileName='logToPrint', logFileMode='w', serverMode=True, host='0.0.0.0', port=8080)

