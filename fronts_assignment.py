# Front
# Write a method to return the value (not the node) at the head of the list. If the list is empty, return null.

#  Node Object constructor
class Sll_Node():
    def __init__ (self, value):
        self.value = value
        self.next = None

first_node = Sll_Node(10)
second_node = Sll_Node(20)
third_node = Sll_Node(30)

first_node.next = second_node
second_node.next = third_node

# print(second_node.next.value)


# link list constructor
class Sll():
    def __init__ (self, head):
        self.head = head


# Add Front
# Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node.

    def add_front(self, value):
        add_temp = self.head
        self.head = Sll_Node(value)
        self.head.next = add_temp
        return self


# Remove Front
# Write a method to remove the head node and return the new list head node. If the list is empty, return null.

    def remove_front(self, value):
        if self.head == None:
            return self

        remove_temp = self.head
        self.head = remove_temp.next
        remove_temp.next = None
        return self

# displaying list
    def display(self):
        runner = self.head
        count = 1
        while(runner):
            print(f"this is {count} node, contains value {runner.value}")
            count += 1
            runner = runner.next
        return self

new_Sll = Sll(Sll_Node(1))
# print(new_Sll.head.value)
new_Sll.add_front(2).add_front(4).add_front(22).add_front(43).add_front(7).remove_front(7).remove_front(1)
print(new_Sll.display())