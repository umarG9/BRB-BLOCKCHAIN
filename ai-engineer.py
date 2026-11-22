import random, hashlib
class AIEngineer:
    def __init__(self): self.knowledge={"gini":{"en":"building","advice":"Gini - Building - Foundation 1m deep - Tushe 1m zurfi - Blocks 9 inch","brb":15},"lantarki":{"en":"electricity","advice":"Wiring - Wayar lantarki - Use 2.5mm cable","brb":15},"ruwa":{"en":"water","advice":"Plumbing - Bututun ruwa - PPR pipe - Tank 1000L","brb":10}}; self.engineers={}
    def engineer_advise(self,name,task): info=self.knowledge.get(task,{"en":task,"advice":f"Engineer advice for {task}","brb":5}); 
        if name not in self.engineers: self.engineers[name]={"total_brb":0}
        self.engineers[name]["total_brb"]+=info["brb"]; return {"engineer":name,"task":task,"en":info["en"],"advice":info["advice"],"brb":info["brb"],"tx":"0x"+hashlib.sha256(str(random.random()).encode()).hexdigest()[:10]}
