import random, hashlib
class AITrader:
    def __init__(self): self.bullish=78; self.market={"masara":{"price":50000},"brb":{"price":0.01}}; self.traders={}
    def market_analysis(self): return {"bullish":"78% 5 coins Green","status":"BULLISH 78% DOMINANT Green>Red Buy! Siya!"}
    def price_prediction(self,crop,days=7): cur=self.market.get(crop,{"price":50000})["price"]; is_bullish=random.random()<0.78; change=random.uniform(2,10) if is_bullish else random.uniform(-5,-1); pred=cur*(1+change/100); trend="BULLISH Farashi ya tashi Price up Sayar Sell Bullish 78%" if is_bullish else "BEARISH Farashi ya sauka Price down Siya Buy Bearish 22%"; return {"crop":crop,"current":f"₦{cur}","predicted":f"₦{pred:.0f} in {days} days","change":f"{change:+.1f}%","trend":trend}
    def trade(self,tname,action,crop,qty): price=self.market.get(crop,{"price":50000})["price"]; total=price*qty; brb=qty*5; 
        if tname not in self.traders: self.traders[tname]={"total_brb":0}
        self.traders[tname]["total_brb"]+=brb; return {"trade":f"{action} {qty} {crop} @ ₦{price}=₦{total}","brb":brb,"tx":"0x"+hashlib.sha256(str(random.random()).encode()).hexdigest()[:12]}
    def token_to_cash_trading(self,brb_amt): naira=brb_amt*0.01*1500; return {"brb":brb_amt,"naira":f"₦{naira:.0f}","rate":"1 BRB=$0.01=₦15"}
