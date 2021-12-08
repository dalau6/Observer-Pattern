from abc import ABC, abstractmethod

class Team(ABC):
    """
    Interface represents publisher
    """

    @abstractmethod
    def attach(self, observer):
        pass
    
    @abstractmethod
    def detach(self, observer):
        pass
    
    @abstractmethod
    def notify(self):
        pass


class ConcreteTeam(Team):
    """
    ConcreteTeam implements interface Team
    """

    _observers_list = list()

    def attach(self, observer):
        print(f'{observer.name} added to team')
        self._observers_list.append(observer)

    def detach(self, observer):
        print(f'{observer.name} removed from team')
        self._observers_list.remove(observer)

    def notify(self):
        print('Team members:')
        for observer in self._observers_list:
            observer.update()

class Observer(ABC):
    """
    Interface Observer represnts subscribers
    """

    @abstractmethod
    def update(self, subject):
        pass

class David(Observer):
    name = "David"

    def update(self):
        print(f'{self.name} has been notified')

class Sarah(Observer):
    name = "Sarah"

    def update(self):
        print(f'{self.name} has been notified')

class Dan(Observer):
    name = "Dan"

    def update(self):
        print(f'{self.name} has been notified')

if __name__ == "__main__":

    publisher = ConcreteTeam()

    david = David()
    publisher.attach(david)

    sarah = Sarah()
    publisher.attach(sarah)

    dan = Dan()
    publisher.attach(dan)

    publisher.detach(david)

    publisher.notify()
