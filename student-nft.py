import hashlib, random
class BRBBlockchain:
    def __init__(self): self.total=0
    def mint_student_nft(self, name): tx="0x"+hashlib.sha256(f"{name}{random.random()}".encode()).hexdigest()[:10]; self.total+=100; return {"name":name,"brb":100,"tx":tx,"type":"STUDENT NFT"}
    def mint_robot_nft(self, name): tx="0x"+hashlib.sha256(f"{name}{random.random()}".encode()).hexdigest()[:10]; self.total+=1000; return {"name":name,"brb":1000,"tx":tx,"type":"ROBOT NFT"}
if __name__=='__main__': brb=BRBBlockchain(); print(brb.mint_student_nft("Aisha")); print(brb.mint_robot_nft("ROBOT 1 MATHS AI"))
