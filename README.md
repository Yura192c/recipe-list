# recipe-list
Test task MirGovorit backend

### Examples of requests
```
GET /recipe/add_product_to_recipe/?recipe_id=1&product_id=2&weight=150
GET /recipe/cook_recipe/?recipe_id=1
GET /recipe/show_recipes_without_product/?product_id=3

```

# Running the program
### Dependency installation
```
pip install -r requirements.txt
```
or create virtual venv 
```
python -m venv venv
source venv/bin/activate
```

### Running the program
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```