from classes import *
import os


if __name__ == "__main__":

    os.system("cls")

    myOrderBook = OrderBook()

    print ("----- Choose the command number ----- \n")
    print (" 1: Add Task \n 2: Finished Tasks \n 3: Unfinished Tasks \n 4: Mark finished Task \n 5: Programmers \n 6: Programmer's status \n")
    
    while True:
        try: 
            cmd = int(input("Command: ").strip())
        

            if cmd == 0:
                break
            
            elif cmd == 1:
                print("------Add Task------\n")
                try:
                    description = input("description: ").strip()
                    programmer, workload_estimate = input("programmer and workload_estimate: ").strip().split()
                    workload_estimate = int(workload_estimate)
                    myOrderBook.add_order(description, programmer, workload_estimate)
                    print("added!")
                except:
                    print("Erroneous input")

            elif cmd == 2:
                print ("------Finished Tasks------\n")
                if (len(myOrderBook.orderList)== 0):
                    print("Empty orderBook!!")
                else: 
                    count = 0
                    for task in myOrderBook.orderList:
                        if task.is_finished() == True:  
                            count += 1 
                            print(task) 
                    if count == 0: 
                        print("No finished tasks")

            elif cmd == 3:
                print ("------Unfinished Tasks------\n")
                if (len(myOrderBook.orderList)== 0):
                    print("Empty orderBook!!")
                else:    
                    count = 0
                    for task in myOrderBook.orderList:
                        if task.is_finished() == False:  
                            count += 1 
                            print(task) 
                    if count == 0: 
                        print("All taskes are finished")

            elif cmd == 4:
                print ("------Mark finished Task------\n")
                try:
                    task_id = input("id: ").strip()
                    myOrderBook.mark_finished(int(task_id))  
                    print("Marked as finished")
                except:
                    print("Erroneous input")

            elif cmd == 5:
                    print ("------Display programmers------\n")
                    programmers = myOrderBook.programmers()
                    if not programmers:
                        print ("Empty orderbook")
                    else:   
                        for programmer in programmers:
                            print(programmer)

            elif cmd == 6: 
                try:
                    print ("------Display programmers------\n")
                    programmers = myOrderBook.programmers()
                    if not programmers:
                        print ("Empty orderbook")
                    else:     
                        programmer = input("programmer: ").strip()
                        finished, not_finished, done, scheduled = myOrderBook.status_of_programmer(programmer)
                        print(f"Task: finished {finished} not finished {not_finished}, hours: done {done} scheduled {scheduled}")
                except:
                    print("Erroneous input")

            else:
                print("Invalid command")
                
        except:
            print ( "Invalid input")