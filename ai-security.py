import random, hashlib
class AISecurity:
    def __init__(self): self.threats={"barawo":{"en":"thief","action":"Alarm! Qararrawa! Call police Kira yansanda Lock doors Rufe kofofi","brb":20},"gobara":{"en":"fire","action":"Fire! Gobara! Use extinguisher Amfani da kashe gobara Evacuate Fice","brb":20}}; self.guards={}
    def security_check(self,guard,loc,threat): info=self.threats.get(threat,{"en":threat,"action":f"Check {threat}","brb":10}); tx="0x"+hashlib.sha256(str(random.random()).encode()).hexdigest()[:10]; 
        if guard not in self.guards: self.guards[guard]={"total_brb":0}
        self.guards[guard]["total_brb"]+=info["brb"]; return {"guard":guard,"location":loc,"threat":threat,"en":info["en"],"action":info["action"],"brb":info["brb"],"tx":tx}
