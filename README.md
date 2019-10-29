# API-Understanding-with-Flask
Understanding API with Python Flask

### My Dataset

```python
my_data = {
    '9001': ['Airtel India', 'Andhra Pradesh & Telangana'],
    '9003': ['Airtel India', 'Tamilnadu'],
    '9323': ['Null', 'Mumbai'],
    '9984': ['Vodafone India', 'UP East'],
    '8840': ['Reliance Jio', 'Haryana East'],
    '8318': ['Reliance Jio', 'Himachal East'],
    '8340': ['Reliance Jio', 'Punjab East'],
    '9996': ['Airtle India', 'Haryana'],
}
```

### API Phone Code

```python
def phone():
    number2 = ''
    gstate = ''
    tname = ''
    number = request.args['number']
    if len(number) < 10 or len(number) > 10:
        return jsonify(error="Your number is wrong"), 404
    else:
        for key, value in my_data.items():
            if key == number[0:4]:
                gstate = value[1]
                tname = value[0]
                return jsonify(your_number=number, state=gstate, company_name=tname), 200

```

### Used Modules
1. Flask==1.1.1
2. requests==2.22.0
