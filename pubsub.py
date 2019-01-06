#https://www.protechtraining.com/blog/post/879
class Subscriber:
    
    def __init__(self, name):
        self.name = name
    def update(self, message):
        publishedMessage = '{} got message "{}"'.format(self.name, message)
        return publishedMessage
    def register(self,event):
        pubsub = Publishers()
        pubsub.subscribe(event,self)
        subscriberEventsList = pubsub.getEvents(self.name)
        messages = pubsub.getMessage(event)
        messageString = ""
        for message in messages:
            messageString += message
        return messageString

 
class Publishers:
    mydict = {}
    subscriberEventsDict = {}
    eventMessageDict = {}

    def get_subscribers(self, event):
        if event in self.mydict.keys():
            return self.mydict[event]
        return []

    def subscribe(self, event, who, callback=None):
        if event in self.mydict.keys():
            self.get_subscribers(event).append(who)
        else:
            subList =[]
            subList.append(who)
            self.mydict[event]= subList
        if who.name in self.subscriberEventsDict.keys():
            self.subscriberEventsDict[who.name].append(event)
        else:
            eventList =[]
            eventList.append(event)
            self.subscriberEventsDict[who.name] = eventList

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def dispatch(self, event, message):
        messageList = {}
        if event in self.eventMessageDict.keys():
            self.eventMessageDict[event].append(message)
        else:
            subList =[]
            subList.append(message)
            self.eventMessageDict[event]= subList
        # self.eventMessageDict[event] = message
        for subscriber in self.get_subscribers(event):
            publishedMessage = subscriber.update(message)
            messageList[subscriber.name] = publishedMessage
        return messageList

    def getEvents(self,subcriber):
        return self.subscriberEventsDict[subcriber]

    def getMessage(self,event):
        if event in self.eventMessageDict.keys():
            return self.eventMessageDict[event]
        else:
            return ["No message published"]

    


class Publisher:    
    def publish(self,event,message):
        pub = Publishers()
        publishedMessageDict = pub.dispatch(event,message)
        return publishedMessageDict




pub = Publisher()
alice = Subscriber('Alice')
john = Subscriber('John')
mark = Subscriber('Mark')
# message = alice.register("dinner")
# print(message)
# message = john.register("lunch")
# print(message)
# message = mark.register("lunch")
# print(message)
pub.publish("lunch", "It's lunchtime!")
pub.publish("dinner", "Dinner is served")
message = alice.register("dinner")
print(message)
message = john.register("lunch")
print(message)
message = mark.register("lunch")
print(message)



