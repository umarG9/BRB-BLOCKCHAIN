import random, hashlib
class AITeacherAdvancedDay8:
    def __init__(self): self.students_memory={}; self.bullish=78
    def upgrade_week1_to_week2(self): return {"week1":"Basic 2+2=4 My name is Boko","week2":"Advanced Algebra x+2=5 → x=3! Sannu x uku ne! Grammar He go→He goes Physics Gravity Coding print('Hello BRB!') def add(a,b)","students":"30→60"}
    def add_student_memory(self,name,sub,score):
        if name not in self.students_memory: self.students_memory[name]={"scores":{},"weak":[],"strong":[],"total_brb":0}
        self.students_memory[name]["scores"][sub]=score
        if score<60:
            if sub not in self.students_memory[name]["weak"]: self.students_memory[name]["weak"].append(sub)
        else:
            if sub not in self.students_memory[name]["strong"]: self.students_memory[name]["strong"].append(sub)
        self.students_memory[name]["total_brb"]+=score; return self.students_memory[name]
    def personalized_lesson(self,name): mem=self.students_memory.get(name,{"weak":["Maths"]}); weak=mem["weak"][0] if mem["weak"] else "Maths"; return f"Hello {name}! Weak {mem['weak']} Focus {weak} Personalized AI Bullish 78%"
    def advanced_lesson(self,sub,level="JSS1"): adv={"Maths":{"JSS1":"Algebra: x+2=5 → x=3! Sannu x uku ne!"},"Coding":{"JSS1":"print('Hello BRB!')","SS1":"def add(a,b): return a+b"}}; return adv.get(sub,{}).get(level,f"Advanced {sub} {level}")
if __name__=='__main__': ai=AITeacherAdvancedDay8(); print(ai.add_student_memory("Aisha","Maths",45)); print(ai.personalized_lesson("Aisha")); print(ai.advanced_lesson("Maths","JSS1"))
