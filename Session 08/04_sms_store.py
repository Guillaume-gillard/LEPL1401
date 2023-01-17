### Code to complete [START] ###

class SMS_Store :
    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        new_sms = (from_number, time_arrived, text_of_SMS)
        self.inbox.append(new_sms)
        self.has_been_viewed = False
    
    
    def message_count(self):
        number_of_message = len(self.inbox)
        return number_of_message
    

    def get_unread_indexes(self):
        unread_indexes = []
        count = 0
        for sms in self.inbox:
            if not sms.has_been_viewed :
                unread_indexes.append(count)
            count += 1
        return unread_indexes

    def get_message(self, i):
        sms_location = self.inbox[i]
        sms = (sms_location[0], sms_location[1], sms_location[2])
        return sms
    
    
    def delete(self, i):
        self.inbox.pop(i)
    

    def clear(self):
        self.inbox = []