from flask import Flask
app=Flask(__name__)
robots=[{"id":i,"name":f"ROBOT {i} {s} AI","subject":s,"brb":1000} for i,s in enumerate(["MATHS","MATHS","ENGLISH","ENGLISH","HAUSA","HAUSA","SCIENCE","SCIENCE","HEAD TEACHER","ASSISTANT"],1)]
@app.route('/robot/<int:id>/speak')
def robot_speak(id): r=robots[id-1]; return {"robot":r["name"],"speak":f"I am {r['name']} - {r['subject']} AI Teacher - 1000 BRB NFT","brb":1000}
@app.route('/robot/<int:id>/status')
def robot_status(id): return {"robot":robots[id-1],"status":"Online 100% AI","bullish":"78% Dominant"}
if __name__=='__main__': app.run(port=5001)
