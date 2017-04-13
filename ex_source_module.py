import os
import twitter


class SomeClass:
    def __init__(self):
        self.var1 = None

    def one_plus_one(self, args):

        res = args[0] + args[1]
        print("Result is: " + str(res))

    def one_plus_one_tweet(self, api, args):
            result = args[0] + args[1]
            print("Result is: " + str(result))
            self.one_plus_one(args)
            success = api.PostUpdate(result)

    def make_api(self):
        api = twitter.Api()


