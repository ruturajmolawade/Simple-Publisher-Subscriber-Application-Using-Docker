# class Subscriber:
#     def __init__(self, name):
#         self.name = name
#     def update(self, message):
#         print('{} got message "{}"'.format(self.name, message))
        
# class Publisher:
#     def __init__(self):
#         self.subscribers = set()
#     def register(self, who):
#         self.subscribers.add(who)
#     def unregister(self, who):
#         self.subscribers.discard(who)
#     def dispatch(self, message):
#         for subscriber in self.subscribers:
#             subscriber.update(message)

class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))
        
# class Publisher:
#     def __init__(self, events):
#         self.events = { event : dict()
#                           for event in events }
#         print(events)
#     def get_subscribers(self, event):
#         return self.events[event]
#     def register(self, event, who, callback=None):
#         if callback == None:
#             callback = getattr(who, 'update')
#         self.get_subscribers(event)[who] = callback
#     def unregister(self, event, who):
#         del self.get_subscribers(event)[who]

#     def dispatch(self, event, message):
#         for subscriber, callback in self.get_subscribers(event).items():
#             callback(message)

class Publishers:
    def __init__(self, events):

        self.events = { event : dict()
                          for event in events}

    def get_subscribers(self, event):
        return self.events[event]
    def register(self, event, who, callback=None):
        if callback == None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback
        print(self.get_subscribers(event)[who])
    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            print(subscriber)
            callback(message)

    def getEvents(self):
        for event in self.events:
            print(event)

    #################################
    # def __init__(self, name):
    #     self.name = name

    # def publish(self, events):
    #     print('{} got message "{}"'.format(self.name, message))

#     def publish(self,event,message):
class Publisher:
    def __init__(self, events,name):
        self.name = name
        self.events = { event : dict()
                          for event in events }
    
    def publish(self,event,message):
        pub = Publishers(self,event,message,self.name)
        pub.dispatch(event,message)


############

# class PubSubSystem:
#     def __init__(self,publisher):
#         self.events = { event : dict()
#                           for event in events }
#         print(event)
#     def get_subscribers(self, event):
#         return self.events[event]    

#     def register(self, event, who, callback=None):
#         if callback == None:
#             callback = getattr(who, 'update')
#         self.get_subscribers(event)[who] = callback
#     def unregister(self, event, who):
#         del self.get_subscribers(event)[who]

#     def dispatch(self, event, message):
#         for subscriber, callback in self.get_subscribers(event).items():
#             callback(message)
# # pub = Publisher()

# bob = Subscriber('Bob')
# alice = Subscriber('Alice')
# john = Subscriber('John')

# pub.register(bob)
# pub.register(alice)
# pub.register(john)

# pub.dispatch("It's lunchtime!")

# pub.unregister(john)

# pub.dispatch("Time for dinner")

#publisher = Publisher('BBC',['News','Sports'])
pub = Publishers(['lunch', 'dinner'])

pub1 = Publishers(['DS','ML'])
bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John')

pub.register("lunch", bob)
pub.register("dinner", alice)
pub.register("lunch", john)
pub.register("dinner", john)
pub1.register('ML',bob)

pub.dispatch("lunch", "It's lunchtime!")
pub.dispatch("dinner", "Dinner is served")
pub1.dispatch("ML","ML class")

pub.getEvents()