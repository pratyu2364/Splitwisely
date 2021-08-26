class Allocator():
    def __init__(self,total,members):
        self.total = total
        self.members = members
    def Allocate_money(self):
        each_member = self.total/len(self.members)
        paid_not_owe = {}
        paid_owe = {}
        not_paid = {}
        to_get = {}
        to_pay = {}
        for i in self.members:
            if self.members[i] > 0 and self.members[i] >= each_member :
                paid_not_owe[i] = self.members[i]# storing friends who have paid bt not owed in a dictionary with the amount
            elif self.members[i] > 0 and self.members[i] < each_member:
                paid_owe[i] = self.members[i]#storing friends who have paid bt owe to someone
            elif self.members[i] == 0:
                not_paid[i] = self.members[i]#friends who had not paid and owe to someone
        for i in paid_not_owe:
            to_get[i] = paid_not_owe[i] - each_member#l the amount each member will get after distribution according to the payment made before
        for i in paid_owe :
            to_pay[i] = each_member - paid_owe[i]#l the amount to be paid by each member  after distribution
        for i in not_paid:
            to_pay[i] = each_member# the amount to be paid by each member who did not pay anything before
        print_list = []
        for mem in to_pay:
            for i in to_get:
                if to_pay[mem] < to_get[i] and to_pay[mem] > 0:
                    print_list.append(f"{mem} has to pay {to_pay[mem]} to {i}")
                    to_get[i] = to_get[i] - to_pay[mem]#members of to_get dictionary get the amount but that is not the final amount
                    to_pay[mem] = 0#member after paying their part, they dont have to any other friend
                    break
                elif to_pay[mem] > to_get[i] and to_get[i] > 0:#
                    print_list.append(f"{mem} has to pay {to_get[i]} to {i}")
                    to_pay[mem] = to_pay[mem] - to_get[i]#member of this group have owed the money to a friend but need to owe the sum to other members of this group
                    to_get[i] = 0#member of this group gets his full part
                elif to_get[i] == to_pay[mem] and to_get[i] > 0:#if amount that a member from to_get dictionary needs to get is equal to amount paid by to_pay group
                    print_list.append(f"{mem} has to pay {to_get[i]} to {i}")
                    to_pay[mem] = 0#both have their part complete
                    to_get[i] = 0
                    break
        return print_list


class PercDiv():
    def __init__(self,total,members,percentage):
        self.total = total
        self.members = members
        self.percentage = percentage
    def Allocate_money(self):
        to_get = {}
        to_pay = {}
        i = 0
        for x in self.members:
            if (self.percentage[i])*(self.total)/100 > self.members[x] :
                to_pay[x] = (self.percentage[i])*(self.total)/100 - self.members[x]
            elif (self.percentage[i])*(self.total)/100 < self.members[x] :
                to_get[x] = self.members[x] - (self.percentage[i])*(self.total)/100
            i += 1
        print_list = []
        for mem in to_pay:
            for i in to_get:
                if to_pay[mem] < to_get[i] and to_pay[mem] > 0:
                    print_list.append(f"{mem} has to pay {to_pay[mem]} to {i}")
                    to_get[i] = to_get[i] - to_pay[mem]
                    to_pay[mem] = 0
                    break
                elif to_pay[mem] > to_get[i] and to_get[i] > 0:
                    print_list.append(f"{mem} has to pay {to_get[i]} to {i}")
                    to_pay[mem] = to_pay[mem] - to_get[i]
                    to_get[i] = 0
                elif to_get[i] == to_pay[mem] and to_get[i] > 0:
                    print_list.append(f"{mem} has to pay {to_get[i]} to {i}")
                    to_pay[mem] = 0
                    to_get[i] = 0
                    break
        return print_list
