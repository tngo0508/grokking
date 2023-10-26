class RequestLogger:
    def __init__(self, time_limit):
        self.time_limit = time_limit
        self.hash_map = {}

    # This function decides whether the message request should be accepted or rejected
    def message_request_decision(self, timestamp, request):
        result = True
        if request in self.hash_map:
            t = timestamp - self.hash_map[request]
            if t < self.time_limit:
                result = False
        if result:
            self.hash_map[request] = timestamp
        return result

## solution
class RequestLogger:

    # initailization of requests hash map
    def __init__(self, time_limit):
        self.requests = {}
        self.limit = time_limit

    # function to accept and deny message requests
    def message_request_decision(self, timestamp, request):

        if request not in self.requests or timestamp - self.requests[request] >= self.limit:
            self.requests[request] = timestamp
            return True

        else:
            return False

# driver code
def main():
    new_requests = RequestLogger(7)

    times = [1, 5, 6, 7, 15]
    messages = ["good morning",
                "hello world",
                "good morning",
                "good morning",
                "hello world"]

    for i in range(len(messages)):
        print(i + 1, ".\t Time, Message: {",
              times[i], ", '", messages[i], "'}", sep="")
        print("\t Message request decision: ",
              new_requests.message_request_decision(
                times[i], messages[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()
