# SQL-Fury
Automatically check your endpoints to see if they are vulnerable to SQL injections.

## Usage:
```bash
git clone https://github.com/ism8el/SQL-Fury.git
cd SQL-Fury/
chmod +x ./SQL-Fury.py
cat endpoints.txt | ./SQL-Fury.py
```

## Example:
### On a single endpoints:
```bash
echo "https://example.com/?message=hello" | ./SQL-Fury.py
```

### On bulk endpoints:
```bash
cat endpoints.txt | ./SQL-Fury.py
```

![Screenshot](/image.jpg "Screenshot").
