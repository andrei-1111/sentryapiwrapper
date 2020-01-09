
The sentry resources available on this package are mostly for reading data only but it can be added later if needed.


## Example Usage

```
"""
Script to export specific issue events to a csv file using pandas.
"""

import pandas as pd
from sentryapiwrapper.events import (
    list_issue_events,
)

issue_id = 1234
issue_events = list_issue_events(issue_id)

df_obj = pd.DataFrame(issue_events)
df_obj.to_csv('/file/location/export.csv', index=None)
```
