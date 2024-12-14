from django.db import models

# Create your models here.
class Product(models.Model):
    """
    A model to represent a product in the store. This model stores the 
    necessary information about a product, including its name, image, price, 
    category, and description. It is used to manage products for an e-commerce 
    platform.

    Attributes:
        CATEGORY (tuple): A tuple that contains choices for the product's 
        category, such as Electronics, Groceries, and Clothings.
        name (str): The name of the product, limited to 100 characters.
        slug (str): A slugified version of the product name, used for URLs.
        image (ImageField): An image of the product to be uploaded to the 'img' 
        directory.
        description (str): A detailed description of the product.
        price (DecimalField): The price of the product, with up to 10 digits, 
        including 2 decimal places.
        category (str): The category of the product, chosen from predefined 
        categories.
    """
    CATEGORY = (
        ('Electronics', 'ELECTRONICS'),
        ('Groceries', 'GROCERIES'),
        ('Clothings', 'CLOTHINGS')
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='img')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=15, choices=CATEGORY,
                                blank=True, null=True)

    def __str__(self):
        """
        Returns a string representation of the Product object, specifically 
        the product's name. This method is used when displaying the product 
        in Django's admin interface or anywhere else a string representation 
        of the object is needed.
        
        Returns:
            str: The name of the product.
        """
        return self.name