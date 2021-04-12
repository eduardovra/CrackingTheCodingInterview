class CallCenter:
    def __init__(self, respondents, managers, directors) -> None:
        self.respondents = set(respondents)
        self.managers = set(managers)
        self.directors = set(directors)
        self.tiers = [self.respondents, self.managers, self.directors]
        self.busy: set = set()

    def _do_dispatch(self, tier):
        if tier >= len(self.tiers) or tier < 0:
            raise RuntimeError("All lines are busy")

        available = self.tiers[tier]
        try:
            employee = available.pop()
            self.busy.add(employee)
        except KeyError:
            return self._do_dispatch(tier + 1)

        return employee

    def dispatch_call(self):
        return self._do_dispatch(0)

    def hangup(self, employee):
        self.busy.remove(employee)

        if isinstance(employee, Respondent):
            self.respondents.add(employee)
        elif isinstance(employee, Manager):
            self.managers.add(employee)
        elif isinstance(employee, Director):
            self.directors.add(employee)


class Employee:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} {self.name}"


class Respondent(Employee):
    pass


class Manager(Employee):
    pass


class Director(Employee):
    pass


respondents = (
    Respondent("John"),
    Respondent("Brad"),
    Respondent("Maria"),
)

managers = (
    Manager("Megan"),
    Manager("Olivia"),
)

directors = (Director("Kurt"),)

cc = CallCenter(respondents, managers, directors)

employee = cc.dispatch_call()
employee = cc.dispatch_call()
employee = cc.dispatch_call()
employee = cc.dispatch_call()
employee = cc.dispatch_call()
employee = cc.dispatch_call()

cc.hangup(employee)
