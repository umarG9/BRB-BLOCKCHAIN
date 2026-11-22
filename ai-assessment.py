import random, hashlib
class AITeacherAdvanced:
    def __init__(self): self.students_memory={}
    def add_student_memory(self,name,sub,score):
        if name not in self.students_memory: self.students_memory[name]={"scores":{},"weak":[],"strong":[],"total_brb":0}
        self.students_memory[name]["scores"][sub]=score
        if score<60: self.students_memory[name]["weak"].append(sub)
        else: self.students_memory[name]["strong"].append(sub)
        self.students_memory[name]["total_brb"]+=score; return self.students_memory[name]
    def personalized_lesson(self,name): mem=self.students_memory.get(name,{"weak":["Maths"]}); return f"Hello {name}! Weak {mem['weak']} Focus {mem['weak'][0]}"
    def auto_quiz(self,sub,level="JSS1"): return {"quiz":f"Solve x+2=5 JSS1 - {sub}","answer":"x=3!","brb":10}
    def generate_report(self,name): mem=self.students_memory.get(name,{}); avg=sum(mem["scores"].values())/len(mem["scores"]) if mem["scores"] else 0; return {"student":name,"avg":avg,"total_brb":mem.get("total_brb",0),"nft":f"REPORT NFT {name} TX 0x..."}
