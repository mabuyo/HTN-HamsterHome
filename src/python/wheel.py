class Wheel(object):
    def __init__(self, diameter):
        self.diameter = diameter
        
    def calculateDistance():
        # revolutions = float(incomingSerialData[2:])
        revolutions = 1
        circumference = 3.14159*diameterOfWheel
        distance = circumference*revolutions
        
### OLD STUFF
# d = datetime.datetime.now()
# key = str(str(d.month)+'-'+str(d.day)+'-'+str(d.year))
# thisday = wheelRef.child(key).get()
# oldDistance = thisday["totalDailyDistance"]
# wheelRef.child(key).set({
#     "totalDailyDistance": oldDistance + distance
# })