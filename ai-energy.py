import random, hashlib
class AIEnergy:
    def __init__(self): self.systems={"solar":{"power":"500W","battery":"200Ah","price":"₦300k","advice":"Solar Hasken rana 500W panel 200Ah battery Charge controller Mai kula da caji","brb":15},"gen":{"power":"5kVA","fuel":"Petrol","price":"₦500k","advice":"Generator Janareto 5kVA Petrol 10L per 8hrs","brb":15}}; self.houses={}
    def energy_advise(self,house,system): info=self.systems.get(system,{"power":"1kW","battery":"100Ah","price":"₦200k","advice":f"Energy {system}","brb":5}); tx="0x"+hashlib.sha256(str(random.random()).encode()).hexdigest()[:10]; 
        if house not in self.houses: self.houses[house]={"total_brb":0}
        self.houses[house]["total_brb"]+=info["brb"]; return {"house":house,"system":system,"power":info["power"],"advice":info["advice"],"brb":info["brb"],"tx":tx}
