# webserver.py
from arelle import CntlrWebMain

CntlrWebMain.main(
    ["--webserver", "--host", "0.0.0.0", "--port", "8080"]
)

