import random, hashlib
class AIDoctor:
    def __init__(self): self.knowledge={"ciwon kai":{"en":"headache","diagnosis":"Take water, rest, paracetamol - Sha ruwa, huta","brb":10},"zazzabi":{"en":"fever","diagnosis":"Fever - Check malaria - Zazzabi - Duba malaria","brb":20}}; self.patients={}
    def diagnose(self,pname,sym): info=self.knowledge.get(sym,{"en":sym,"diagnosis":"Drink water, rest - Sha ruwa, huta","brb":5}); 
        if pname not in self.patients: self.patients[pname]={"visits":[],"total_brb":0}
        self.patients[pname]["total_brb"]+=info["brb"]; return {"patient":pname,"symptom":sym,"en":info["en"],"diagnosis":info["diagnosis"],"brb":info["brb"],"tx":"0x"+hashlib.sha256(str(random.random()).encode()).hexdigest()[:10]}
