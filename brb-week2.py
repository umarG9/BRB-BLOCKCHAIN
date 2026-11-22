import hashlib, random, time
class BlackRackBlockchainWeek2:
    def __init__(self): self.total_supply=0; self.bullish=78; self.brb_price=0.01
    def mint(self,typ,name,amt,week=1): tx="0x"+hashlib.sha256(f"{name}{time.time()}".encode()).hexdigest()[:12]; self.total_supply+=amt; return {"name":name,"brb":amt,"tx":tx,"week":week}
    def week1_mint(self): self.total_supply=0; 
        for i in range(1,11): self.mint("ROBOT TEACHER GIDA1",f"ROBOT TEACHER {i} GIDA1",1000,week=1)
        for i in range(1,31): self.mint("STUDENT WEEK1 GIDA1",f"STUDENT {i} WEEK1 GIDA1",100,week=1)
    def week2_mint(self):
        for i in range(31,61): self.mint("STUDENT WEEK2 GIDA1",f"STUDENT {i} WEEK2 GIDA1 Advanced",100,week=2)
        for i in range(1,6): self.mint("ROBOT DOCTOR GIDA2",f"ROBOT DOCTOR {i} GIDA2",1000,week=2)
        for i in range(1,51): self.mint("PATIENT GIDA2",f"PATIENT {i} GIDA2",100,week=2)
        self.mint("BONUS BULLISH 78% WEEK2",f"BONUS BULLISH 78% WEEK2 2 HOUSES",2000,week=2)
    def token_to_cash_week2(self): fees=60*1.5+50*1; token_val=self.total_supply*self.brb_price; total=fees+token_val; return {"total":total,"total_brb":self.total_supply}
