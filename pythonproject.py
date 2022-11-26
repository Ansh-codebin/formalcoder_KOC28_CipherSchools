import random
when = ("once upon a time ","a year ago",)
who=(" me and my family","me and my friend")
where=("ramashearam","mumbai")

mode=("by car its was a ","by train its was a ")
experince=("great","superb")
activity=(" we enjoy a lot  we explore the city temples and museum and the local market  " , " we explore a lot there like we went to some tourist place like temple and old monument  ")
back=(" we all are un happy when relasied that the trip is going to end soon and we have to come back in our routine life ", " we all are sad after relase that trip is going to end very soon but we r also happy that we have collect a lot of memory ")
end=(" travelling is adventure which give us positive and negetive memory ")




print(random.choice(when) +random.choice(who) + "  going to "+ random.choice(where) + " which is 2000km far away from my home but  " +random.choice(mode)  + random.choice(experince) + " experince" + random.choice(activity) + random.choice(back))