class BaseHandler:
    def __init__(self):
        self.next=None

    def set_next(self,handler):
        self.next = handler
        return handler
    
    def handle(self,context):
        if(self.next is not None):
            return self.next.handle(context)
        return context
        
