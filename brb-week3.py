import hashlib, random, time
class BlackRackBlockchainWeek3:
    def __init__(self): self.total_supply=0; self.week1_supply=13000; self.week2_supply=31000; self.week3_new=0; self.bullish=78; self.brb_price=0.01
    def mint(self,typ,name,amt,week=3): tx="0x"+hashlib.sha256(f"{name}{time.time()}".encode()).hexdigest()[:16]; self.total_supply+=amt; 
        if week==3: self.week3_new+=amt; return {"name":name,"brb":amt,"tx":tx,"week":week}
    def week1_mint(self): self.total_supply=0; 
        for i in range(1,11): self.mint("ROBOT TEACHER GIDA1",f"ROBOT TEACHER {i} GIDA1",1000,week=1)
        for i in range(1,31): self.mint("STUDENT WEEK1 GIDA1",f"STUDENT {i} WEEK1 GIDA1",100,week=1)
        self.week1_supply=self.total_supply
    def week2_mint(self):
        for i in range(31,61): self.mint("STUDENT WEEK2 GIDA1",f"STUDENT {i} WEEK2 GIDA1 Advanced",100,week=2)
        for i in range(1,6): self.mint("ROBOT DOCTOR GIDA2",f"ROBOT DOCTOR {i} GIDA2",1000,week=2)
        for i in range(1,51): self.mint("PATIENT GIDA2",f"PATIENT {i} GIDA2",100,week=2)
        self.mint("BONUS BULLISH 78% WEEK2",f"BONUS BULLISH 78% WEEK2 2 HOUSES",2000,week=2)
        for i in range(1,11): self.mint("STUDENT ADVANCED WEEK2",f"ADVANCED STUDENT {i} WEEK2 JSS1-SS1",100,week=2)
        self.week2_supply=self.total_supply
    def week3_mint(self):
        for i in range(61,101): self.mint("STUDENT WEEK3 GIDA1",f"STUDENT {i} WEEK3 GIDA1 100S Total",100,week=3)
        for i in range(1,6): self.mint("ROBOT FARMER GIDA3",f"ROBOT FARMER {i} GIDA3",1000,week=3)
        for i in range(1,51): self.mint("FARMER GIDA3",f"FARMER {i} GIDA3",100,week=3)
        for i in range(1,11): self.mint("CROP FIELD GIDA3",f"CROP FIELD {i} GIDA3 {random.choice(['Maize','Rice','Tomato'])} 1 Acre",500,week=3)
        for i in range(1,21): self.mint("TRADER GIDA3",f"TRADER {i} GIDA3",100,week=3)
        for i in range(1,101): self.mint("TRADE GIDA3",f"TRADE {i} GIDA3",50,week=3)
        self.mint("MARKET ANALYSIS NFT BULLISH 78% WEEK3",f"MARKET ANALYSIS BULLISH 78% DOMINANT Green>Red",1000,week=3)
        self.mint("BONUS TOWN TO TOKEN 3X WEEK3",f"BONUS TOWN TO TOKEN 3X 3 HOUSES BULLISH 78% 20 ROBOTS 200 PEOPLE",3000,week=3)
