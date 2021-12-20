# class Car:
#
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def report(self):
#         print(f"{self.brand} - {self.model}")
#
#
# class User:
#
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.purchases = 0
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, another_user):
#         self.following += 1
#         another_user.followers += 1
#
#     def buy(self):
#         self.purchases += 1
#
#     def report(self):
#         print(f"{self.username} has {self.followers} followers and also following {self.following}")
#
#
# tesla = Car("Tesla", "Model 3")
# tesla.report()
#
# anton = User("anton", "a123")
# clarence = User("clarence", "c123")
# mohana = User("mohana", "m123")
#
# clarence.follow(mohana)
# clarence.follow(anton)
# anton.follow(clarence)
#
# clarence.report()
# anton.report()
# mohana.report()

from day_17_quiz import Quiz

quiz = Quiz()


for _ in quiz.questions:

    quiz.display_current_question()
    quiz.check_answer()
    quiz.display_score()
    quiz.current_index += 1

print(f"\nYou got {round(quiz.score / quiz.current_index * 100, 2)}%")