# silly-logger 🌸

A silly little Python logger that prints cute faces in your terminal and sends logs to a live dashboard.

## Install

```bash
uv add silly-logger
# or
pip install silly-logger
```

## Usage

```python
from silly_logger import Logger

log = Logger("my_script")

log.debug("loading stuff")      # :3  cyan
log.info("all good")            # :>  green
log.warn("hmm weird")           # :|  yellow
log.error("something broke")    # >:( red
log.critical("everything died") # X_X bold red
```

Optional `category` tag:
```python
log.info("user signed in", category="auth")
log.error("payment failed", category="billing")
```

Silent JSON — dashboard only, no terminal output:
```python
log.json({"user": "lain", "action": "login", "status": 200}, category="auth")
```

## Dashboard

Logs are sent to [lain-log-server.up.railway.app](https://lain-log-server.up.railway.app) in real time :D

## PyPI

[pypi.org/project/silly-logger](https://pypi.org/project/silly-logger/)
