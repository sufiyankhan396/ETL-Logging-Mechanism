
---

## Logging Examples

### 1. Simple Console Logging

**File:** `logging_examples/simple_logging.py`

```python
import logging

# Basic configuration for logging to console
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Log messages with different severity levels
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
