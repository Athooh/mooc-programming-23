# Write your solution here:
class Task:
    task_counter = 0

    def __init__(self, description, programmer, workload):
        self.id = Task.generate_unique_id()
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    @classmethod
    def generate_unique_id(cls):
        cls.task_counter += 1
        return cls.task_counter

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"


class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        task = Task(description, programmer, workload)
        self.orders.append(task)

    def all_orders(self):
        return self.orders

    def programmers(self):
        unique_programmers = set()
        for order in self.orders:
            unique_programmers.add(order.programmer)
        return list(unique_programmers)

    def mark_finished(self, task_id):
        found = False
        for order in self.orders:
            if order.id == task_id:
                order.mark_finished()
                found = True
                break
        if not found:
            raise ValueError("No task found with the given ID")

    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]

    def status_of_programmer(self, programmer):
        finished_tasks = [order for order in self.finished_orders() if order.programmer == programmer]
        unfinished_tasks = [order for order in self.unfinished_orders() if order.programmer == programmer]
        finished_count = len(finished_tasks)
        unfinished_count = len(unfinished_tasks)
        finished_workload = sum(order.workload for order in finished_tasks)
        unfinished_workload = sum(order.workload for order in unfinished_tasks)
        return (finished_count, unfinished_count, finished_workload, unfinished_workload)

if __name__ == '__main__':
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)

