
class Task:
    
    __idCounter= 0
        
    def __init__(self, description, programmer, workload, status = "NOT FINISHED"):
        
        Task.__idCounter+= 1
        
        self.id = Task.__idCounter
        self.description = description
        self.workload = workload
        self.programmer = programmer
        self.status = status

    def mark_finished(self):
        self.status = "FINISHED" 
    
    def is_finished(self):
        return self.status == "FINISHED"

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.status}"



#----------------------test----------------------
# t1 = Task("program hello world", "Eric", 3)
# print(t1.id, t1.description, t1.programmer, t1.workload)
# print(t1)
# print(t1.is_finished())
# t1.mark_finished()
# print(t1)
# print(t1.is_finished())
# t2 = Task("program webstore", "Adele",10)
# t3 = Task("program mobile app for workload accounting", "Eric",25)
# print(t2)
# print(t3)


class OrderBook:
    
    __orderList = []
    __programmerList = []
    
    def __init__(self):
        self.tasks = [] 
        self.next_id = 1  
        
    @property
    def orderList(self):
        return self.__orderList
        
    def add_order(self, description, programmer, workload):
        self.__orderList.append(Task(description, programmer, workload))
            
    def all_orders(self):
        return self.__orderList 
   
    def programmers(self):
        for task in self.__orderList :
            if task.programmer not in self.__programmerList:
             self.__programmerList.append(task.programmer)
        return self.__programmerList

    def programmersTasks(self):
        programmer_tasks = {}  
        
        for task in self.__orderList:
            programmer_name = task.programmer 
            task_id = task.id  
            
            if programmer_name in programmer_tasks:
                programmer_tasks[programmer_name].append(task_id)
            else:
                programmer_tasks[programmer_name] = [task_id]
        
        return programmer_tasks

    def mark_finished(self, id):
    
        task_found = False
        
        for task in self.__orderList:
            if task.id == id:
                task.mark_finished()
                task_found = True
                break
        
        if not task_found:
            raise ValueError(f"Task with id {id} not found.")

    def status_of_programmer(self, programmer):
        __finished_tasks = 0
        __unfinished_tasks = 0
        __finished_hours = 0
        __unfinished_hours = 0
        
        for task in self.__orderList:
            if task.programmer == programmer:
                if task.is_finished():
                    __finished_tasks += 1
                    __finished_hours += task.workload
                else:
                    __unfinished_tasks += 1
                    __unfinished_hours += task.workload
        
        return (__finished_tasks, __unfinished_tasks, __finished_hours, __unfinished_hours)



#----------------------test----------------------
# orders = OrderBook()
# orders.add_order("program webstore", "Adele", 10)
# orders.add_order("program mobile app for workload accounting", "Eric", 25)
# orders.add_order("program app for practising mathematics", "Adele", 100)
# orders.add_order("program the next facebook", "Eric", 1000)

# orders.mark_finished(1)
# orders.mark_finished(2)

# for order in orders.all_orders():
#     print(order)

# for programmer in orders.programmers():
#     print (programmer)

# programmer_task_dict = OrderBook.programmersTasks(orders)
# print(programmer_task_dict)

# status = orders.status_of_programmer("Adele")
# print(status)