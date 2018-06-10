import weakref


class Subject(object):
    """Provider of notifications to other objects
    """

    def __init__(self, name):
        self.name = name
        self._observers = weakref.WeakSet()

    def register_observer(self, observer):
        """attach the observing object for this subject
        """
        self._observers.add(observer)
        print("observer {0} now listening on {1}".format(
            observer.name, self.name))

    def notify_observers(self, msg):
        """transmit event to all interested observers
        """
        print("subject notifying observers about {}".format(msg,))
        for observer in self._observers:
            observer.notify(self, msg)


class Observer(object):

    def __init__(self, name):
        self.name = name

    def start_observing(self, subject):
        """register for getting event for a subject
        """
        subject.register_observer(self)

    def notify(self, subject, msg):
        """notify all observers 
        """
        print("{0} got msg from {1} that {2}".format(
            self.name, subject.name, msg))

#class_homework = Subject("class homework")
#student1 = Observer("student 1")
#student2 = Observer("student 2")

#student1.start_observing(class_homework)
#student2.start_observing(class_homework)

#class_homework.notify_observers("result is out")

#del student2

#class_homework.notify_observers("20/20 passed this sem")

#The output for the preceding code is as follows:

#$ python codes/B04885_05_code_01.py
#observer student 1 now listening on class homework
#observer student 2 now listening on class homework
#subject notifying observers about result is out
#student 1 got msg from class homework that result is out
#student 2 got msg from class homework that result is out
#subject notifying observers about 20/20 passed this sem
#student 1 got msg from class homework that 20/20 passed this sem


  
