from ticketscript import Ticket, StudentTicket, GroupTicket

def show_all(tickets):
    for t in tickets:
        print (f"{t.get_name()}: rs {t.price() :.2f}")

def main():
    tickets_list = [Ticket("Concert",200), StudentTicket("Museum", 150)]
    show_all(tickets_list)

main()