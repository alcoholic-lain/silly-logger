import logging
import requests
import threading

URL = "https://lain-log-server.up.railway.app/log"

# terminal colors
_R = "\033[0m"
_CYAN   = "\033[96m"
_GREEN  = "\033[92m"
_YELLOW = "\033[93m"
_RED    = "\033[91m"
_BOLD   = "\033[1m"

STYLES = {
    "DEBUG":    (_CYAN,        ":3"),
    "INFO":     (_GREEN,       ":>"),
    "WARN":     (_YELLOW,      ":|"),
    "WARNING":  (_YELLOW,      ":|"),
    "ERROR":    (_RED,         ">:("),
    "CRIT":     (_BOLD + _RED, "X_X"),
    "CRITICAL": (_BOLD + _RED, "X_X"),
}


class _Formatter(logging.Formatter):
    def format(self, record):
        level = record.levelname
        color, emoji = STYLES.get(level, ("", level))
        record.msg = f"{color}{emoji} {record.msg}{_R}"
        return super().format(record)


class Logger:
    def __init__(self, source: str):
        self.source = source
        self._log = logging.getLogger(source)
        self._log.setLevel(logging.DEBUG)
        if not self._log.handlers:
            h = logging.StreamHandler()
            h.setFormatter(_Formatter("%(message)s"))
            self._log.addHandler(h)

    def _send(self, level, message, category=None):
        data = {"level": level, "message": message, "source": self.source, "category": category}
        threading.Thread(target=requests.post, args=(URL,), kwargs={"json": data, "timeout": 5}).start()

    def debug(self, msg, category=None):    self._log.debug(msg);    self._send("DEBUG", msg, category)
    def info(self, msg, category=None):     self._log.info(msg);     self._send("INFO",  msg, category)
    def warn(self, msg, category=None):     self._log.warning(msg);  self._send("WARN",  msg, category)
    def error(self, msg, category=None):    self._log.error(msg);    self._send("ERROR", msg, category)
    def critical(self, msg, category=None): self._log.critical(msg); self._send("CRIT",  msg, category)
