# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_vmray_analyzer"""

try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition


def codegen_reload_data():
    """
    Parameters required reload codegen for the fn_vmray_analyzer package
    """
    return {
        "package": u"fn_vmray_analyzer",
        "message_destinations": [u"vmray_sandbox_message_destination"],
        "functions": [u"fn_vmray_sandbox_analyzer"],
        "workflows": [u"example_vmray_sandbox_analyzer_artifact", u"example_vmray_sandbox_analyzer_attachment"],
        "actions": [u"Example: VMRay Sandbox Analyzer [Attachment]", u"Example: VMRay Sandbox Analyzer [Artifact]"],
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
        - vmray_sandbox_message_destination
    - Functions:
        - fn_vmray_sandbox_analyzer
    - Workflows:
        - example_vmray_sandbox_analyzer_artifact
        - example_vmray_sandbox_analyzer_attachment
    - Rules:
        - Example: VMRay Sandbox Analyzer [Attachment]
        - Example: VMRay Sandbox Analyzer [Artifact]
    """

    yield ImportDefinition(u"""
eyJhY3Rpb25fb3JkZXIiOiBbXSwgImFjdGlvbnMiOiBbeyJhdXRvbWF0aW9ucyI6IFtdLCAiY29u
ZGl0aW9ucyI6IFt7ImV2YWx1YXRpb25faWQiOiBudWxsLCAiZmllbGRfbmFtZSI6ICJhcnRpZmFj
dC50eXBlIiwgIm1ldGhvZCI6ICJlcXVhbHMiLCAidHlwZSI6IG51bGwsICJ2YWx1ZSI6ICJPdGhl
ciBGaWxlIn0sIHsiZXZhbHVhdGlvbl9pZCI6IG51bGwsICJmaWVsZF9uYW1lIjogImFydGlmYWN0
LnR5cGUiLCAibWV0aG9kIjogImVxdWFscyIsICJ0eXBlIjogbnVsbCwgInZhbHVlIjogIkxvZyBG
aWxlIn0sIHsiZXZhbHVhdGlvbl9pZCI6IG51bGwsICJmaWVsZF9uYW1lIjogImFydGlmYWN0LnR5
cGUiLCAibWV0aG9kIjogImVxdWFscyIsICJ0eXBlIjogbnVsbCwgInZhbHVlIjogIkVtYWlsIEF0
dGFjaG1lbnQifV0sICJlbmFibGVkIjogdHJ1ZSwgImV4cG9ydF9rZXkiOiAiRXhhbXBsZTogVk1S
YXkgU2FuZGJveCBBbmFseXplciBbQXJ0aWZhY3RdIiwgImlkIjogNTcsICJsb2dpY190eXBlIjog
ImFueSIsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtdLCAibmFtZSI6ICJFeGFtcGxlOiBWTVJh
eSBTYW5kYm94IEFuYWx5emVyIFtBcnRpZmFjdF0iLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3Qi
LCAidGFncyI6IFtdLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ0eXBlIjogMSwgInV1aWQi
OiAiYWI2NTlmZmItYzk3Ni00M2Y4LWFkNzktYWJlYWY0OWU2YTFiIiwgInZpZXdfaXRlbXMiOiBb
XSwgIndvcmtmbG93cyI6IFsiZXhhbXBsZV92bXJheV9zYW5kYm94X2FuYWx5emVyX2FydGlmYWN0
Il19LCB7ImF1dG9tYXRpb25zIjogW10sICJjb25kaXRpb25zIjogW10sICJlbmFibGVkIjogdHJ1
ZSwgImV4cG9ydF9rZXkiOiAiRXhhbXBsZTogVk1SYXkgU2FuZGJveCBBbmFseXplciBbQXR0YWNo
bWVudF0iLCAiaWQiOiA1OCwgImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm1lc3NhZ2VfZGVzdGluYXRp
b25zIjogW10sICJuYW1lIjogIkV4YW1wbGU6IFZNUmF5IFNhbmRib3ggQW5hbHl6ZXIgW0F0dGFj
aG1lbnRdIiwgIm9iamVjdF90eXBlIjogImF0dGFjaG1lbnQiLCAidGFncyI6IFtdLCAidGltZW91
dF9zZWNvbmRzIjogODY0MDAsICJ0eXBlIjogMSwgInV1aWQiOiAiYzdhYWE1ZWEtNGJmOC00OTE0
LTk2OTUtNzJjODNiOWM3ZTgxIiwgInZpZXdfaXRlbXMiOiBbXSwgIndvcmtmbG93cyI6IFsiZXhh
bXBsZV92bXJheV9zYW5kYm94X2FuYWx5emVyX2F0dGFjaG1lbnQiXX1dLCAiYXV0b21hdGljX3Rh
c2tzIjogW10sICJleHBvcnRfZGF0ZSI6IDE1OTk4NzAyNTQ5NjAsICJleHBvcnRfZm9ybWF0X3Zl
cnNpb24iOiAyLCAiZXh0ZW5zaW9ucyI6IFtdLCAiZmllbGRzIjogW3siYWxsb3dfZGVmYXVsdF92
YWx1ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2Us
ICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlf
c2VydmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVu
Y3Rpb24vYXJ0aWZhY3RfaWQiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzQ2
LCAiaW5wdXRfdHlwZSI6ICJudW1iZXIiLCAiaW50ZXJuYWwiOiBmYWxzZSwgImlzX3RyYWNrZWQi
OiBmYWxzZSwgIm5hbWUiOiAiYXJ0aWZhY3RfaWQiLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJv
cGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIiLCAicHJlZml4IjogbnVsbCwgInJlYWRf
b25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW10sICJ0ZW1wbGF0ZXMi
OiBbXSwgInRleHQiOiAiYXJ0aWZhY3RfaWQiLCAidG9vbHRpcCI6ICJ0aGUgaWQgb2YgdGhlIGFy
dGlmYWN0IG9iamVjdCIsICJ0eXBlX2lkIjogMTEsICJ1dWlkIjogImVmZGJjYTdlLTZhZTgtNDI2
OS1hM2QxLTgwZjE3MTZhNjIyMiIsICJ2YWx1ZXMiOiBbXX0sIHsiYWxsb3dfZGVmYXVsdF92YWx1
ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJj
aGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2Vy
dmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rp
b24vYXR0YWNobWVudF9pZCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiAzNDUs
ICJpbnB1dF90eXBlIjogIm51bWJlciIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6
IGZhbHNlLCAibmFtZSI6ICJhdHRhY2htZW50X2lkIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAi
b3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFk
X29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFtdLCAidGVtcGxhdGVz
IjogW10sICJ0ZXh0IjogImF0dGFjaG1lbnRfaWQiLCAidG9vbHRpcCI6ICJ0aGUgaWQgb2YgdGhl
IGF0dGFjaG1lbnQiLCAidHlwZV9pZCI6IDExLCAidXVpZCI6ICIxN2MzZTY1Mi02NTU5LTQ5MzUt
OWY5NS03NDM3NGNhMzdhN2IiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUi
OiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hh
bmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZl
ciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9u
L2luY2lkZW50X2lkIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDE4OCwgImlu
cHV0X3R5cGUiOiAibnVtYmVyIiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFs
c2UsICJuYW1lIjogImluY2lkZW50X2lkIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0
aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFkX29ubHki
OiBmYWxzZSwgInJlcXVpcmVkIjogImFsd2F5cyIsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3Mi
OiBbXSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJpbmNpZGVudF9pZCIsICJ0b29sdGlwIjog
InRoZSBpZCBvZiB0aGUgaW5jaWRlbnQiLCAidHlwZV9pZCI6IDExLCAidXVpZCI6ICJlYWQyMTRj
Mi0xM2ZlLTQzZjYtYTNjNy02NzZhODgzMzhkYmIiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2Rl
ZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6
IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hv
c2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6
ICJfX2Z1bmN0aW9uL2FuYWx5c2lzX3JlcG9ydF9zdGF0dXMiLCAiaGlkZV9ub3RpZmljYXRpb24i
OiBmYWxzZSwgImlkIjogMzQ3LCAiaW5wdXRfdHlwZSI6ICJib29sZWFuIiwgImludGVybmFsIjog
ZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogImFuYWx5c2lzX3JlcG9ydF9zdGF0
dXMiLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRl
ciI6ICIiLCAicHJlZml4IjogbnVsbCwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0Ijog
ZmFsc2UsICJ0YWdzIjogW10sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAiYW5hbHlzaXNfcmVw
b3J0X3N0YXR1cyIsICJ0b29sdGlwIjogInRoZSBhbmFseXNpcyByZXBvcnQgaGFzIGdlbmVyYXRl
ZD8gIFR1cmUgb3IgRmFsc2UiLCAidHlwZV9pZCI6IDExLCAidXVpZCI6ICJjYTdkZTFlMy1mZWU4
LTQzYmUtYjE1MS1hNmM5ZGIwNjAyNDgiLCAidmFsdWVzIjogW119LCB7ImV4cG9ydF9rZXkiOiAi
aW5jaWRlbnQvaW50ZXJuYWxfY3VzdG9taXphdGlvbnNfZmllbGQiLCAiaWQiOiAwLCAiaW5wdXRf
dHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogdHJ1ZSwgIm5hbWUiOiAiaW50ZXJuYWxfY3VzdG9t
aXphdGlvbnNfZmllbGQiLCAicmVhZF9vbmx5IjogdHJ1ZSwgInRleHQiOiAiQ3VzdG9taXphdGlv
bnMgRmllbGQgKGludGVybmFsKSIsICJ0eXBlX2lkIjogMCwgInV1aWQiOiAiYmZlZWMyZDQtMzc3
MC0xMWU4LWFkMzktNGEwMDA0MDQ0YWExIn1dLCAiZnVuY3Rpb25zIjogW3siY3JlYXRvciI6IHsi
ZGlzcGxheV9uYW1lIjogIlJlc2lsaWVudCBTeXNhZG1pbiIsICJpZCI6IDMsICJuYW1lIjogImFA
YS5jb20iLCAidHlwZSI6ICJ1c2VyIn0sICJkZXNjcmlwdGlvbiI6IHsiZm9ybWF0IjogInRleHQi
LCAiY29udGVudCI6ICJBbmFseXplIGFuIGF0dGFjaG1lbnQgb3IgYXJ0aWZhY3QgZmlsZSBmb3Ig
bWFsd2FyZSB1c2luZyBWTVJheSBBbmFseXplciBDbG91ZC4ifSwgImRlc3RpbmF0aW9uX2hhbmRs
ZSI6ICJ2bXJheV9zYW5kYm94X21lc3NhZ2VfZGVzdGluYXRpb24iLCAiZGlzcGxheV9uYW1lIjog
IlZNUmF5IFNhbmRib3ggQW5hbHl6ZXIiLCAiZXhwb3J0X2tleSI6ICJmbl92bXJheV9zYW5kYm94
X2FuYWx5emVyIiwgImlkIjogMzEsICJsYXN0X21vZGlmaWVkX2J5IjogeyJkaXNwbGF5X25hbWUi
OiAiUmVzaWxpZW50IFN5c2FkbWluIiwgImlkIjogMywgIm5hbWUiOiAiYUBhLmNvbSIsICJ0eXBl
IjogInVzZXIifSwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE1OTk4MzE5Njg4ODcsICJuYW1lIjog
ImZuX3ZtcmF5X3NhbmRib3hfYW5hbHl6ZXIiLCAidGFncyI6IFtdLCAidXVpZCI6ICIxYWE1YjY2
OS1lNWQzLTQzNDEtYTVlNi05ZDhiNzBjMTcwNzkiLCAidmVyc2lvbiI6IDEsICJ2aWV3X2l0ZW1z
IjogW3siY29udGVudCI6ICJlYWQyMTRjMi0xM2ZlLTQzZjYtYTNjNy02NzZhODgzMzhkYmIiLCAi
ZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93
X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxs
fSwgeyJjb250ZW50IjogImVmZGJjYTdlLTZhZTgtNDI2OS1hM2QxLTgwZjE3MTZhNjIyMiIsICJl
bGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3df
aWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9
LCB7ImNvbnRlbnQiOiAiMTdjM2U2NTItNjU1OS00OTM1LTlmOTUtNzQzNzRjYTM3YTdiIiwgImVs
ZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19p
ZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0s
IHsiY29udGVudCI6ICJjYTdkZTFlMy1mZWU4LTQzYmUtYjE1MS1hNmM5ZGIwNjAyNDgiLCAiZWxl
bWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lm
IjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfV0s
ICJ3b3JrZmxvd3MiOiBbeyJhY3Rpb25zIjogW10sICJkZXNjcmlwdGlvbiI6IG51bGwsICJuYW1l
IjogIkV4YW1wbGU6IFZNUkFZIFNhbmRib3ggQW5hbHl6ZXIgW0FydGlmYWN0XSIsICJvYmplY3Rf
dHlwZSI6ICJhcnRpZmFjdCIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJleGFtcGxlX3ZtcmF5X3Nh
bmRib3hfYW5hbHl6ZXJfYXJ0aWZhY3QiLCAidGFncyI6IFtdLCAidXVpZCI6IG51bGwsICJ3b3Jr
Zmxvd19pZCI6IDM3fSwgeyJhY3Rpb25zIjogW10sICJkZXNjcmlwdGlvbiI6IG51bGwsICJuYW1l
IjogIkV4YW1wbGU6IFZNUmF5IFNhbmRib3ggQW5hbHl6ZXIgW0F0dGFjaG1lbnRdIiwgIm9iamVj
dF90eXBlIjogImF0dGFjaG1lbnQiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiZXhhbXBsZV92bXJh
eV9zYW5kYm94X2FuYWx5emVyX2F0dGFjaG1lbnQiLCAidGFncyI6IFtdLCAidXVpZCI6IG51bGws
ICJ3b3JrZmxvd19pZCI6IDM2fV19XSwgImdlb3MiOiBudWxsLCAiZ3JvdXBzIjogbnVsbCwgImlk
IjogNjMsICJpbmJvdW5kX21haWxib3hlcyI6IG51bGwsICJpbmNpZGVudF9hcnRpZmFjdF90eXBl
cyI6IFtdLCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJ1cGRhdGVfZGF0ZSI6IDE2MDAyODI3NDU3NjAs
ICJjcmVhdGVfZGF0ZSI6IDE2MDAyODI3NDU3NjAsICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFl
OC1hZDM5LTRhMDAwNDA0NGFhMCIsICJkZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2th
Z2VzIChpbnRlcm5hbCkiLCAiZXhwb3J0X2tleSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChp
bnRlcm5hbCkiLCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAi
ZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJwYXJlbnRfaWQiOiBudWxsLCAiaGlk
ZGVuIjogZmFsc2UsICJpZCI6IDB9XSwgImluZHVzdHJpZXMiOiBudWxsLCAibGF5b3V0cyI6IFtd
LCAibG9jYWxlIjogbnVsbCwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW3siYXBpX2tleXMiOiBb
XSwgImRlc3RpbmF0aW9uX3R5cGUiOiAwLCAiZXhwZWN0X2FjayI6IHRydWUsICJleHBvcnRfa2V5
IjogInZtcmF5X3NhbmRib3hfbWVzc2FnZV9kZXN0aW5hdGlvbiIsICJuYW1lIjogIlZNUmF5IFNh
bmRib3ggTWVzc2FnZSBEZXN0aW5hdGlvbiIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJ2bXJheV9z
YW5kYm94X21lc3NhZ2VfZGVzdGluYXRpb24iLCAidGFncyI6IFtdLCAidXNlcnMiOiBbImFAYS5j
b20iXSwgInV1aWQiOiAiYWI3ZjMzNmMtODBiMi00ODY3LWE2YTktYjZjMzA3MzJiM2YwIn1dLCAi
bm90aWZpY2F0aW9ucyI6IG51bGwsICJvdmVycmlkZXMiOiBbXSwgInBoYXNlcyI6IFtdLCAicmVn
dWxhdG9ycyI6IG51bGwsICJyb2xlcyI6IFtdLCAic2NyaXB0cyI6IFtdLCAic2VydmVyX3ZlcnNp
b24iOiB7ImJ1aWxkX251bWJlciI6IDAsICJtYWpvciI6IDM1LCAibWlub3IiOiAwLCAidmVyc2lv
biI6ICIzNS4wLjAifSwgInRhZ3MiOiBbXSwgInRhc2tfb3JkZXIiOiBbXSwgInRpbWVmcmFtZXMi
OiBudWxsLCAidHlwZXMiOiBbXSwgIndvcmtmbG93cyI6IFt7ImFjdGlvbnMiOiBbXSwgImNvbnRl
bnQiOiB7InZlcnNpb24iOiAxLCAid29ya2Zsb3dfaWQiOiAiZXhhbXBsZV92bXJheV9zYW5kYm94
X2FuYWx5emVyX2FydGlmYWN0IiwgInhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rp
bmc9XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3Bl
Yy9CUE1OLzIwMTAwNTI0L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3Jn
L3NwZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3Jn
L3NwZWMvREQvMjAxMDA1MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9z
cGVjL0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5p
Ym0uY29tL2JwbW5cIiB4bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVt
YVwiIHhtbG5zOnhzaT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNl
XCIgdGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nl
c3MgaWQ9XCJleGFtcGxlX3ZtcmF5X3NhbmRib3hfYW5hbHl6ZXJfYXJ0aWZhY3RcIiBpc0V4ZWN1
dGFibGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1wbGU6IFZNUkFZIFNhbmRib3ggQW5hbHl6ZXIgW0Fy
dGlmYWN0XVwiPjxkb2N1bWVudGF0aW9uPlRoaXMgd29ya2Zsb3cgdGFrZXMgYW4gYXJ0aWZhY3Qg
ZmlsZSBhcyBpbnB1dCBhbmQgY2FsbHMgdGhlIFZNUmF5IFNhbmRib3ggQW5hbHl6ZXIgZnVuY3Rp
b24gdG8gZGV0ZXJtaW5lIGlmIHRoZSBmaWxlIGNvbnRhaW5zIG1hbHdhcmUuICBUaGUgYW5hbHlz
aXMgcmVzdWx0IGlzIHJldHVybmVkIGluIGFuIGluY2lkZW50IG5vdGUuPC9kb2N1bWVudGF0aW9u
PjxzdGFydEV2ZW50IGlkPVwiU3RhcnRFdmVudF8xNTVhc3htXCI+PG91dGdvaW5nPlNlcXVlbmNl
Rmxvd18xOG40aDhkPC9vdXRnb2luZz48L3N0YXJ0RXZlbnQ+PHNlcnZpY2VUYXNrIGlkPVwiU2Vy
dmljZVRhc2tfMTc2aThlNlwiIG5hbWU9XCJWTVJheSBTYW5kYm94IEFuYWx5emVyXCIgcmVzaWxp
ZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1bmN0
aW9uIHV1aWQ9XCIxYWE1YjY2OS1lNWQzLTQzNDEtYTVlNi05ZDhiNzBjMTcwNzlcIj57XCJpbnB1
dHNcIjp7XCJjYTdkZTFlMy1mZWU4LTQzYmUtYjE1MS1hNmM5ZGIwNjAyNDhcIjp7XCJpbnB1dF90
eXBlXCI6XCJzdGF0aWNcIixcInN0YXRpY19pbnB1dFwiOntcImJvb2xlYW5fdmFsdWVcIjpmYWxz
ZSxcIm11bHRpc2VsZWN0X3ZhbHVlXCI6W119fX0sXCJwb3N0X3Byb2Nlc3Npbmdfc2NyaXB0XCI6
XCJkZWYgIGZvbnRfY29sb3IodnRpX3Njb3JlLHNhbXBsZV9zZXZlcml0eSk6XFxuICBjb2xvciA9
IFxcXCJncmVlblxcXCJcXG4gIHRyeTpcXG4gICAgaWYgc2FtcGxlX3NldmVyaXR5IGluIFtcXFwi
bWFsaWNpb3VzXFxcIl0gb3IgaW50KHZ0aV9zY29yZSkgJmd0Oz0gNzU6XFxuICAgICAgY29sb3Ig
PSBcXFwicmVkXFxcIlxcbiAgICBlbGlmIHNhbXBsZV9zZXZlcml0eSBpbiBbXFxcImJsYWNrbGlz
dGVkXFxcIixcXFwic3VzcGljaW91c1xcXCJdIG9yIGludCh2dGlfc2NvcmUpICZndDs9IDUwOlxc
biAgICAgIGNvbG9yID0gXFxcInllbGxvd1xcXCJcXG4gIGV4Y2VwdDpcXG4gICAgICBwYXNzXFxu
ICByZXR1cm4gY29sb3JcXG5cXG5pZiBub3QgcmVzdWx0cy5hbmFseXNpc19yZXBvcnRfc3RhdHVz
OlxcbiBub3RlVGV4dCA9IHVcXFwiXFxcIlxcXCJTdWNjZXNzZnVsIHN1Ym1pdCAmbHQ7YiZndDt7
fSZsdDsvYiZndDsgdG8gVk1SYXkgQ2xvdWQgQW5hbHl6ZXIuIEhvd2V2ZXIgaXQgd2lsbCB0YWtl
IHRpbWUgdG8gZ2VuZXJhdGUgYW4gYW5hbHlzaXMgcmVwb3J0LCBwbGVhc2Ugc3VibWl0IGl0IGFn
YWluIGxhdGVyLiAmbHQ7YnImZ3Q7XFxcIlxcXCJcXFwiLmZvcm1hdChhcnRpZmFjdC52YWx1ZSlc
XG4gXFxuZWxzZTpcXG4gbm90ZVRleHQgPSB1XFxcIlxcXCJcXFwiU3VjY2Vzc2Z1bCBzdWJtaXQg
Jmx0O2ImZ3Q7e30mbHQ7L2ImZ3Q7IHRvIFZNUmF5IENsb3VkIEFuYWx5emVyLkNoZWNrIHRoZSBy
ZXN1bHRzIGJlbG93OiAmbHQ7YnImZ3Q7XFxcIlxcXCJcXFwiLmZvcm1hdChhcnRpZmFjdC52YWx1
ZSlcXG5cXG4gZm9yIHNhbXBsZSBpbiByZXN1bHRzLnNhbXBsZV9maW5hbF9yZXN1bHQ6XFxuICAg
bm90ZVRleHQgKz0gdVxcXCJcXFwiXFxcIi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t
LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXFxcIlxcXCJcXFwiXFxuICAg
Y29sb3IgPSBmb250X2NvbG9yKHNhbXBsZVtcXFwic2FtcGxlX3JlcG9ydFxcXCJdW1xcXCJzYW1w
bGVfc2NvcmVcXFwiXSxzYW1wbGVbXFxcInNhbXBsZV9yZXBvcnRcXFwiXVtcXFwic2FtcGxlX2xh
c3RfcmVwdXRhdGlvbl9zZXZlcml0eVxcXCJdKVxcbiAgIG5vdGVUZXh0ICs9IHVcXFwiXFxcIlxc
XCImbHQ7YnImZ3Q7Vk1SYXkgU2FuZGJveCBBbmFseXNpczogJmx0O2ImZ3Q7e3NhbXBsZV9maWxl
bmFtZX0mbHQ7L2ImZ3Q7IGNvbXBsZXRlLiZsdDticiZndDtcXG4gICAgICAgICAgICAgICAgICAg
Vk1SQVkgT25saW5lIEF0dGFjaG1lbnQ6ICZsdDthIGhyZWY9e3NhbXBsZV9vbmxpbmVfcmVwb3J0
fSZndDt7c2FtcGxlX29ubGluZV9yZXBvcnR9Jmx0Oy9hJmd0OyZsdDticiZndDtcXG4gICAgICAg
ICAgICAgICAgICAgVk1SYXkgQW5hbHl6ZXIgcmVzdWx0OiAgVlRJIFNjb3JlOiAmbHQ7YiBzdHls
ZT0gXFxcImNvbG9yOntjb2xvcn1cXFwiJmd0O3tzYW1wbGVfdnRpX3Njb3JlfSZsdDsvYiZndDss
ICBTZXZlcml0eTogJmx0O2Igc3R5bGU9IFxcXCJjb2xvcjp7Y29sb3J9XFxcIiZndDt7c2FtcGxl
X3NldmVyaXR5fSZsdDsvYiZndDsgJmx0O2JyJmd0O1xcbiAgICAgICAgICAgICAgIFxcXCJcXFwi
XFxcIi5mb3JtYXQoc2FtcGxlX2ZpbGVuYW1lPXNhbXBsZVtcXFwic2FtcGxlX3JlcG9ydFxcXCJd
W1xcXCJzYW1wbGVfZmlsZW5hbWVcXFwiXSxcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBz
YW1wbGVfb25saW5lX3JlcG9ydD1zYW1wbGVbXFxcInNhbXBsZV9yZXBvcnRcXFwiXVtcXFwic2Ft
cGxlX3dlYmlmX3VybFxcXCJdLFxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIGNvbG9yID0g
Y29sb3IsXFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgc2FtcGxlX3Z0aV9zY29yZSA9IHNh
bXBsZVtcXFwic2FtcGxlX3JlcG9ydFxcXCJdW1xcXCJzYW1wbGVfc2NvcmVcXFwiXSxcXG4gICAg
ICAgICAgICAgICAgICAgICAgICAgICBzYW1wbGVfc2V2ZXJpdHkgPSBzYW1wbGVbXFxcInNhbXBs
ZV9yZXBvcnRcXFwiXVtcXFwic2FtcGxlX2xhc3RfcmVwdXRhdGlvbl9zZXZlcml0eVxcXCJdKVxc
biBcXG4gICBub3RlVGV4dCArPSB1XFxcIlxcXCJcXFwiJmx0O2JyJmd0O3wgYW5hbHlzaXNfaWQg
fCBhbmFseXNpc19qb2Jfc3RhcnRlZCB8IGFuYWx5c2lzX3Z0aV9zY29yZSB8IGFuYWx5c2lzX3Nl
dmVyaXR5IHwmbHQ7YnImZ3Q7XFxcIlxcXCJcXFwiXFxuICAgXFxuICAgZm9yIGFuYWx5c2lzIGlu
IHNhbXBsZVtcXFwic2FtcGxlX2FuYWx5c2lzX3JlcG9ydFxcXCJdOlxcbiAgICAgY29sb3IgPSBm
b250X2NvbG9yKGFuYWx5c2lzW1xcXCJhbmFseXNpc192dGlfc2NvcmVcXFwiXSxhbmFseXNpc1tc
XFwiYW5hbHlzaXNfc2V2ZXJpdHlcXFwiXSlcXG4gICAgIG5vdGVUZXh0ICs9IHVcXFwiXFxcIlxc
XCJ8ICZsdDthIGhyZWY9e2FuYWx5c2lzX2xpbmt9Jmd0OyAge2FuYWx5c2lzX2lkfSAmbHQ7L2Em
Z3Q7IHwge2FuYWx5c2lzX2pvYl9zdGFydGVkfSB8ICAmbHQ7YiBzdHlsZT0gXFxcImNvbG9yOntj
b2xvcn1cXFwiJmd0OyB7YW5hbHlzaXNfdnRpX3Njb3JlfSZsdDsvYiZndDsgIHwgJmx0O2Igc3R5
bGU9IFxcXCJjb2xvcjp7Y29sb3J9XFxcIiZndDt7YW5hbHlzaXNfc2V2ZXJpdHl9Jmx0Oy9iJmd0
OyB8Jmx0O2JyJmd0O1xcbiAgICAgICAgICAgICAgICAgXFxcIlxcXCJcXFwiLmZvcm1hdChhbmFs
eXNpc19saW5rPWFuYWx5c2lzW1xcXCJhbmFseXNpc193ZWJpZl91cmxcXFwiXSxcXG4gICAgICAg
ICAgICAgICAgICAgICAgICAgICBhbmFseXNpc19pZD1hbmFseXNpc1tcXFwiYW5hbHlzaXNfaWRc
XFwiXSxcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBhbmFseXNpc19qb2Jfc3RhcnRlZD1h
bmFseXNpc1tcXFwiYW5hbHlzaXNfam9iX3N0YXJ0ZWRcXFwiXSxcXG4gICAgICAgICAgICAgICAg
ICAgICAgICAgICBhbmFseXNpc192dGlfc2NvcmU9YW5hbHlzaXNbXFxcImFuYWx5c2lzX3Z0aV9z
Y29yZVxcXCJdLFxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIGFuYWx5c2lzX3NldmVyaXR5
PWFuYWx5c2lzW1xcXCJhbmFseXNpc19zZXZlcml0eVxcXCJdLFxcbiAgICAgICAgICAgICAgICAg
ICAgICAgICAgIGNvbG9yPWNvbG9yKVxcbiBcXG4gICByZXB1dGF0aW9ucyA9IFtzdHIocmVwdXRh
dGlvbltcXFwicmVwdXRhdGlvbl9sb29rdXBfc2V2ZXJpdHlcXFwiXSkgZm9yIHJlcHV0YXRpb24g
aW4gc2FtcGxlW1xcXCJzYW1wbGVfcmVwdXRhdGlvbl9yZXBvcnRcXFwiXV1cXG4gICBcXG4gICBp
ZiBcXFwibWFsaWNpb3VzXFxcIiBpbiByZXB1dGF0aW9uczpcXG4gICAgIGNvbG9yID0gXFxcInJl
ZFxcXCJcXG4gICAgIHJlcHV0YXRpb25fbG9va3VwX3NldmVyaXR5ID0gXFxcIm1hbGljaW91c1xc
XCJcXG4gICBlbGlmIFxcXCJzdXNwaWNpb3VzXFxcIiBpbiByZXB1dGF0aW9uczpcXG4gICAgIGNv
bG9yID0gXFxcInllbGxvd1xcXCJcXG4gICAgIHJlcHV0YXRpb25fbG9va3VwX3NldmVyaXR5ID0g
XFxcInN1c3BpY2lvdXNcXFwiXFxuICAgZWxpZiBcXFwiYmxhY2tsaXN0ZWRcXFwiIGluIHJlcHV0
YXRpb25zOlxcbiAgICAgY29sb3IgPSBcXFwieWVsbG93XFxcIlxcbiAgICAgcmVwdXRhdGlvbl9s
b29rdXBfc2V2ZXJpdHkgPSBcXFwiYmxhY2tsaXN0ZWRcXFwiXFxuICAgZWxpZiBcXFwibm90X3N1
c3BpY2lvdXNcXFwiIGluIHJlcHV0YXRpb25zOlxcbiAgICAgY29sb3IgPSBcXFwiZ3JlZW5cXFwi
XFxuICAgICByZXB1dGF0aW9uX2xvb2t1cF9zZXZlcml0eSA9IFxcXCJub3Rfc3VzcGljaW91c1xc
XCJcXG4gICBlbGlmIFxcXCJ3aGl0ZWxpc3RlZFxcXCIgaW4gcmVwdXRhdGlvbnM6XFxuICAgICBj
b2xvciA9IFxcXCJncmVlblxcXCJcXG4gICAgIHJlcHV0YXRpb25fbG9va3VwX3NldmVyaXR5ID0g
XFxcIndoaXRlbGlzdGVkXFxcIlxcbiAgIGVsc2U6XFxuICAgICBjb2xvciA9IFxcXCJncmVlblxc
XCJcXG4gICAgIHJlcHV0YXRpb25fbG9va3VwX3NldmVyaXR5ID0gXFxcInVua25vd25cXFwiXFxu
ICAgICBcXG4gICBub3RlVGV4dCArPSB1XFxcIlxcXCJcXFwiUmVwdXRhdGlvbiBsb29rdXAgcmVz
dWx0OiAgJmx0O2Igc3R5bGU9IFxcXCJjb2xvcjp7Y29sb3J9XFxcIiZndDt7cmVwdXRhdGlvbl9s
b29rdXBfc2V2ZXJpdHl9ICZsdDsvYiZndDsgJmx0O2JyJmd0O1xcXCJcXFwiXFxcIi5mb3JtYXQo
Y29sb3I9Y29sb3IsIHJlcHV0YXRpb25fbG9va3VwX3NldmVyaXR5PXJlcHV0YXRpb25fbG9va3Vw
X3NldmVyaXR5KVxcbiAgIFxcbmluY2lkZW50LmFkZE5vdGUoaGVscGVyLmNyZWF0ZVJpY2hUZXh0
KG5vdGVUZXh0KSlcXG5cXG5cIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiaW5wdXRzLmlu
Y2lkZW50X2lkID0gaW5jaWRlbnQuaWRcXG5pbnB1dHMuYXJ0aWZhY3RfaWQgPSBhcnRpZmFjdC5p
ZFwiLFwicmVzdWx0X25hbWVcIjpcIlwifTwvcmVzaWxpZW50OmZ1bmN0aW9uPjwvZXh0ZW5zaW9u
RWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18xOG40aDhkPC9pbmNvbWluZz48b3V0Z29p
bmc+U2VxdWVuY2VGbG93XzA2OGtvNjM8L291dGdvaW5nPjwvc2VydmljZVRhc2s+PHNlcXVlbmNl
RmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xOG40aDhkXCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8x
NTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMTc2aThlNlwiLz48ZW5kRXZlbnQgaWQ9
XCJFbmRFdmVudF8wZGh0OWVsXCI+PGluY29taW5nPlNlcXVlbmNlRmxvd18wNjhrbzYzPC9pbmNv
bWluZz48L2VuZEV2ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMDY4a282M1wi
IHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzE3Nmk4ZTZcIiB0YXJnZXRSZWY9XCJFbmRFdmVudF8w
ZGh0OWVsXCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIj48
dGV4dD5TdGFydCB5b3VyIHdvcmtmbG93IGhlcmU8L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNz
b2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgc291cmNlUmVmPVwiU3RhcnRFdmVu
dF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiLz48dGV4dEFu
bm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8wejkwMGlvXCI+PHRleHQ+UmVzdWx0IGlzIGlu
Y2lkZW50IG5vdGUgaXMgY3JlYXRlZCBjb250YWluaW5nIHRoZSByZXN1bHRzIG9mIGFuYWx5c2lz
PC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXN4
enA1clwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzE3Nmk4ZTZcIiB0YXJnZXRSZWY9XCJUZXh0
QW5ub3RhdGlvbl8wejkwMGlvXCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5vdGF0aW9u
XzF4eXlyaG5cIj48dGV4dD48IVtDREFUQVtpbnB1dHM6XG4xLiBpbmNpZGVudF9pZCAocmVxdWly
ZWQpXG4yLiBhcnRpZmFjdF9pZFxuMy4gYW5hbHlzaXNfcmVwb3J0X3N0YXR1cyhcIk5vXCIgYnkg
ZGVmYXVsdCk6IFwiWWVzXCIgZm9yIGFuYWx5c2lzIGhhcyBmaW5pc2hlZCwgXCJOb1wiIGZvciBh
bmFseXNpcyBoYXMgbm90IGNvbXBsZXRlZCB5ZXQuXV0+PC90ZXh0PjwvdGV4dEFubm90YXRpb24+
PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMTFsdHB5NlwiIHNvdXJjZVJlZj1cIlNlcnZp
Y2VUYXNrXzE3Nmk4ZTZcIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8xeHl5cmhuXCIvPjwv
cHJvY2Vzcz48YnBtbmRpOkJQTU5EaWFncmFtIGlkPVwiQlBNTkRpYWdyYW1fMVwiPjxicG1uZGk6
QlBNTlBsYW5lIGJwbW5FbGVtZW50PVwidW5kZWZpbmVkXCIgaWQ9XCJCUE1OUGxhbmVfMVwiPjxi
cG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU3RhcnRFdmVudF8xNTVhc3htXCIgaWQ9XCJT
dGFydEV2ZW50XzE1NWFzeG1fZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9
XCIzNlwiIHg9XCIyNzdcIiB5PVwiMTk5XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3Vu
ZHMgaGVpZ2h0PVwiMFwiIHdpZHRoPVwiOTBcIiB4PVwiMjcyXCIgeT1cIjIzNFwiLz48L2JwbW5k
aTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVt
ZW50PVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5
dF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjEwMFwiIHg9XCI3NFwi
IHk9XCIyNzNcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1l
bnQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4X2RpXCI+
PG9tZ2RpOndheXBvaW50IHg9XCIyNzhcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIy
MlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjE1N1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5
PVwiMjczXCIvPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50
PVwiU2VydmljZVRhc2tfMTc2aThlNlwiIGlkPVwiU2VydmljZVRhc2tfMTc2aThlNl9kaVwiPjxv
bWdkYzpCb3VuZHMgaGVpZ2h0PVwiODBcIiB3aWR0aD1cIjEwMFwiIHg9XCI0MTFcIiB5PVwiMTc3
XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2Vx
dWVuY2VGbG93XzE4bjRoOGRcIiBpZD1cIlNlcXVlbmNlRmxvd18xOG40aDhkX2RpXCI+PG9tZ2Rp
OndheXBvaW50IHg9XCIzMTNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIxN1wiLz48
b21nZGk6d2F5cG9pbnQgeD1cIjQxMVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjE3
XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1c
IjkwXCIgeD1cIjMxN1wiIHk9XCIxOTUuNVwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6
QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJFbmRFdmVudF8wZGh0OWVs
XCIgaWQ9XCJFbmRFdmVudF8wZGh0OWVsX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwi
IHdpZHRoPVwiMzZcIiB4PVwiNzM2XCIgeT1cIjE5OVwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21n
ZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCI5MFwiIHg9XCI3MDlcIiB5PVwiMjM4XCIv
PjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBi
cG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18wNjhrbzYzXCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMDY4
a282M19kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiNTExXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2lu
dFwiIHk9XCIyMTdcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI3MzZcIiB4c2k6dHlwZT1cIm9tZ2Rj
OlBvaW50XCIgeT1cIjIxN1wiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdo
dD1cIjEzXCIgd2lkdGg9XCI5MFwiIHg9XCI1NzguNVwiIHk9XCIxOTUuNVwiLz48L2JwbW5kaTpC
UE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9
XCJUZXh0QW5ub3RhdGlvbl8wejkwMGlvXCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8wejkwMGlvX2Rp
XCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI1MVwiIHdpZHRoPVwiNDIzXCIgeD1cIjQ2MlwiIHk9
XCIxOVwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1c
IkFzc29jaWF0aW9uXzFzeHpwNXJcIiBpZD1cIkFzc29jaWF0aW9uXzFzeHpwNXJfZGlcIj48b21n
ZGk6d2F5cG9pbnQgeD1cIjUwNlwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTgyXCIv
PjxvbWdkaTp3YXlwb2ludCB4PVwiNjQzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCI3
MFwiLz48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRl
eHRBbm5vdGF0aW9uXzF4eXlyaG5cIiBpZD1cIlRleHRBbm5vdGF0aW9uXzF4eXlyaG5fZGlcIj48
b21nZGM6Qm91bmRzIGhlaWdodD1cIjEwOFwiIHdpZHRoPVwiMzU1XCIgeD1cIjEwXCIgeT1cIjE4
XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNz
b2NpYXRpb25fMTFsdHB5NlwiIGlkPVwiQXNzb2NpYXRpb25fMTFsdHB5Nl9kaVwiPjxvbWdkaTp3
YXlwb2ludCB4PVwiNDExXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIxODlcIi8+PG9t
Z2RpOndheXBvaW50IHg9XCIyODlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjEyNlwi
Lz48L2JwbW5kaTpCUE1ORWRnZT48L2JwbW5kaTpCUE1OUGxhbmU+PC9icG1uZGk6QlBNTkRpYWdy
YW0+PC9kZWZpbml0aW9ucz4ifSwgImNvbnRlbnRfdmVyc2lvbiI6IDEsICJjcmVhdG9yX2lkIjog
ImFAYS5jb20iLCAiZGVzY3JpcHRpb24iOiAiVGhpcyB3b3JrZmxvdyB0YWtlcyBhbiBhcnRpZmFj
dCBmaWxlIGFzIGlucHV0IGFuZCBjYWxscyB0aGUgVk1SYXkgU2FuZGJveCBBbmFseXplciBmdW5j
dGlvbiB0byBkZXRlcm1pbmUgaWYgdGhlIGZpbGUgY29udGFpbnMgbWFsd2FyZS4gIFRoZSBhbmFs
eXNpcyByZXN1bHQgaXMgcmV0dXJuZWQgaW4gYW4gaW5jaWRlbnQgbm90ZS4iLCAiZXhwb3J0X2tl
eSI6ICJleGFtcGxlX3ZtcmF5X3NhbmRib3hfYW5hbHl6ZXJfYXJ0aWZhY3QiLCAibGFzdF9tb2Rp
ZmllZF9ieSI6ICJhQGEuY29tIiwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE1OTk4MzE5Njk2MTQs
ICJuYW1lIjogIkV4YW1wbGU6IFZNUkFZIFNhbmRib3ggQW5hbHl6ZXIgW0FydGlmYWN0XSIsICJv
YmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJleGFtcGxlX3Zt
cmF5X3NhbmRib3hfYW5hbHl6ZXJfYXJ0aWZhY3QiLCAidGFncyI6IFtdLCAidXVpZCI6ICI0YWQ3
OWViYS1hZjBkLTQ1ZmMtOGI4MS01MDgxNTQ0ODllYjgiLCAid29ya2Zsb3dfaWQiOiAzN30sIHsi
YWN0aW9ucyI6IFtdLCAiY29udGVudCI6IHsidmVyc2lvbiI6IDEsICJ3b3JrZmxvd19pZCI6ICJl
eGFtcGxlX3ZtcmF5X3NhbmRib3hfYW5hbHl6ZXJfYXR0YWNobWVudCIsICJ4bWwiOiAiPD94bWwg
dmVyc2lvbj1cIjEuMFwiIGVuY29kaW5nPVwiVVRGLThcIj8+PGRlZmluaXRpb25zIHhtbG5zPVwi
aHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9NT0RFTFwiIHhtbG5zOmJwbW5k
aT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvRElcIiB4bWxuczpvbWdk
Yz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RDXCIgeG1sbnM6b21nZGk9
XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9ESVwiIHhtbG5zOnJlc2lsaWVu
dD1cImh0dHA6Ly9yZXNpbGllbnQuaWJtLmNvbS9icG1uXCIgeG1sbnM6eHNkPVwiaHR0cDovL3d3
dy53My5vcmcvMjAwMS9YTUxTY2hlbWFcIiB4bWxuczp4c2k9XCJodHRwOi8vd3d3LnczLm9yZy8y
MDAxL1hNTFNjaGVtYS1pbnN0YW5jZVwiIHRhcmdldE5hbWVzcGFjZT1cImh0dHA6Ly93d3cuY2Ft
dW5kYS5vcmcvdGVzdFwiPjxwcm9jZXNzIGlkPVwiZXhhbXBsZV92bXJheV9zYW5kYm94X2FuYWx5
emVyX2F0dGFjaG1lbnRcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1wbGU6IFZN
UmF5IFNhbmRib3ggQW5hbHl6ZXIgW0F0dGFjaG1lbnRdXCI+PGRvY3VtZW50YXRpb24+VGhpcyB3
b3JrZmxvdyB0YWtlcyBhbiBhdHRhY2htZW50IGZpbGUgYXMgaW5wdXQgYW5kIGNhbGxzIHRoZSBW
TVJheSBTYW5kYm94IEFuYWx5emVyIGZ1bmN0aW9uIHRvIGRldGVybWluZSBpZiB0aGUgZmlsZSBj
b250YWlucyBtYWx3YXJlLiAgVGhlIGFuYWx5c2lzIHJlc3VsdCBpcyByZXR1cm5lZCBpbiBhbiBp
bmNpZGVudCBub3RlLjwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZlbnRf
MTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMTc2bHYzajwvb3V0Z29pbmc+PC9zdGFy
dEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzFmd3UyN2lcIiBuYW1lPVwiVk1S
YXkgU2FuZGJveCBBbmFseXplclwiIHJlc2lsaWVudDp0eXBlPVwiZnVuY3Rpb25cIj48ZXh0ZW5z
aW9uRWxlbWVudHM+PHJlc2lsaWVudDpmdW5jdGlvbiB1dWlkPVwiMWFhNWI2NjktZTVkMy00MzQx
LWE1ZTYtOWQ4YjcwYzE3MDc5XCI+e1wiaW5wdXRzXCI6e1wiY2E3ZGUxZTMtZmVlOC00M2JlLWIx
NTEtYTZjOWRiMDYwMjQ4XCI6e1wiaW5wdXRfdHlwZVwiOlwic3RhdGljXCIsXCJzdGF0aWNfaW5w
dXRcIjp7XCJib29sZWFuX3ZhbHVlXCI6ZmFsc2UsXCJtdWx0aXNlbGVjdF92YWx1ZVwiOltdfX19
LFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiZGVmICBmb250X2NvbG9yKHZ0aV9zY29yZSxz
YW1wbGVfc2V2ZXJpdHkpOlxcbiAgY29sb3IgPSBcXFwiZ3JlZW5cXFwiXFxuICB0cnk6XFxuICAg
IGlmIHNhbXBsZV9zZXZlcml0eSBpbiBbXFxcIm1hbGljaW91c1xcXCJdIG9yIGludCh2dGlfc2Nv
cmUpICZndDs9IDc1OlxcbiAgICAgIGNvbG9yID0gXFxcInJlZFxcXCJcXG4gICAgZWxpZiBzYW1w
bGVfc2V2ZXJpdHkgaW4gW1xcXCJibGFja2xpc3RlZFxcXCIsXFxcInN1c3BpY2lvdXNcXFwiXSBv
ciBpbnQodnRpX3Njb3JlKSAmZ3Q7PSA1MDpcXG4gICAgICBjb2xvciA9IFxcXCJ5ZWxsb3dcXFwi
XFxuICBleGNlcHQ6XFxuICAgICAgcGFzc1xcbiAgcmV0dXJuIGNvbG9yXFxuXFxuaWYgbm90IHJl
c3VsdHMuYW5hbHlzaXNfcmVwb3J0X3N0YXR1czpcXG4gbm90ZVRleHQgPSB1XFxcIlxcXCJcXFwi
U3VjY2Vzc2Z1bCBzdWJtaXQgJmx0O2ImZ3Q7e30mbHQ7L2ImZ3Q7IHRvIFZNUmF5IENsb3VkIEFu
YWx5emVyLkhvd2V2ZXIgaXQgd2lsbCB0YWtlIHRpbWUgdG8gZ2VuZXJhdGUgYW4gYW5hbHlzaXMg
cmVwb3J0LCBwbGVhc2Ugc3VibWl0IGl0IGFnYWluIGxhdGVyLiAmbHQ7YnImZ3Q7XFxcIlxcXCJc
XFwiLmZvcm1hdChhdHRhY2htZW50Lm5hbWUpXFxuIFxcbmVsc2U6XFxuIG5vdGVUZXh0ID0gdVxc
XCJcXFwiXFxcIlN1Y2Nlc3NmdWwgc3VibWl0ICZsdDtiJmd0O3t9Jmx0Oy9iJmd0OyB0byBWTVJh
eSBBbmFseXplci5DaGVjayB0aGUgcmVzdWx0cyBiZWxvdzogJmx0O2JyJmd0O1xcXCJcXFwiXFxc
Ii5mb3JtYXQoYXR0YWNobWVudC5uYW1lKVxcbiBcXG4gZm9yIHNhbXBsZSBpbiByZXN1bHRzLnNh
bXBsZV9maW5hbF9yZXN1bHQ6XFxuICAgbm90ZVRleHQgKz0gdVxcXCJcXFwiXFxcIi0tLS0tLS0t
LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t
LS0tLS0tXFxcIlxcXCJcXFwiXFxuICAgY29sb3IgPSBmb250X2NvbG9yKHNhbXBsZVtcXFwic2Ft
cGxlX3JlcG9ydFxcXCJdW1xcXCJzYW1wbGVfc2NvcmVcXFwiXSxzYW1wbGVbXFxcInNhbXBsZV9y
ZXBvcnRcXFwiXVtcXFwic2FtcGxlX2xhc3RfcmVwdXRhdGlvbl9zZXZlcml0eVxcXCJdKVxcbiAg
IG5vdGVUZXh0ICs9IHVcXFwiXFxcIlxcXCImbHQ7YnImZ3Q7Vk1SYXkgU2FuZGJveCBBbmFseXNp
czogJmx0O2ImZ3Q7e3NhbXBsZV9maWxlbmFtZX0mbHQ7L2ImZ3Q7IGNvbXBsZXRlLiZsdDticiZn
dDtcXG4gICAgICAgICAgICAgICAgICAgVk1SQVkgT25saW5lIEF0dGFjaG1lbnQ6ICZsdDthIGhy
ZWY9e3NhbXBsZV9vbmxpbmVfcmVwb3J0fSZndDt7c2FtcGxlX29ubGluZV9yZXBvcnR9Jmx0Oy9h
Jmd0OyZsdDticiZndDtcXG4gICAgICAgICAgICAgICAgICAgVk1SYXkgQW5hbHl6ZXIgcmVzdWx0
OiAgVlRJIFNjb3JlOiAmbHQ7YiBzdHlsZT0gXFxcImNvbG9yOntjb2xvcn1cXFwiJmd0O3tzYW1w
bGVfdnRpX3Njb3JlfSZsdDsvYiZndDssICBTZXZlcml0eTogJmx0O2Igc3R5bGU9IFxcXCJjb2xv
cjp7Y29sb3J9XFxcIiZndDt7c2FtcGxlX3NldmVyaXR5fSZsdDsvYiZndDsgJmx0O2JyJmd0O1xc
biAgICAgICAgICAgICAgIFxcXCJcXFwiXFxcIi5mb3JtYXQoc2FtcGxlX2ZpbGVuYW1lPXNhbXBs
ZVtcXFwic2FtcGxlX3JlcG9ydFxcXCJdW1xcXCJzYW1wbGVfZmlsZW5hbWVcXFwiXSxcXG4gICAg
ICAgICAgICAgICAgICAgICAgICAgICBzYW1wbGVfb25saW5lX3JlcG9ydD1zYW1wbGVbXFxcInNh
bXBsZV9yZXBvcnRcXFwiXVtcXFwic2FtcGxlX3dlYmlmX3VybFxcXCJdLFxcbiAgICAgICAgICAg
ICAgICAgICAgICAgICAgIGNvbG9yID0gY29sb3IsXFxuICAgICAgICAgICAgICAgICAgICAgICAg
ICAgc2FtcGxlX3Z0aV9zY29yZSA9IHNhbXBsZVtcXFwic2FtcGxlX3JlcG9ydFxcXCJdW1xcXCJz
YW1wbGVfc2NvcmVcXFwiXSxcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBzYW1wbGVfc2V2
ZXJpdHkgPSBzYW1wbGVbXFxcInNhbXBsZV9yZXBvcnRcXFwiXVtcXFwic2FtcGxlX2xhc3RfcmVw
dXRhdGlvbl9zZXZlcml0eVxcXCJdKVxcbiBcXG4gICBub3RlVGV4dCArPSB1XFxcIlxcXCJcXFwi
Jmx0O2JyJmd0O3wgYW5hbHlzaXNfaWQgfCBhbmFseXNpc19qb2Jfc3RhcnRlZCB8IGFuYWx5c2lz
X3Z0aV9zY29yZSB8IGFuYWx5c2lzX3NldmVyaXR5IHwmbHQ7YnImZ3Q7XFxcIlxcXCJcXFwiXFxu
ICAgXFxuICAgZm9yIGFuYWx5c2lzIGluIHNhbXBsZVtcXFwic2FtcGxlX2FuYWx5c2lzX3JlcG9y
dFxcXCJdOlxcbiAgICAgY29sb3IgPSBmb250X2NvbG9yKGFuYWx5c2lzW1xcXCJhbmFseXNpc192
dGlfc2NvcmVcXFwiXSxhbmFseXNpc1tcXFwiYW5hbHlzaXNfc2V2ZXJpdHlcXFwiXSlcXG4gICAg
IG5vdGVUZXh0ICs9IHVcXFwiXFxcIlxcXCJ8ICZsdDthIGhyZWY9e2FuYWx5c2lzX2xpbmt9Jmd0
OyAge2FuYWx5c2lzX2lkfSAmbHQ7L2EmZ3Q7IHwge2FuYWx5c2lzX2pvYl9zdGFydGVkfSB8ICAm
bHQ7YiBzdHlsZT0gXFxcImNvbG9yOntjb2xvcn1cXFwiJmd0OyB7YW5hbHlzaXNfdnRpX3Njb3Jl
fSZsdDsvYiZndDsgIHwgJmx0O2Igc3R5bGU9IFxcXCJjb2xvcjp7Y29sb3J9XFxcIiZndDt7YW5h
bHlzaXNfc2V2ZXJpdHl9Jmx0Oy9iJmd0OyB8Jmx0O2JyJmd0O1xcbiAgICAgICAgICAgICAgICAg
XFxcIlxcXCJcXFwiLmZvcm1hdChhbmFseXNpc19saW5rPWFuYWx5c2lzW1xcXCJhbmFseXNpc193
ZWJpZl91cmxcXFwiXSxcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBhbmFseXNpc19pZD1h
bmFseXNpc1tcXFwiYW5hbHlzaXNfaWRcXFwiXSxcXG4gICAgICAgICAgICAgICAgICAgICAgICAg
ICBhbmFseXNpc19qb2Jfc3RhcnRlZD1hbmFseXNpc1tcXFwiYW5hbHlzaXNfam9iX3N0YXJ0ZWRc
XFwiXSxcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBhbmFseXNpc192dGlfc2NvcmU9YW5h
bHlzaXNbXFxcImFuYWx5c2lzX3Z0aV9zY29yZVxcXCJdLFxcbiAgICAgICAgICAgICAgICAgICAg
ICAgICAgIGFuYWx5c2lzX3NldmVyaXR5PWFuYWx5c2lzW1xcXCJhbmFseXNpc19zZXZlcml0eVxc
XCJdLFxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIGNvbG9yPWNvbG9yKVxcbiBcXG4gICBy
ZXB1dGF0aW9ucyA9IFtzdHIocmVwdXRhdGlvbltcXFwicmVwdXRhdGlvbl9sb29rdXBfc2V2ZXJp
dHlcXFwiXSkgZm9yIHJlcHV0YXRpb24gaW4gc2FtcGxlW1xcXCJzYW1wbGVfcmVwdXRhdGlvbl9y
ZXBvcnRcXFwiXV1cXG4gICBcXG4gICBpZiBcXFwibWFsaWNpb3VzXFxcIiBpbiByZXB1dGF0aW9u
czpcXG4gICAgIGNvbG9yID0gXFxcInJlZFxcXCJcXG4gICAgIHJlcHV0YXRpb25fbG9va3VwX3Nl
dmVyaXR5ID0gXFxcIm1hbGljaW91c1xcXCJcXG4gICBlbGlmIFxcXCJzdXNwaWNpb3VzXFxcIiBp
biByZXB1dGF0aW9uczpcXG4gICAgIGNvbG9yID0gXFxcInllbGxvd1xcXCJcXG4gICAgIHJlcHV0
YXRpb25fbG9va3VwX3NldmVyaXR5ID0gXFxcInN1c3BpY2lvdXNcXFwiXFxuICAgZWxpZiBcXFwi
YmxhY2tsaXN0ZWRcXFwiIGluIHJlcHV0YXRpb25zOlxcbiAgICAgY29sb3IgPSBcXFwieWVsbG93
XFxcIlxcbiAgICAgcmVwdXRhdGlvbl9sb29rdXBfc2V2ZXJpdHkgPSBcXFwiYmxhY2tsaXN0ZWRc
XFwiXFxuICAgZWxpZiBcXFwibm90X3N1c3BpY2lvdXNcXFwiIGluIHJlcHV0YXRpb25zOlxcbiAg
ICAgY29sb3IgPSBcXFwiZ3JlZW5cXFwiXFxuICAgICByZXB1dGF0aW9uX2xvb2t1cF9zZXZlcml0
eSA9IFxcXCJub3Rfc3VzcGljaW91c1xcXCJcXG4gICBlbGlmIFxcXCJ3aGl0ZWxpc3RlZFxcXCIg
aW4gcmVwdXRhdGlvbnM6XFxuICAgICBjb2xvciA9IFxcXCJncmVlblxcXCJcXG4gICAgIHJlcHV0
YXRpb25fbG9va3VwX3NldmVyaXR5ID0gXFxcIndoaXRlbGlzdGVkXFxcIlxcbiAgIGVsc2U6XFxu
ICAgICBjb2xvciA9IFxcXCJncmVlblxcXCJcXG4gICAgIHJlcHV0YXRpb25fbG9va3VwX3NldmVy
aXR5ID0gXFxcInVua25vd25cXFwiXFxuICAgICBcXG4gICBub3RlVGV4dCArPSB1XFxcIlxcXCJc
XFwiUmVwdXRhdGlvbiBsb29rdXAgcmVzdWx0OiAgJmx0O2Igc3R5bGU9IFxcXCJjb2xvcjp7Y29s
b3J9XFxcIiZndDt7cmVwdXRhdGlvbl9sb29rdXBfc2V2ZXJpdHl9ICZsdDsvYiZndDsgJmx0O2Jy
Jmd0O1xcXCJcXFwiXFxcIi5mb3JtYXQoY29sb3I9Y29sb3IsIHJlcHV0YXRpb25fbG9va3VwX3Nl
dmVyaXR5PXJlcHV0YXRpb25fbG9va3VwX3NldmVyaXR5KVxcbiAgIFxcbmluY2lkZW50LmFkZE5v
dGUoaGVscGVyLmNyZWF0ZVJpY2hUZXh0KG5vdGVUZXh0KSlcXG5cXG5cIixcInByZV9wcm9jZXNz
aW5nX3NjcmlwdFwiOlwiaW5wdXRzLmluY2lkZW50X2lkID0gaW5jaWRlbnQuaWRcXG5pbnB1dHMu
YXR0YWNobWVudF9pZCA9IGF0dGFjaG1lbnQuaWRcXG5cIixcInJlc3VsdF9uYW1lXCI6XCJcIn08
L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5j
ZUZsb3dfMTc2bHYzajwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18xbGpmYzNyPC9v
dXRnb2luZz48L3NlcnZpY2VUYXNrPjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMTc2
bHYzalwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZp
Y2VUYXNrXzFmd3UyN2lcIi8+PGVuZEV2ZW50IGlkPVwiRW5kRXZlbnRfMGVvaHhkNlwiPjxpbmNv
bWluZz5TZXF1ZW5jZUZsb3dfMWxqZmMzcjwvaW5jb21pbmc+PC9lbmRFdmVudD48c2VxdWVuY2VG
bG93IGlkPVwiU2VxdWVuY2VGbG93XzFsamZjM3JcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18x
Znd1MjdpXCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMGVvaHhkNlwiLz48dGV4dEFubm90YXRpb24g
aWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+U3RhcnQgeW91ciB3b3JrZmxvdyBo
ZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25f
MXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlRl
eHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRp
b25fMGV3ajFyZFwiPjx0ZXh0PlJlc3VsdCBpcyBpbmNpZGVudCBub3RlIGlzIGNyZWF0ZWQgY29u
dGFpbmluZyB0aGUgcmVzdWx0cyBvZiBhbmFseXNpczwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxh
c3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzAxNWs5ZGdcIiBzb3VyY2VSZWY9XCJTZXJ2aWNl
VGFza18xZnd1MjdpXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25fMGV3ajFyZFwiLz48dGV4
dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8wbzc0MXNlXCI+PHRleHQ+PCFbQ0RBVEFb
aW5wdXRzOlxuMS4gaW5jaWRlbnRfaWQgKHJlcXVpcmVkKVxuMi4gYXR0YWNobWVudF9pZFxuMy4g
YW5hbHlzaXNfcmVwb3J0X3N0YXR1cyhcIk5vXCIgYnkgZGVmYXVsdCk6XHUwMGEwXCJZZXNcIiBm
b3IgYW5hbHlzaXMgaGFzIGZpbmlzaGVkLCBcIk5vXCIgZm9yIGFuYWx5c2lzIGhhcyBub3QgY29t
cGxldGVkIHlldC5dXT48L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJB
c3NvY2lhdGlvbl8xOG1reHllXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMWZ3dTI3aVwiIHRh
cmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzBvNzQxc2VcIi8+PC9wcm9jZXNzPjxicG1uZGk6QlBN
TkRpYWdyYW0gaWQ9XCJCUE1ORGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1OUGxhbmUgYnBtbkVsZW1l
bnQ9XCJ1bmRlZmluZWRcIiBpZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5kaTpCUE1OU2hhcGUgYnBt
bkVsZW1lbnQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bV9k
aVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjM0MlwiIHk9
XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIwXCIgd2lk
dGg9XCI5MFwiIHg9XCIzMzdcIiB5PVwiMjIzXCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5k
aTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlv
bl8xa3h4aXl0XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0X2RpXCI+PG9tZ2RjOkJvdW5k
cyBoZWlnaHQ9XCIzMFwiIHdpZHRoPVwiMTAwXCIgeD1cIjIzOFwiIHk9XCIyNjFcIi8+PC9icG1u
ZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8x
c2V1ajQ4XCIgaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9
XCIzNDdcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIxOFwiLz48b21nZGk6d2F5cG9p
bnQgeD1cIjMwM1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjYxXCIvPjwvYnBtbmRp
OkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU2VydmljZVRhc2tfMWZ3
dTI3aVwiIGlkPVwiU2VydmljZVRhc2tfMWZ3dTI3aV9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0
PVwiODBcIiB3aWR0aD1cIjEwMFwiIHg9XCI0OTFcIiB5PVwiMTY2XCIvPjwvYnBtbmRpOkJQTU5T
aGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzE3Nmx2M2pc
IiBpZD1cIlNlcXVlbmNlRmxvd18xNzZsdjNqX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIzNzhc
IiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1c
IjQ5MVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxh
YmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjkwXCIgeD1cIjM4OS41XCIg
eT1cIjE4NC41XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRp
OkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIkVuZEV2ZW50XzBlb2h4ZDZcIiBpZD1cIkVuZEV2ZW50
XzBlb2h4ZDZfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9
XCI2OTNcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0
PVwiMTNcIiB3aWR0aD1cIjkwXCIgeD1cIjY2NlwiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxh
YmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2Vx
dWVuY2VGbG93XzFsamZjM3JcIiBpZD1cIlNlcXVlbmNlRmxvd18xbGpmYzNyX2RpXCI+PG9tZ2Rp
OndheXBvaW50IHg9XCI1OTFcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48
b21nZGk6d2F5cG9pbnQgeD1cIjY5M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2
XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1c
IjkwXCIgeD1cIjU5N1wiIHk9XCIxODQuNVwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6
QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8w
ZXdqMXJkXCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8wZXdqMXJkX2RpXCI+PG9tZ2RjOkJvdW5kcyBo
ZWlnaHQ9XCI0NlwiIHdpZHRoPVwiNDMwXCIgeD1cIjU1N1wiIHk9XCI0M1wiLz48L2JwbW5kaTpC
UE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzAxNWs5
ZGdcIiBpZD1cIkFzc29jaWF0aW9uXzAxNWs5ZGdfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjU5
MFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTc1XCIvPjxvbWdkaTp3YXlwb2ludCB4
PVwiNzM0XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCI4OVwiLz48L2JwbW5kaTpCUE1O
RWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzBvNzQx
c2VcIiBpZD1cIlRleHRBbm5vdGF0aW9uXzBvNzQxc2VfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdo
dD1cIjk3XCIgd2lkdGg9XCIzNDBcIiB4PVwiMTgyXCIgeT1cIjEzXCIvPjwvYnBtbmRpOkJQTU5T
aGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMThta3h5ZVwi
IGlkPVwiQXNzb2NpYXRpb25fMThta3h5ZV9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiNDk2XCIg
eHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIxNzFcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI0
MTdcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjExMFwiLz48L2JwbW5kaTpCUE1ORWRn
ZT48L2JwbW5kaTpCUE1OUGxhbmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4i
fSwgImNvbnRlbnRfdmVyc2lvbiI6IDEsICJjcmVhdG9yX2lkIjogImFAYS5jb20iLCAiZGVzY3Jp
cHRpb24iOiAiVGhpcyB3b3JrZmxvdyB0YWtlcyBhbiBhdHRhY2htZW50IGZpbGUgYXMgaW5wdXQg
YW5kIGNhbGxzIHRoZSBWTVJheSBTYW5kYm94IEFuYWx5emVyIGZ1bmN0aW9uIHRvIGRldGVybWlu
ZSBpZiB0aGUgZmlsZSBjb250YWlucyBtYWx3YXJlLiAgVGhlIGFuYWx5c2lzIHJlc3VsdCBpcyBy
ZXR1cm5lZCBpbiBhbiBpbmNpZGVudCBub3RlLiIsICJleHBvcnRfa2V5IjogImV4YW1wbGVfdm1y
YXlfc2FuZGJveF9hbmFseXplcl9hdHRhY2htZW50IiwgImxhc3RfbW9kaWZpZWRfYnkiOiAiYUBh
LmNvbSIsICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTk5ODMxOTY5NDMzLCAibmFtZSI6ICJFeGFt
cGxlOiBWTVJheSBTYW5kYm94IEFuYWx5emVyIFtBdHRhY2htZW50XSIsICJvYmplY3RfdHlwZSI6
ICJhdHRhY2htZW50IiwgInByb2dyYW1tYXRpY19uYW1lIjogImV4YW1wbGVfdm1yYXlfc2FuZGJv
eF9hbmFseXplcl9hdHRhY2htZW50IiwgInRhZ3MiOiBbXSwgInV1aWQiOiAiZjhiODkxMGItMDcx
ZS00YzZmLWFkNTQtMzRhZDEwZTc5ZGIwIiwgIndvcmtmbG93X2lkIjogMzZ9XSwgIndvcmtzcGFj
ZXMiOiBbXX0=
""")
