class Country('models'.Model):
    name = 'models'.CharField(max_length=50, default="Zambia")
    code = 'models'.CharField(max_length=2)
    
    def __str__(self):
        return self.name
