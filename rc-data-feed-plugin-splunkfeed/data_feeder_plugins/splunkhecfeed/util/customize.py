# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for rc-data-feed-plugin-splunkfeed"""

try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition


def codegen_reload_data():
    """
    Parameters required reload codegen for the rc-data-feed-plugin-splunkfeed package
    """
    return {
        "package": u"rc-data-feed-plugin-splunkfeed",
        "message_destinations": [u"feed_data"],
        "functions": [u"data_feeder_sync_incidents"],
        "workflows": [u"data_feeder_sync_incidents"],
        "actions": [u"Data Feeder: Sync Incidents", u"Data Feeder: Milestone", u"Data Feeder: Note", u"Data Feeder: Artifact", u"Data Feeder: Attachment", u"Data Feeder: Task", u"Data Feeder: Incident"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    Contents:
    - Message Destinations:
        - feed_data
    - Functions:
        - data_feeder_sync_incidents
    - Workflows:
        - data_feeder_sync_incidents
    - Rules:
        - Data Feeder: Sync Incidents
        - Data Feeder: Milestone
        - Data Feeder: Note
        - Data Feeder: Artifact
        - Data Feeder: Attachment
        - Data Feeder: Task
        - Data Feeder: Incident
    """

    yield ImportDefinition(u"""
eyJhY3Rpb25fb3JkZXIiOiBbXSwgImFjdGlvbnMiOiBbeyJhdXRvbWF0aW9ucyI6IFtdLCAiY29u
ZGl0aW9ucyI6IFtdLCAiZW5hYmxlZCI6IHRydWUsICJleHBvcnRfa2V5IjogIkRhdGEgRmVlZGVy
OiBBcnRpZmFjdCIsICJpZCI6IDE0LCAibG9naWNfdHlwZSI6ICJhbGwiLCAibWVzc2FnZV9kZXN0
aW5hdGlvbnMiOiBbImZlZWRfZGF0YSJdLCAibmFtZSI6ICJEYXRhIEZlZWRlcjogQXJ0aWZhY3Qi
LCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3QiLCAidGFncyI6IFtdLCAidGltZW91dF9zZWNvbmRz
IjogODY0MDAsICJ0eXBlIjogMCwgInV1aWQiOiAiM2M2MjdhYTgtNTgxMC00NGE0LWEyNWQtZTVh
OGRiMTliNmE2IiwgInZpZXdfaXRlbXMiOiBbXSwgIndvcmtmbG93cyI6IFtdfSwgeyJhdXRvbWF0
aW9ucyI6IFtdLCAiY29uZGl0aW9ucyI6IFtdLCAiZW5hYmxlZCI6IHRydWUsICJleHBvcnRfa2V5
IjogIkRhdGEgRmVlZGVyOiBBdHRhY2htZW50IiwgImlkIjogMTUsICJsb2dpY190eXBlIjogImFs
bCIsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFsiZmVlZF9kYXRhIl0sICJuYW1lIjogIkRhdGEg
RmVlZGVyOiBBdHRhY2htZW50IiwgIm9iamVjdF90eXBlIjogImF0dGFjaG1lbnQiLCAidGFncyI6
IFtdLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ0eXBlIjogMCwgInV1aWQiOiAiMmI2Mjhi
OGMtMWI1Mi00ZTUxLWE1ZjMtYzMyM2Q3ZmYwMzdlIiwgInZpZXdfaXRlbXMiOiBbXSwgIndvcmtm
bG93cyI6IFtdfSwgeyJhdXRvbWF0aW9ucyI6IFtdLCAiY29uZGl0aW9ucyI6IFtdLCAiZW5hYmxl
ZCI6IHRydWUsICJleHBvcnRfa2V5IjogIkRhdGEgRmVlZGVyOiBJbmNpZGVudCIsICJpZCI6IDE2
LCAibG9naWNfdHlwZSI6ICJhbGwiLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbImZlZWRfZGF0
YSJdLCAibmFtZSI6ICJEYXRhIEZlZWRlcjogSW5jaWRlbnQiLCAib2JqZWN0X3R5cGUiOiAiaW5j
aWRlbnQiLCAidGFncyI6IFtdLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ0eXBlIjogMCwg
InV1aWQiOiAiNWJjMGI5OWItOGY4Ny00OGRlLTk3ZDktOTMzM2YxMTM5ZDVkIiwgInZpZXdfaXRl
bXMiOiBbXSwgIndvcmtmbG93cyI6IFtdfSwgeyJhdXRvbWF0aW9ucyI6IFtdLCAiY29uZGl0aW9u
cyI6IFtdLCAiZW5hYmxlZCI6IHRydWUsICJleHBvcnRfa2V5IjogIkRhdGEgRmVlZGVyOiBNaWxl
c3RvbmUiLCAiaWQiOiAxNywgImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm1lc3NhZ2VfZGVzdGluYXRp
b25zIjogWyJmZWVkX2RhdGEiXSwgIm5hbWUiOiAiRGF0YSBGZWVkZXI6IE1pbGVzdG9uZSIsICJv
YmplY3RfdHlwZSI6ICJtaWxlc3RvbmUiLCAidGFncyI6IFtdLCAidGltZW91dF9zZWNvbmRzIjog
ODY0MDAsICJ0eXBlIjogMCwgInV1aWQiOiAiYzdmY2FmNTAtNDQwMi00YzYyLTk1NTItYzI2ZGY2
ZTViZTliIiwgInZpZXdfaXRlbXMiOiBbXSwgIndvcmtmbG93cyI6IFtdfSwgeyJhdXRvbWF0aW9u
cyI6IFtdLCAiY29uZGl0aW9ucyI6IFtdLCAiZW5hYmxlZCI6IHRydWUsICJleHBvcnRfa2V5Ijog
IkRhdGEgRmVlZGVyOiBOb3RlIiwgImlkIjogMTgsICJsb2dpY190eXBlIjogImFsbCIsICJtZXNz
YWdlX2Rlc3RpbmF0aW9ucyI6IFsiZmVlZF9kYXRhIl0sICJuYW1lIjogIkRhdGEgRmVlZGVyOiBO
b3RlIiwgIm9iamVjdF90eXBlIjogIm5vdGUiLCAidGFncyI6IFtdLCAidGltZW91dF9zZWNvbmRz
IjogODY0MDAsICJ0eXBlIjogMCwgInV1aWQiOiAiNzgwZjJlYmUtOWFhYy00MWU5LTk4YWItNzA2
ODhhYzlhZjdhIiwgInZpZXdfaXRlbXMiOiBbXSwgIndvcmtmbG93cyI6IFtdfSwgeyJhdXRvbWF0
aW9ucyI6IFtdLCAiY29uZGl0aW9ucyI6IFtdLCAiZW5hYmxlZCI6IHRydWUsICJleHBvcnRfa2V5
IjogIkRhdGEgRmVlZGVyOiBTeW5jIEluY2lkZW50cyIsICJpZCI6IDE5LCAibG9naWNfdHlwZSI6
ICJhbGwiLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbXSwgIm5hbWUiOiAiRGF0YSBGZWVkZXI6
IFN5bmMgSW5jaWRlbnRzIiwgIm9iamVjdF90eXBlIjogImluY2lkZW50IiwgInRhZ3MiOiBbXSwg
InRpbWVvdXRfc2Vjb25kcyI6IDg2NDAwLCAidHlwZSI6IDEsICJ1dWlkIjogIjE3NGFiYzE4LWRj
NzItNDEzMC1hNWM4LTY0MjFmYjQ0OWYxMiIsICJ2aWV3X2l0ZW1zIjogW3siY29udGVudCI6ICJj
YzUzMmEyMi1lOTBmLTQ2ZTQtOTE5YS0wYWQxMjk2Nzk2YmYiLCAiZWxlbWVudCI6ICJmaWVsZF91
dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwg
InNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50
IjogIjNlMmU5M2RlLTZiYTUtNGFkZi1iMDQ0LTY2YTQ2MDlkZDc3ZCIsICJlbGVtZW50IjogImZp
ZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBu
dWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNv
bnRlbnQiOiAiN2VkM2FmMDMtZDNiMy00MWVkLWE3MjEtOTcwNTQzNDYzNTk4IiwgImVsZW1lbnQi
OiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19p
ZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH1d
LCAid29ya2Zsb3dzIjogWyJkYXRhX2ZlZWRlcl9zeW5jX2luY2lkZW50cyJdfSwgeyJhdXRvbWF0
aW9ucyI6IFtdLCAiY29uZGl0aW9ucyI6IFtdLCAiZW5hYmxlZCI6IHRydWUsICJleHBvcnRfa2V5
IjogIkRhdGEgRmVlZGVyOiBUYXNrIiwgImlkIjogMjAsICJsb2dpY190eXBlIjogImFsbCIsICJt
ZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFsiZmVlZF9kYXRhIl0sICJuYW1lIjogIkRhdGEgRmVlZGVy
OiBUYXNrIiwgIm9iamVjdF90eXBlIjogInRhc2siLCAidGFncyI6IFtdLCAidGltZW91dF9zZWNv
bmRzIjogODY0MDAsICJ0eXBlIjogMCwgInV1aWQiOiAiZWUwZDkyZWUtZTUzZC00ZWJkLWEyOGYt
ZGY5NTllOTQ5ZWQ3IiwgInZpZXdfaXRlbXMiOiBbXSwgIndvcmtmbG93cyI6IFtdfV0sICJhdXRv
bWF0aWNfdGFza3MiOiBbXSwgImV4cG9ydF9kYXRlIjogMTU5OTU4NDgyMDgxOSwgImV4cG9ydF9m
b3JtYXRfdmVyc2lvbiI6IDIsICJmaWVsZHMiOiBbeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFs
c2UsICJibGFua19vcHRpb24iOiB0cnVlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJs
ZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZh
bHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL2RmX3F1
ZXJ5X2FwaV9tZXRob2QiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMTg1LCAi
aW5wdXRfdHlwZSI6ICJib29sZWFuIiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjog
ZmFsc2UsICJuYW1lIjogImRmX3F1ZXJ5X2FwaV9tZXRob2QiLCAib3BlcmF0aW9uX3Blcm1zIjog
e30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIiLCAicHJlZml4IjogbnVsbCwg
InJlYWRfb25seSI6IGZhbHNlLCAicmVxdWlyZWQiOiAiYWx3YXlzIiwgInJpY2hfdGV4dCI6IGZh
bHNlLCAidGFncyI6IFtdLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogImRmX3F1ZXJ5X2FwaV9t
ZXRob2QiLCAidG9vbHRpcCI6ICIiLCAidHlwZV9pZCI6IDExLCAidXVpZCI6ICI3MzFlOTRmZi04
MjJmLTQ4ZjEtODNhOS1hNzgzODBmZDYzNmIiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1
bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZh
bHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2Vu
X2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJf
X2Z1bmN0aW9uL2RmX21pbl9pbmNpZGVudF9pZCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNl
LCAiaWQiOiAxODQsICJpbnB1dF90eXBlIjogIm51bWJlciIsICJpbnRlcm5hbCI6IGZhbHNlLCAi
aXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJkZl9taW5faW5jaWRlbnRfaWQiLCAib3BlcmF0
aW9uX3Blcm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIiLCAicHJl
Zml4IjogbnVsbCwgInJlYWRfb25seSI6IGZhbHNlLCAicmVxdWlyZWQiOiAiYWx3YXlzIiwgInJp
Y2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFtdLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogImRm
X21pbl9pbmNpZGVudF9pZCIsICJ0b29sdGlwIjogIkVudGVyIGFuIGluY2lkZW50ICMgb3IgMCB0
byBpbmRpY2F0ZSB0aGUgc3RhcnQgb2YgYWxsIGluY2lkZW50cyIsICJ0eXBlX2lkIjogMTEsICJ1
dWlkIjogImI4MGQxMWQ0LTljNmItNGNkNy05NTFhLTRmZThjNTcyYzllZiIsICJ2YWx1ZXMiOiBb
XX0sIHsiYWxsb3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2Us
ICJjYWxjdWxhdGVkIjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNl
LCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2Us
ICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vZGZfbWF4X2luY2lkZW50X2lkIiwgImhpZGVfbm90
aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDE4MywgImlucHV0X3R5cGUiOiAibnVtYmVyIiwgImlu
dGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogImRmX21heF9pbmNp
ZGVudF9pZCIsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgInBsYWNl
aG9sZGVyIjogIiIsICJwcmVmaXgiOiBudWxsLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3Rl
eHQiOiBmYWxzZSwgInRhZ3MiOiBbXSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJkZl9tYXhf
aW5jaWRlbnRfaWQiLCAidG9vbHRpcCI6ICJFbnRlciBpbmNpZGVudCAjIGZvciB1cHBlciByYW5n
ZSBvciAwIHRvIGluZGljYXRlIGFsbCBpbmNpZGVudHMiLCAidHlwZV9pZCI6IDExLCAidXVpZCI6
ICJlNzgyMGU0NC00MDg3LTRjZTItODRhZi0wZmU5MzYzMGEwM2MiLCAidmFsdWVzIjogW119LCB7
ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2Fs
Y3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRl
ZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhw
b3J0X2tleSI6ICJhY3Rpb25pbnZvY2F0aW9uL2RhdGFfZmVlZGVyX21heGltdW1faW5jaWRlbnRf
aWQiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMTgyLCAiaW5wdXRfdHlwZSI6
ICJudW1iZXIiLCAiaW50ZXJuYWwiOiBmYWxzZSwgImlzX3RyYWNrZWQiOiBmYWxzZSwgIm5hbWUi
OiAiZGF0YV9mZWVkZXJfbWF4aW11bV9pbmNpZGVudF9pZCIsICJvcGVyYXRpb25fcGVybXMiOiB7
fSwgIm9wZXJhdGlvbnMiOiBbXSwgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiAicHJvcGVy
dGllcyIsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFtd
LCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogIk1heGltdW0gSW5jaWRlbnQgSUQiLCAidG9vbHRp
cCI6ICJFbnRlciBJbmNpZGVudCBJRCB0byBzeW5jIHVwIHRvIG9yIDAgdG8gaW5kaWNhdGUgYWxs
IGluY2lkZW50cyIsICJ0eXBlX2lkIjogNiwgInV1aWQiOiAiM2UyZTkzZGUtNmJhNS00YWRmLWIw
NDQtNjZhNDYwOWRkNzdkIiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjog
ZmFsc2UsICJibGFua19vcHRpb24iOiB0cnVlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdl
YWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6
IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJhY3Rpb25pbnZvY2F0
aW9uL3F1ZXJ5X2FwaV9tZXRob2QiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjog
MTgxLCAiaW5wdXRfdHlwZSI6ICJib29sZWFuIiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFj
a2VkIjogZmFsc2UsICJuYW1lIjogInF1ZXJ5X2FwaV9tZXRob2QiLCAib3BlcmF0aW9uX3Blcm1z
Ijoge30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIiLCAicHJlZml4IjogInBy
b3BlcnRpZXMiLCAicmVhZF9vbmx5IjogZmFsc2UsICJyZXF1aXJlZCI6ICJhbHdheXMiLCAicmlj
aF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW10sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAiUXVl
cnkgQVBJIE1ldGhvZCIsICJ0b29sdGlwIjogIlNwZWNpZnkgdHJ1ZSBpZiBlcnJvcnMgb2NjdXIg
d2hlbiB1c2luZyB0aGUgZGVmYXVsdCBzZWFyY2ggY2FwYWJpbGl0eSIsICJ0eXBlX2lkIjogNiwg
InV1aWQiOiAiN2VkM2FmMDMtZDNiMy00MWVkLWE3MjEtOTcwNTQzNDYzNTk4IiwgInZhbHVlcyI6
IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxz
ZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFs
c2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxz
ZSwgImV4cG9ydF9rZXkiOiAiYWN0aW9uaW52b2NhdGlvbi9kYXRhX2ZlZWRlcl9taW5pbXVtX2lu
Y2lkZW50X2lkIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDE4MCwgImlucHV0
X3R5cGUiOiAibnVtYmVyIiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2Us
ICJuYW1lIjogImRhdGFfZmVlZGVyX21pbmltdW1faW5jaWRlbnRfaWQiLCAib3BlcmF0aW9uX3Bl
cm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIiLCAicHJlZml4Ijog
InByb3BlcnRpZXMiLCAicmVhZF9vbmx5IjogZmFsc2UsICJyZXF1aXJlZCI6ICJhbHdheXMiLCAi
cmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW10sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAi
TWluaW11bSBJbmNpZGVudCBJRCIsICJ0b29sdGlwIjogIkVudGVyIEluY2lkZW50IElEIHRvIHN0
YXJ0IHN5bmMgb3IgMCIsICJ0eXBlX2lkIjogNiwgInV1aWQiOiAiY2M1MzJhMjItZTkwZi00NmU0
LTkxOWEtMGFkMTI5Njc5NmJmIiwgInZhbHVlcyI6IFtdfSwgeyJleHBvcnRfa2V5IjogImluY2lk
ZW50L2ludGVybmFsX2N1c3RvbWl6YXRpb25zX2ZpZWxkIiwgImlkIjogMCwgImlucHV0X3R5cGUi
OiAidGV4dCIsICJpbnRlcm5hbCI6IHRydWUsICJuYW1lIjogImludGVybmFsX2N1c3RvbWl6YXRp
b25zX2ZpZWxkIiwgInJlYWRfb25seSI6IHRydWUsICJ0ZXh0IjogIkN1c3RvbWl6YXRpb25zIEZp
ZWxkIChpbnRlcm5hbCkiLCAidHlwZV9pZCI6IDAsICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFl
OC1hZDM5LTRhMDAwNDA0NGFhMSJ9XSwgImZ1bmN0aW9ucyI6IFt7ImNyZWF0b3IiOiB7ImRpc3Bs
YXlfbmFtZSI6ICJpbnRlZ3JhdGlvbnMiLCAiaWQiOiA0LCAibmFtZSI6ICJlYjJkMWY3ZC02NjUx
LTQxNWEtYjRmZi1hMTRmY2QyZjg0ZjUiLCAidHlwZSI6ICJhcGlrZXkifSwgImRlc2NyaXB0aW9u
IjogeyJmb3JtYXQiOiAidGV4dCIsICJjb250ZW50IjogIlN5bmNocm9uaXplIEluY2lkZW50KHMp
IGFuZCB0aGVpciBhc3NvY2lhdGVkIHRhc2tzLCBub3RlcywgYXR0YWNobWVudHMsIGFydGlmYWN0
cywgbWlsZXN0b25lcyBhbmQgYXNzb2NpYXRlZCBkYXRhdGFibGVzIn0sICJkZXN0aW5hdGlvbl9o
YW5kbGUiOiAiZmVlZF9kYXRhIiwgImRpc3BsYXlfbmFtZSI6ICJEYXRhIEZlZWRlcjogU3luYyBJ
bmNpZGVudHMiLCAiZXhwb3J0X2tleSI6ICJkYXRhX2ZlZWRlcl9zeW5jX2luY2lkZW50cyIsICJp
ZCI6IDEsICJsYXN0X21vZGlmaWVkX2J5IjogeyJkaXNwbGF5X25hbWUiOiAiaW50ZWdyYXRpb25z
IiwgImlkIjogNCwgIm5hbWUiOiAiZWIyZDFmN2QtNjY1MS00MTVhLWI0ZmYtYTE0ZmNkMmY4NGY1
IiwgInR5cGUiOiAiYXBpa2V5In0sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTc3MjQwMTI4Njk1
LCAibmFtZSI6ICJkYXRhX2ZlZWRlcl9zeW5jX2luY2lkZW50cyIsICJ0YWdzIjogW10sICJ1dWlk
IjogIjdmZmVkNGU1LTcyZmItNDE2Mi1iZGVmLTRlYTNlYmZhODlkZSIsICJ2ZXJzaW9uIjogMSwg
InZpZXdfaXRlbXMiOiBbeyJjb250ZW50IjogImI4MGQxMWQ0LTljNmItNGNkNy05NTFhLTRmZThj
NTcyYzllZiIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0
aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9s
YWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiZTc4MjBlNDQtNDA4Ny00Y2UyLTg0YWYtMGZlOTM2
MzBhMDNjIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rp
b24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xh
YmVsIjogbnVsbH0sIHsiY29udGVudCI6ICI3MzFlOTRmZi04MjJmLTQ4ZjEtODNhOS1hNzgzODBm
ZDYzNmIiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlv
biIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFi
ZWwiOiBudWxsfV0sICJ3b3JrZmxvd3MiOiBbeyJhY3Rpb25zIjogW10sICJkZXNjcmlwdGlvbiI6
IG51bGwsICJuYW1lIjogIkRhdGEgRmVlZGVyOiBTeW5jIEluY2lkZW50cyIsICJvYmplY3RfdHlw
ZSI6ICJpbmNpZGVudCIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJkYXRhX2ZlZWRlcl9zeW5jX2lu
Y2lkZW50cyIsICJ0YWdzIjogW10sICJ1dWlkIjogbnVsbCwgIndvcmtmbG93X2lkIjogMX1dfV0s
ICJnZW9zIjogbnVsbCwgImdyb3VwcyI6IG51bGwsICJpZCI6IDEsICJpbmJvdW5kX21haWxib3hl
cyI6IG51bGwsICJpbmNpZGVudF9hcnRpZmFjdF90eXBlcyI6IFtdLCAiaW5jaWRlbnRfdHlwZXMi
OiBbeyJ1cGRhdGVfZGF0ZSI6IDE1OTk1ODQ4MDY3NDUsICJjcmVhdGVfZGF0ZSI6IDE1OTk1ODQ4
MDY3NDUsICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIsICJk
ZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZXhwb3J0
X2tleSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAibmFtZSI6ICJDdXN0
b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVt
IjogZmFsc2UsICJwYXJlbnRfaWQiOiBudWxsLCAiaGlkZGVuIjogZmFsc2UsICJpZCI6IDB9XSwg
ImluZHVzdHJpZXMiOiBudWxsLCAibGF5b3V0cyI6IFtdLCAibG9jYWxlIjogbnVsbCwgIm1lc3Nh
Z2VfZGVzdGluYXRpb25zIjogW3siYXBpX2tleXMiOiBbImViMmQxZjdkLTY2NTEtNDE1YS1iNGZm
LWExNGZjZDJmODRmNSJdLCAiZGVzdGluYXRpb25fdHlwZSI6IDAsICJleHBlY3RfYWNrIjogdHJ1
ZSwgImV4cG9ydF9rZXkiOiAiZmVlZF9kYXRhIiwgIm5hbWUiOiAiZmVlZF9kYXRhIiwgInByb2dy
YW1tYXRpY19uYW1lIjogImZlZWRfZGF0YSIsICJ0YWdzIjogW10sICJ1c2VycyI6IFtdLCAidXVp
ZCI6ICJlMDUyODJmYi02Y2ZjLTQ3MDktYWY4NC1jZDcxNDM4NTgxYzgifV0sICJub3RpZmljYXRp
b25zIjogbnVsbCwgIm92ZXJyaWRlcyI6IFtdLCAicGhhc2VzIjogW10sICJyZWd1bGF0b3JzIjog
bnVsbCwgInJvbGVzIjogW10sICJzY3JpcHRzIjogW10sICJzZXJ2ZXJfdmVyc2lvbiI6IHsiYnVp
bGRfbnVtYmVyIjogMzIsICJtYWpvciI6IDM1LCAibWlub3IiOiAyLCAidmVyc2lvbiI6ICIzNS4y
LjMyIn0sICJ0YWdzIjogW10sICJ0YXNrX29yZGVyIjogW10sICJ0aW1lZnJhbWVzIjogbnVsbCwg
InR5cGVzIjogW10sICJ3b3JrZmxvd3MiOiBbeyJhY3Rpb25zIjogW10sICJjb250ZW50IjogeyJ2
ZXJzaW9uIjogMSwgIndvcmtmbG93X2lkIjogImRhdGFfZmVlZGVyX3N5bmNfaW5jaWRlbnRzIiwg
InhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5p
dGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVM
XCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9E
SVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENc
IiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIg
eG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4
c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6
Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwi
aHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJkYXRhX2ZlZWRlcl9z
eW5jX2luY2lkZW50c1wiIGlzRXhlY3V0YWJsZT1cInRydWVcIiBuYW1lPVwiRGF0YSBGZWVkZXI6
IFN5bmMgSW5jaWRlbnRzXCI+PGRvY3VtZW50YXRpb24+U3luY2hyb25pemUgSW5jaWRlbnQocykg
YW5kIHRoZWlyIGFzc29jaWF0ZWQgdGFza3MsIG5vdGVzLCBhdHRhY2htZW50cywgYXJ0aWZhY3Rz
LCBtaWxlc3RvbmVzIGFuZCBhc3NvY2lhdGVkIGRhdGF0YWJsZXM8L2RvY3VtZW50YXRpb24+PHN0
YXJ0RXZlbnQgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIj48b3V0Z29pbmc+U2VxdWVuY2VGbG93
XzFndmxudmc8L291dGdvaW5nPjwvc3RhcnRFdmVudD48c2VydmljZVRhc2sgaWQ9XCJTZXJ2aWNl
VGFza18weW9mN2hpXCIgbmFtZT1cIkRhdGEgRmVlZGVyOiBTeW5jIEluY2lkZW50c1wiIHJlc2ls
aWVudDp0eXBlPVwiZnVuY3Rpb25cIj48ZXh0ZW5zaW9uRWxlbWVudHM+PHJlc2lsaWVudDpmdW5j
dGlvbiB1dWlkPVwiN2ZmZWQ0ZTUtNzJmYi00MTYyLWJkZWYtNGVhM2ViZmE4OWRlXCI+e1wiaW5w
dXRzXCI6e30sXCJwb3N0X3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCIjIHsndmVyc2lvbic6ICcxLjAn
LCAnc3VjY2Vzcyc6IFRydWUsICdyZWFzb24nOiBOb25lLCAnY29udGVudCc6IHsnbnVtX29mX3N5
bmNfaW5jaWRlbnRzJzogMn0sICdyYXcnOiAne1xcXCJudW1fb2Zfc3luY19pbmNpZGVudHNcXFwi
OiAyfScsICdpbnB1dHMnOiB7J2RmX21heF9pbmNpZGVudF9pZCc6IE5vbmUsICdkZl9taW5faW5j
aWRlbnRfaWQnOiAwfSwgJ21ldHJpY3MnOiB7J3ZlcnNpb24nOiAnMS4wJywgJ3BhY2thZ2UnOiAn
dW5rbm93bicsICdwYWNrYWdlX3ZlcnNpb24nOiAndW5rbm93bicsICdob3N0JzogJ01hcmtzLU1C
UC5maW9zLXJvdXRlci5ob21lJywgJ2V4ZWN1dGlvbl90aW1lX21zJzogMjA2MiwgJ3RpbWVzdGFt
cCc6ICcyMDE5LTA1LTE0IDIxOjM3OjA1J319XFxuaW5jaWRlbnQuYWRkTm90ZShcXFwiRGF0YSBG
ZWVkZXIgU3luY1xcXFxuTWluOiB7fSBNYXg6IHt9XFxcXG5JbmNpZGVudHMgU3luYydkOiB7fVxc
XCIuZm9ybWF0KFxcbiAgICAgICByZXN1bHRzWydpbnB1dHMnXVsnZGZfbWluX2luY2lkZW50X2lk
J10sIFxcbiAgICAgICByZXN1bHRzWydpbnB1dHMnXVsnZGZfbWF4X2luY2lkZW50X2lkJ10sXFxu
ICAgICAgIHJlc3VsdHNbJ2NvbnRlbnQnXVsnbnVtX29mX3N5bmNfaW5jaWRlbnRzJ10pKVwiLFwi
cHJlX3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCJ0cnk6XFxuICBpbnB1dHMuZGZfbWluX2luY2lkZW50
X2lkID0gcnVsZS5wcm9wZXJ0aWVzLmRhdGFfZmVlZGVyX21pbmltdW1faW5jaWRlbnRfaWRcXG4g
IGlucHV0cy5kZl9tYXhfaW5jaWRlbnRfaWQgPSBydWxlLnByb3BlcnRpZXMuZGF0YV9mZWVkZXJf
bWF4aW11bV9pbmNpZGVudF9pZFxcbiAgaW5wdXRzLmRmX3F1ZXJ5X2FwaV9tZXRob2QgPSBydWxl
LnByb3BlcnRpZXMucXVlcnlfYXBpX21ldGhvZFxcbmV4Y2VwdDpcXG4gIGhlbHBlci5mYWlsKFxc
XCJUaGlzIHZlcnNpb24gb2YgUmVzaWxpZW50IGNhbm5vdCB1c2UgdGhpcyBmdW5jdGlvblxcXCIp
XFxuICBcIixcInJlc3VsdF9uYW1lXCI6XCJcIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVu
c2lvbkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMWd2bG52ZzwvaW5jb21pbmc+PG91
dGdvaW5nPlNlcXVlbmNlRmxvd18xZzdkNjk3PC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxzZXF1
ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMWd2bG52Z1wiIHNvdXJjZVJlZj1cIlN0YXJ0RXZl
bnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzB5b2Y3aGlcIi8+PGVuZEV2ZW50
IGlkPVwiRW5kRXZlbnRfMXZndzE4ZlwiPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMWc3ZDY5Nzwv
aW5jb21pbmc+PC9lbmRFdmVudD48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzFnN2Q2
OTdcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18weW9mN2hpXCIgdGFyZ2V0UmVmPVwiRW5kRXZl
bnRfMXZndzE4ZlwiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0
XCI+PHRleHQ+U3RhcnQgeW91ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+
PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0
RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PHRl
eHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMDMzMzRjYlwiPjx0ZXh0PkNyZWF0ZXMg
YW4gaW5jaWRlbnQgbm90ZSB3aXRoIG51bWJlciBvZiBpbmNpZGVudHMgc3luY2hyb25pemVkPC90
ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMDd0YnV6
a1wiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzB5b2Y3aGlcIiB0YXJnZXRSZWY9XCJUZXh0QW5u
b3RhdGlvbl8wMzMzNGNiXCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5vdGF0aW9uXzFs
dmJ2NjJcIj48dGV4dD5JbnB1dCBmcm9tIFJ1bGUgYWN0aXZpdHkgZmllbGRzPC90ZXh0PjwvdGV4
dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMG5paXp3ZFwiIHNvdXJj
ZVJlZj1cIlNlcnZpY2VUYXNrXzB5b2Y3aGlcIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8x
bHZidjYyXCIvPjwvcHJvY2Vzcz48YnBtbmRpOkJQTU5EaWFncmFtIGlkPVwiQlBNTkRpYWdyYW1f
MVwiPjxicG1uZGk6QlBNTlBsYW5lIGJwbW5FbGVtZW50PVwidW5kZWZpbmVkXCIgaWQ9XCJCUE1O
UGxhbmVfMVwiPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU3RhcnRFdmVudF8xNTVh
c3htXCIgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1fZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1c
IjM2XCIgd2lkdGg9XCIzNlwiIHg9XCIxNjJcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVs
PjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMFwiIHdpZHRoPVwiOTBcIiB4PVwiMTU3XCIgeT1cIjIy
M1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNo
YXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiIGlkPVwiVGV4dEFubm90
YXRpb25fMWt4eGl5dF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjEw
MFwiIHg9XCI5OVwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVk
Z2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgaWQ9XCJBc3NvY2lhdGlvbl8x
c2V1ajQ4X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxNjlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBv
aW50XCIgeT1cIjIyMFwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjE1M1wiIHhzaTp0eXBlPVwib21n
ZGM6UG9pbnRcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBl
IGJwbW5FbGVtZW50PVwiU2VydmljZVRhc2tfMHlvZjdoaVwiIGlkPVwiU2VydmljZVRhc2tfMHlv
ZjdoaV9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiODBcIiB3aWR0aD1cIjEwMFwiIHg9XCIy
OTFcIiB5PVwiMTY2XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5F
bGVtZW50PVwiU2VxdWVuY2VGbG93XzFndmxudmdcIiBpZD1cIlNlcXVlbmNlRmxvd18xZ3ZsbnZn
X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxOThcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIg
eT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjI5MVwiIHhzaTp0eXBlPVwib21nZGM6UG9p
bnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwi
MTNcIiB3aWR0aD1cIjBcIiB4PVwiMjQ0LjVcIiB5PVwiMTg0XCIvPjwvYnBtbmRpOkJQTU5MYWJl
bD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIkVuZEV2
ZW50XzF2Z3cxOGZcIiBpZD1cIkVuZEV2ZW50XzF2Z3cxOGZfZGlcIj48b21nZGM6Qm91bmRzIGhl
aWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCI0NjguNTI3MTY0Njg1OTA4M1wiIHk9XCIxODhc
Ii8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwi
MFwiIHg9XCI0ODYuNTI3MTY0Njg1OTA4M1wiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVs
PjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVu
Y2VGbG93XzFnN2Q2OTdcIiBpZD1cIlNlcXVlbmNlRmxvd18xZzdkNjk3X2RpXCI+PG9tZ2RpOndh
eXBvaW50IHg9XCIzOTFcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21n
ZGk6d2F5cG9pbnQgeD1cIjQ2OVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIv
PjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBc
IiB4PVwiNDMwXCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVk
Z2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8wMzMzNGNi
XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8wMzMzNGNiX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9
XCI1OVwiIHdpZHRoPVwiMTc2XCIgeD1cIjM4NFwiIHk9XCI2N1wiLz48L2JwbW5kaTpCUE1OU2hh
cGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzA3dGJ1emtcIiBp
ZD1cIkFzc29jaWF0aW9uXzA3dGJ1emtfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjM4NVwiIHhz
aTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTcwXCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNDM4
XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIxMjZcIi8+PC9icG1uZGk6QlBNTkVkZ2U+
PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8xbHZidjYyXCIg
aWQ9XCJUZXh0QW5ub3RhdGlvbl8xbHZidjYyX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI0
NlwiIHdpZHRoPVwiMTMzXCIgeD1cIjE0NVwiIHk9XCI4MlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+
PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzBuaWl6d2RcIiBpZD1c
IkFzc29jaWF0aW9uXzBuaWl6d2RfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjI5NlwiIHhzaTp0
eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTcxXCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMjQxXCIg
eHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIxMjhcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PC9i
cG1uZGk6QlBNTlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+In0sICJj
b250ZW50X3ZlcnNpb24iOiAxLCAiY3JlYXRvcl9pZCI6ICJlYjJkMWY3ZC02NjUxLTQxNWEtYjRm
Zi1hMTRmY2QyZjg0ZjUiLCAiZGVzY3JpcHRpb24iOiAiU3luY2hyb25pemUgSW5jaWRlbnQocykg
YW5kIHRoZWlyIGFzc29jaWF0ZWQgdGFza3MsIG5vdGVzLCBhdHRhY2htZW50cywgYXJ0aWZhY3Rz
LCBtaWxlc3RvbmVzIGFuZCBhc3NvY2lhdGVkIGRhdGF0YWJsZXMiLCAiZXhwb3J0X2tleSI6ICJk
YXRhX2ZlZWRlcl9zeW5jX2luY2lkZW50cyIsICJsYXN0X21vZGlmaWVkX2J5IjogImViMmQxZjdk
LTY2NTEtNDE1YS1iNGZmLWExNGZjZDJmODRmNSIsICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTc3
MjQwMTI5MjM5LCAibmFtZSI6ICJEYXRhIEZlZWRlcjogU3luYyBJbmNpZGVudHMiLCAib2JqZWN0
X3R5cGUiOiAiaW5jaWRlbnQiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiZGF0YV9mZWVkZXJfc3lu
Y19pbmNpZGVudHMiLCAidGFncyI6IFtdLCAidXVpZCI6ICI0MzM3MDZhNS0yYjYxLTQ4ZDgtOWIx
My1iNDI0NjJhNGU5MDkiLCAid29ya2Zsb3dfaWQiOiAxfV0sICJ3b3Jrc3BhY2VzIjogW119
""")
