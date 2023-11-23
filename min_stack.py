from stack import MainStack


class MinStack:
    # Initialize min and main stack here
    def __init__(self):
        self.main_stack = []
        self.aux_stack = []

    # Remove and returns value from the stack
    def pop(self):
        ret = self.main_stack.pop()
        self.aux_stack.pop()
        return ret

    # Pushes values into the stack
    def push(self, value):
        self.main_stack.append(value)
        if not self.aux_stack:
            self.aux_stack.append(value)
        else:
            if self.aux_stack[-1] > value:
                self.aux_stack.append(value)
            else:
                self.aux_stack.append(self.aux_stack[-1])


    # Returns minimum value from stack
    def min_number(self):
        return self.aux_stack[-1]

# SOLUTION
class MainStack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()


class MinStack:
    # Initializing min and main stack
    def __init__(self):
        self.min_stack = MainStack()
        self.main_stack = MainStack()

    # Pop() removes and returns value from min_stack
    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()

    # Pushes values into min_stack
    def push(self, value):
        self.main_stack.push(value)
        if self.min_stack.is_empty() or value < self.min_stack.top():
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.top())

    # Returns minimum value from min_stack in O(1) Time
    def min_number(self):
        if self.min_stack.is_empty():
            return None
        else:
            return self.min_stack.top()


# driver code
def main():
    input_stacks = [
                   [[9, 3, 1, 4, 2, 5], [1, 1, 0, 1, 0, 1]],
                   [[5, 10, 6, 23, 2], [1, 1, 0, 1, 0]],
                   [[1, 2, 3, 4, 5, 6, -3, -8], [1, 1, 0, 1, 0, 1, 1, 0]],
                   [[14, 32, 66, 71, 22, 50, 35], [1, 0, 1, 1, 0, 1, 0]],
                   [[-2, 4, 5, 0, 1, -3], [1, 1, 1, 1, 1, 1]]
    ]

    # loop over all the input streams
    for i in range(len(input_stacks)):
        print(i + 1, ".\t Starting operations:", sep="")
        min_stack_obj = MinStack()

        for j in range(len(input_stacks[i][1])):
            if input_stacks[i][1][j] == 1:
                if input_stacks[i][0] == []:
                    next
                else:
                    print("\t\t Push(", input_stacks[i][0][j], ")", sep="")
                    min_stack_obj.push(input_stacks[i][0][j])
            else:
                print("\t\t Pop() returns ", min_stack_obj.pop(), sep="")
        print("\t Minimum number in the stack is: ",
              min_stack_obj.min_number(), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()