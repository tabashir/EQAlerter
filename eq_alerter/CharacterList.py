#    This file is part of EQAlerter.

#    EQAlerter is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    EQAlerter is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with EQAlerter.  If not, see <http://www.gnu.org/licenses/>.

# list of characters
class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # Return the head element in the list 
    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element

    # Return the last element in the list 
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element

    # Return true if the list is empty
    def isEmpty(self):
        return self.__size == 0

    # Return the size of the list
    def getSize(self):
        return self.__size

    def __str__(self):
        result = "["

        current = self.__head
        for i in range(self.__size+1):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", " # Separate two elements with a comma
            else:
                result += "]" # Insert the closing ] in the string

        return result

    # Add an element to the end of the list 
    def add(self, e, s):
        newCharacter = Character(e, s) # Create a new node for e

        if self.__tail == None:
            self.__head = self.__tail = newCharacter # The only node in list
        else:
            self.__tail.next = newCharacter # Link the new with the last node
            self.__tail = self.__tail.next # tail now points to the last node
            self.__size += 1 # Increase size

    # get character name
    def getName(self, index):
        current = self.__head
        for i in range(self.__size+1):
            if i == int(index):
                return(current.element)
            current = current.next


    # get character server
    def getServer(self, index):
        current = self.__head
        for i in range(self.__size+1):
            if i == int(index):
                return(current.server)
            current = current.next

    # Clear the list */
    def clear(self):
        self.__head = self.__tail = None

    # Return elements via indexer
    def __getitem__(self, index):
        return self.get(index)

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self.__head)
    

# The Character class
class Character:
    def __init__(self, name, server):
        self.element = name
        self.server = server
        self.next = None


class LinkedListIterator: 
    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            name = self.current.element
            server = self.current.server
            self.current = self.current.next
            return (name, server)    

# End of Class
