# day 34

## django form

```django
{% for field in form %}
    {{ field.errors }}    
    <br>
    {{ field.label_tag }}
    <br>
    {{ field }}    
    {% endfor %}
```



