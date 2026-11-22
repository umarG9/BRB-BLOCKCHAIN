import random
class AITeacher:
    def __init__(self): self.bullish=78; self.robots=10
    def ai_brain_response(self, subject, question):
        if subject=="Maths": return f"2+2=4 - Biyu da biyu hudu ne! Sannu yara! - Basic W1 - Ready for Advanced Algebra x+2=5 - Bullish {self.bullish}% - {question}"
        elif subject=="English": return f"My name is BRB AI! - Basic W1 - Ready for Advanced Grammar He go→He goes - {question}"
        else: return f"BRB AI School - 10 AI Teachers - 100% AI - {subject} - {question} - Bullish {self.bullish}%"
if __name__=='__main__': ai=AITeacher(); print(ai.ai_brain_response("Maths","What is 2+2?")); print(ai.ai_brain_response("English","My name?"))
