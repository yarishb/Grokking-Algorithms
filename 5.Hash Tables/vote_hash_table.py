voted = {}
def vote(name):
     if voted.get(name):
          print("Kick them out!")
     else:
          voted[name] = True
          print("Let them vote")

vote("Bob")
vote("Martin")
vote("Bob")
vote("Robbin")