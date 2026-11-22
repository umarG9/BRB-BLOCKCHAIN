import random, hashlib
class AIFarmer:
    def __init__(self): self.knowledge={"masara":{"en":"maize","season":"Rainy Damina June-Oct","soil":"Loamy Yashi mai kyau","yield":"1 acre 20 bags","price":"₦50k per bag","brb":15},"shinkafa":{"en":"rice","season":"Rainy Fadama","yield":"1 acre 25 bags","price":"₦60k","brb":15}}; self.farmers={}
    def advise(self,fname,crop): info=self.knowledge.get(crop,{"en":crop,"season":"General","yield":"Good","price":"Good","brb":5}); 
        if fname not in self.farmers: self.farmers[fname]={"total_brb":0,"acres":0}
        self.farmers[fname]["total_brb"]+=info["brb"]; self.farmers[fname]["acres"]+=1
        return {"farmer":fname,"crop":crop,"en":info["en"],"season":info["season"],"yield":info["yield"],"price":info["price"],"brb":info["brb"],"tx":"0x"+hashlib.sha256(str(random.random()).encode()).hexdigest()[:10]}
