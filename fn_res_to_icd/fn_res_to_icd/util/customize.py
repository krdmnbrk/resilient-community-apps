# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_res_to_icd"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_res_to_icd package"""
    reload_params = {"package": u"fn_res_to_icd",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "function_params": [u"incident_id"], 
                    "datatables": [], 
                    "message_destinations": [u"fn_res_to_icd"], 
                    "functions": [u"res_to_icd_function"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [u"example_res_to_icd"], 
                    "actions": [u"Example: Escalate to ICD"], 
                    "incident_artifact_types": [] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     incident_id
    #   Message Destinations:
    #     fn_res_to_icd
    #   Functions:
    #     res_to_icd_function
    #   Workflows:
    #     example_res_to_icd
    #   Rules:
    #     Example: Escalate to ICD


    yield ImportDefinition(u"""
eyJhY3Rpb25fb3JkZXIiOiBbXSwgImFjdGlvbnMiOiBbeyJhdXRvbWF0aW9ucyI6IFtdLCAiY29u
ZGl0aW9ucyI6IFtdLCAiZXhwb3J0X2tleSI6ICJFeGFtcGxlOiBFc2NhbGF0ZSB0byBJQ0QiLCAi
aWQiOiAxNDcsICJsb2dpY190eXBlIjogImFsbCIsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtd
LCAibmFtZSI6ICJFeGFtcGxlOiBFc2NhbGF0ZSB0byBJQ0QiLCAib2JqZWN0X3R5cGUiOiAiaW5j
aWRlbnQiLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ0eXBlIjogMSwgInV1aWQiOiAiMjc0
NGFhMDgtOTM1My00NmY0LWI0OWYtMjgxMDk1OWJhNzEzIiwgInZpZXdfaXRlbXMiOiBbXSwgIndv
cmtmbG93cyI6IFsiZXhhbXBsZV9yZXNfdG9faWNkIl19XSwgImF1dG9tYXRpY190YXNrcyI6IFtd
LCAiZXhwb3J0X2RhdGUiOiAxNTYyMjM4Njk2NjgzLCAiZXhwb3J0X2Zvcm1hdF92ZXJzaW9uIjog
MiwgImZpZWxkcyI6IFt7ImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUs
ICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVw
cmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJpbmNpZGVudC9pbmNfdHJhaW5pbmciLCAi
aGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMjIzLCAiaW5wdXRfdHlwZSI6ICJib29s
ZWFuIiwgImludGVybmFsIjogZmFsc2UsICJuYW1lIjogImluY190cmFpbmluZyIsICJvcGVyYXRp
b25fcGVybXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgInByZWZpeCI6IG51bGwsICJyZWFkX29u
bHkiOiB0cnVlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAi
U2ltdWxhdGlvbiIsICJ0b29sdGlwIjogIldoZXRoZXIgdGhlIGluY2lkZW50IGlzIGEgc2ltdWxh
dGlvbiBvciBhIHJlZ3VsYXIgaW5jaWRlbnQuICBUaGlzIGZpZWxkIGlzIHJlYWQtb25seS4iLCAi
dHlwZV9pZCI6IDAsICJ1dWlkIjogImMzZjBlM2VkLTIxZTEtNGQ1My1hZmZiLWZlNWNhMzMwOGNj
YSIsICJ2YWx1ZXMiOiBbXX0sIHsiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjaGFuZ2VhYmxlIjog
dHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2Us
ICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vaW5jaWRlbnRf
aWQiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzIxLCAiaW5wdXRfdHlwZSI6
ICJudW1iZXIiLCAiaW50ZXJuYWwiOiBmYWxzZSwgIm5hbWUiOiAiaW5jaWRlbnRfaWQiLCAib3Bl
cmF0aW9uX3Blcm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIiLCAi
cHJlZml4IjogbnVsbCwgInJlYWRfb25seSI6IGZhbHNlLCAicmVxdWlyZWQiOiAiYWx3YXlzIiwg
InJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogImluY2lkZW50X2lk
IiwgInRvb2x0aXAiOiAiaW5jaWRlbnRfaWQgZm9yIGZ1bmN0aW9uIGFjdGlvbnMiLCAidHlwZV9p
ZCI6IDExLCAidXVpZCI6ICIwZGQxYzJlMS05NWM5LTQ0NGMtODY4OC0yNjlkZWE2ZmI3ZjEiLCAi
dmFsdWVzIjogW119XSwgImZ1bmN0aW9ucyI6IFt7ImNyZWF0b3IiOiB7ImRpc3BsYXlfbmFtZSI6
ICJTZWFuIE8gR29ybWFuIiwgImlkIjogNzcsICJuYW1lIjogInNlYW4ub2dvcm1hbkBpYm0uY29t
IiwgInR5cGUiOiAidXNlciJ9LCAiZGVzY3JpcHRpb24iOiB7ImZvcm1hdCI6ICJ0ZXh0IiwgImNv
bnRlbnQiOiAiVGhpcyBmdW5jdGlvbiB0cmFuc2ZlcnMgYSByZXNpbGllbnQgd2l0aCBhIHFyYWRh
ciBzZXZlcml0eSAoMS0xMCkgdG8gYW4gaWNkIHRpY2tldCB3aXRoIGEgcHJpb3JpdHkgKDQtMSki
fSwgImRlc3RpbmF0aW9uX2hhbmRsZSI6ICJmbl9yZXNfdG9faWNkIiwgImRpc3BsYXlfbmFtZSI6
ICJyZXNfdG9faWNkX2Z1bmN0aW9uIiwgImV4cG9ydF9rZXkiOiAicmVzX3RvX2ljZF9mdW5jdGlv
biIsICJpZCI6IDM0LCAibGFzdF9tb2RpZmllZF9ieSI6IHsiZGlzcGxheV9uYW1lIjogIlNlYW4g
TyBHb3JtYW4iLCAiaWQiOiA3NywgIm5hbWUiOiAic2Vhbi5vZ29ybWFuQGlibS5jb20iLCAidHlw
ZSI6ICJ1c2VyIn0sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTYyMTU4MDA3NTQyLCAibmFtZSI6
ICJyZXNfdG9faWNkX2Z1bmN0aW9uIiwgInV1aWQiOiAiNzA3NzgwMDktOGNkOS00YTMwLWI2YjYt
MzVjNGYyYjMzZDg3IiwgInZlcnNpb24iOiA4LCAidmlld19pdGVtcyI6IFt7ImNvbnRlbnQiOiAi
MGRkMWMyZTEtOTVjOS00NDRjLTg2ODgtMjY5ZGVhNmZiN2YxIiwgImVsZW1lbnQiOiAiZmllbGRf
dXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93
X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH1dLCAid29ya2Zsb3dzIjog
W3siYWN0aW9ucyI6IFtdLCAiZGVzY3JpcHRpb24iOiBudWxsLCAibmFtZSI6ICJFeGFtcGxlOiBy
ZXNfdG9faWNkIiwgIm9iamVjdF90eXBlIjogImluY2lkZW50IiwgInByb2dyYW1tYXRpY19uYW1l
IjogImV4YW1wbGVfcmVzX3RvX2ljZCIsICJ1dWlkIjogbnVsbCwgIndvcmtmbG93X2lkIjogMjB9
XX1dLCAiZ2VvcyI6IG51bGwsICJpZCI6IDE0MiwgImluY2lkZW50X2FydGlmYWN0X3R5cGVzIjog
W10sICJpbmNpZGVudF90eXBlcyI6IFt7InVwZGF0ZV9kYXRlIjogMTU2MjA5NzcwMzcyMywgImNy
ZWF0ZV9kYXRlIjogMTU2MjA5NzcwMzcyMywgInV1aWQiOiAiYmZlZWMyZDQtMzc3MC0xMWU4LWFk
MzktNGEwMDA0MDQ0YWEwIiwgImRlc2NyaXB0aW9uIjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMg
KGludGVybmFsKSIsICJleHBvcnRfa2V5IjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVy
bmFsKSIsICJuYW1lIjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJlbmFi
bGVkIjogZmFsc2UsICJzeXN0ZW0iOiBmYWxzZSwgInBhcmVudF9pZCI6IG51bGwsICJoaWRkZW4i
OiBmYWxzZSwgImlkIjogMH1dLCAiaW5kdXN0cmllcyI6IG51bGwsICJsYXlvdXRzIjogW10sICJs
b2NhbGUiOiBudWxsLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbeyJkZXN0aW5hdGlvbl90eXBl
IjogMCwgImV4cGVjdF9hY2siOiB0cnVlLCAiZXhwb3J0X2tleSI6ICJmbl9yZXNfdG9faWNkIiwg
Im5hbWUiOiAiZm5fcmVzX3RvX2ljZCIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJmbl9yZXNfdG9f
aWNkIiwgInVzZXJzIjogWyJzZWFuLm9nb3JtYW5AaWJtLmNvbSJdLCAidXVpZCI6ICI2MGVkYTlh
Yi05ZGQ3LTRlYTktODhmNi02MGE3M2JiMTQ3NDIifV0sICJub3RpZmljYXRpb25zIjogbnVsbCwg
Im92ZXJyaWRlcyI6IFtdLCAicGhhc2VzIjogW10sICJyZWd1bGF0b3JzIjogbnVsbCwgInJvbGVz
IjogW10sICJzY3JpcHRzIjogW10sICJzZXJ2ZXJfdmVyc2lvbiI6IHsiYnVpbGRfbnVtYmVyIjog
NDI1NCwgIm1ham9yIjogMzEsICJtaW5vciI6IDAsICJ2ZXJzaW9uIjogIjMxLjAuNDI1NCJ9LCAi
dGFza19vcmRlciI6IFtdLCAidGltZWZyYW1lcyI6IG51bGwsICJ0eXBlcyI6IFtdLCAid29ya2Zs
b3dzIjogW3siYWN0aW9ucyI6IFtdLCAiY29udGVudCI6IHsidmVyc2lvbiI6IDEwLCAid29ya2Zs
b3dfaWQiOiAiZXhhbXBsZV9yZXNfdG9faWNkIiwgInhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4w
XCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9t
Zy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3
dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3
dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cu
b21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jl
c2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAx
L1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1h
LWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0
XCI+PHByb2Nlc3MgaWQ9XCJleGFtcGxlX3Jlc190b19pY2RcIiBpc0V4ZWN1dGFibGU9XCJ0cnVl
XCIgbmFtZT1cIkV4YW1wbGU6IHJlc190b19pY2RcIj48ZG9jdW1lbnRhdGlvbj5UaGlzIHdvcmtm
bG93IGFpbXMgdG8gZXNjYWxhdGUgYSByZXNpbGllbnQgaW5jaWRlbnQgdG8gYW4gaWNkIGRlc2sg
dGlja2V0LCBpbmNsdWRpbmcgdGhlIFFyYWRhciBzZXZlcml0eSB0cmFuc2xhdGVkIHRvIGFuIGlj
ZCBkZXNrIHRpY2tldCBwcmlvcml0eTwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1cIlN0
YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMHR4Y3A5ZTwvb3V0Z29p
bmc+PC9zdGFydEV2ZW50PjxlbmRFdmVudCBpZD1cIkVuZEV2ZW50XzFsM2c4OWNcIj48aW5jb21p
bmc+U2VxdWVuY2VGbG93XzF1OTU4dXA8L2luY29taW5nPjwvZW5kRXZlbnQ+PHNlcXVlbmNlRmxv
dyBpZD1cIlNlcXVlbmNlRmxvd18wdHhjcDllXCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVh
c3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMDY4anNha1wiLz48c2VydmljZVRhc2sgaWQ9
XCJTZXJ2aWNlVGFza18wNjhqc2FrXCIgbmFtZT1cInJlc190b19pY2RfZnVuY3Rpb25cIiByZXNp
bGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVu
Y3Rpb24gdXVpZD1cIjcwNzc4MDA5LThjZDktNGEzMC1iNmI2LTM1YzRmMmIzM2Q4N1wiPntcImlu
cHV0c1wiOnt9LFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiaWYgcmVzdWx0cy5zdWNjZXNz
OlxcbiAgbm90ZV90ZXh0ID1cXFwiezB9IGhhcyBiZWVuIGFkZGVkIHRvIGljZCBkZXNrIHByaW9y
aXR5IHdpdGggaWNkX2lkIHsxfVxcXCIuZm9ybWF0KGluY2lkZW50LmlkLHJlc3VsdHMuaWNkX2lk
KVxcbiAgaW5jaWRlbnQuYWRkTm90ZShoZWxwZXIuY3JlYXRlUGxhaW5UZXh0KG5vdGVfdGV4dCkp
XFxuZWxzZTpcXG4gIG5vdGVfdGV4dCA9IFxcXCJFcnJvciBhZGRpbmcgUXJhZGFyIHNldmVyaXR5
IHt9XFxcIi5mb3JtYXQoaW5jaWRlbnQudmFsdWUpXFxuICBpbmNpZGVudC5hZGROb3RlKGhlbHBl
ci5jcmVhdGVQbGFpblRleHQobm90ZV90ZXh0KSlcIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdFwi
OlwiaW5wdXRzLmluY2lkZW50X2lkPWluY2lkZW50LmlkXCJ9PC9yZXNpbGllbnQ6ZnVuY3Rpb24+
PC9leHRlbnNpb25FbGVtZW50cz48aW5jb21pbmc+U2VxdWVuY2VGbG93XzB0eGNwOWU8L2luY29t
aW5nPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMXU5NTh1cDwvb3V0Z29pbmc+PC9zZXJ2aWNlVGFz
az48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzF1OTU4dXBcIiBzb3VyY2VSZWY9XCJT
ZXJ2aWNlVGFza18wNjhqc2FrXCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMWwzZzg5Y1wiLz48dGV4
dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+U3RhcnQgeW91
ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwi
QXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRh
cmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PC9wcm9jZXNzPjxicG1uZGk6QlBN
TkRpYWdyYW0gaWQ9XCJCUE1ORGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1OUGxhbmUgYnBtbkVsZW1l
bnQ9XCJ1bmRlZmluZWRcIiBpZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5kaTpCUE1OU2hhcGUgYnBt
bkVsZW1lbnQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bV9k
aVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjE2MFwiIHk9
XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIwXCIgd2lk
dGg9XCI5MFwiIHg9XCIxNTVcIiB5PVwiMjIzXCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5k
aTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlv
bl8xa3h4aXl0XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0X2RpXCI+PG9tZ2RjOkJvdW5k
cyBoZWlnaHQ9XCIzMFwiIHdpZHRoPVwiMTAwXCIgeD1cIjk5XCIgeT1cIjI1NFwiLz48L2JwbW5k
aTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzFz
ZXVqNDhcIiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1c
IjE2OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjIwXCIvPjxvbWdkaTp3YXlwb2lu
dCB4PVwiMTUzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyNTRcIi8+PC9icG1uZGk6
QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJFbmRFdmVudF8xbDNnODlj
XCIgaWQ9XCJFbmRFdmVudF8xbDNnODljX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwi
IHdpZHRoPVwiMzZcIiB4PVwiNDkwXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21n
ZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjUwOFwiIHk9XCIyMjdcIi8+
PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJw
bW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzB0eGNwOWVcIiBpZD1cIlNlcXVlbmNlRmxvd18wdHhj
cDllX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxOTZcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50
XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjI3NlwiIHhzaTp0eXBlPVwib21nZGM6
UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0
PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiMjM2XCIgeT1cIjE4NC41XCIvPjwvYnBtbmRpOkJQTU5M
YWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNl
cnZpY2VUYXNrXzA2OGpzYWtcIiBpZD1cIlNlcnZpY2VUYXNrXzA2OGpzYWtfZGlcIj48b21nZGM6
Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwiMjc2LjExNjI3OTA2OTc2NzRc
IiB5PVwiMTY2XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVt
ZW50PVwiU2VxdWVuY2VGbG93XzF1OTU4dXBcIiBpZD1cIlNlcXVlbmNlRmxvd18xdTk1OHVwX2Rp
XCI+PG9tZ2RpOndheXBvaW50IHg9XCIzNzZcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1c
IjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjQ5MFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRc
IiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNc
IiB3aWR0aD1cIjBcIiB4PVwiNDMzXCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9i
cG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFncmFtPjwv
ZGVmaW5pdGlvbnM+In0sICJjcmVhdG9yX2lkIjogInNlYW4ub2dvcm1hbkBpYm0uY29tIiwgImRl
c2NyaXB0aW9uIjogIlRoaXMgd29ya2Zsb3cgYWltcyB0byBlc2NhbGF0ZSBhIHJlc2lsaWVudCBp
bmNpZGVudCB0byBhbiBpY2QgZGVzayB0aWNrZXQsIGluY2x1ZGluZyB0aGUgUXJhZGFyIHNldmVy
aXR5IHRyYW5zbGF0ZWQgdG8gYW4gaWNkIGRlc2sgdGlja2V0IHByaW9yaXR5IiwgImV4cG9ydF9r
ZXkiOiAiZXhhbXBsZV9yZXNfdG9faWNkIiwgImxhc3RfbW9kaWZpZWRfYnkiOiAic2Vhbi5vZ29y
bWFuQGlibS5jb20iLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTU2MjE1ODAwNzY0MiwgIm5hbWUi
OiAiRXhhbXBsZTogcmVzX3RvX2ljZCIsICJvYmplY3RfdHlwZSI6ICJpbmNpZGVudCIsICJwcm9n
cmFtbWF0aWNfbmFtZSI6ICJleGFtcGxlX3Jlc190b19pY2QiLCAidXVpZCI6ICJkMzcyM2U3Yi0z
MzI3LTQwYjEtYTE5Ni03OGFjYjJiOWM1ZjQiLCAid29ya2Zsb3dfaWQiOiAyMH1dLCAid29ya3Nw
YWNlcyI6IFtdfQ==
"""
    )