import hashlib, random, time
class BlackRackBlockchain:
    def __init__(self): self.total_supply=0; self.bullish=78; self.brb_price=0.01
    def mint(self, typ, name, amt): tx="0x"+hashlib.sha256(f"{name}{time.time()}".encode()).hexdigest()[:12]; self.total_supply+=amt; print(f"Mint: {typ} {name} {amt} BRB TX:{tx} Bullish {self.bullish}%"); return {"name":name,"brb":amt,"tx":tx}
    def town_to_token(self): 
        for i in range(1,11): self.mint("ROBOT NFT TEACHER GIDA1",f"ROBOT TEACHER {i} GIDA1",1000)
        for i in range(1,31): self.mint("STUDENT NFT WEEK1 GIDA1",f"STUDENT {i} WEEK1 GIDA1",100)
        print(f"TOTAL 13K BRB - TOWN TO TOKEN 13K")
    def token_to_cash(self): fees=30*1.5; tokens=self.total_supply*self.brb_price; total=fees+tokens; print(f"Fees ${fees} + Tokens {self.total_supply}x${self.brb_price}=${tokens} = ${total}/month ROI 4M Bullish {self.bullish}%"); return {"total":total}
if __name__=='__main__': brb=BlackRackBlockchain(); brb.town_to_token(); print(brb.token_to_cash())
