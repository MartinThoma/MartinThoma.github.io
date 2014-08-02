---
layout: post
title: Logging in Python
author: Martin Thoma
date: 2014-08-01 21:15
categories:
- Code
tags:
- Python
- Logging
featured_image: logos/python.png
---

Python has a nice logging module. You can use it like this:


## Stream output

```python
#!/usr/bin/env python

import logging
import sys

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
```

## File output

```python
#!/usr/bin/env python

import logging

logging.basicConfig(filename='logging.log',
                    format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
```

## See also

* [Tutorial](https://docs.python.org/2/howto/logging.html)
* [Documentation](https://docs.python.org/2/library/logging.html)