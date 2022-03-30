#Node Object and constructor
class Node():
    def __init__ (self, value):
        self.value = value
        self.next = None

first_node = Node(10)
second_node = Node(20)
third_node = Node(30)

first_node.next = second_node
second_node.next = third_node

# print(first_node, "This is my node object")
# print(first_node.value, "This is the value my node contains")
# print(first_node.next, "This is what my node points to")

# print(first_node, "This is my node object")
# print(first_node.value, "This is the value my node contains")
# print(first_node.next.value, "This is what my node points to")

# link list constructor
class Sll():
    def __init__ (self, head):
        self.head = head

    #add to front
    def add_front(self, value):
        temp = self.head
        self.head = Node(value)
        self.head.next = temp
        return self

    # displaying your list (we use var name called "Runner")
    def display(self):
        runner = self.head
        count = 1
        while(runner):
            print(f"This is your {count} node, it contains value {runner.value}")
            count += 1
            runner = runner.next
        return self

# new_ssl = Sll(Node(1)) #first haead node value
# print(new_ssl.head.value, "before")
# new_ssl.add_front(2)
# print(new_ssl.head.value, "after")


# Move
# SList: Move Min to Front
# Create a standalone function that locates the minimum value in a linked list, and moves that node to the front of the list. Return the new list, with all nodes still present, and all (except for the new head node) in their original order.

    def move_min_to_front(self):
            runner = self.head
            count=0
            temp_val = runner.value
            while(runner):
                if runner.next:
                    if temp_val > runner.next.value :
                        count+=1
                        temp_val=runner.next.value
                    else:
                        count+=1
                runner = runner.next
            self.contains_delete(temp_val)
            self.add_front(temp_val)


# SList: Move Max to Back
# Create a standalone function that locates the maximum value in a linked list, and moves that node to the back of the list. Return the new list, with all nodes still present, and all in their original order except for the node you moved to the end of the singly linked list.

    def move_max_to_back(self):
            runner = self.head
            max_val= runner.value
            while(runner):
                if  (max_val < runner.value):
                    max_val = runner.value


                runner = runner.next
            self.contains_delete(max_val)
            self.push_back(max_val)

    def val_push_back(self, new_value):
        new_node = Node(new_value)
        if(self.head == None):
            self.head = new_node
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node



new_ssl = Sll(Node(1)) 
new_ssl.add_front(2).add_front(4).add_front(22).add_front(43).add_front(7)
print(new_ssl.display())