class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        return f"{self.name} (located in {self.location})"
    
class Product:
    def __init__(self, name, price, company: Company) -> None:
        self.name = name
        self.price = price
        self.company = company

    def get_info(self):
        print(f"{self.name} is produced by {self.company.get_info()}")

company = Company("Apple", "california")
product = Product(name="Iphone", price=231, company=company)

product.get_info()