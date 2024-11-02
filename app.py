from flask import Flask, render_template, send_from_directory,request, redirect
from pymongo import MongoClient
from routes import add, home, product
app = Flask(__name__)
app.secret_key = 'your_secret_key'
# MongoDB setup
client = MongoClient("mongodb+srv://user:user@cluster0.u3fdtma.mongodb.net/")  # Update this URI if your MongoDB setup is different
db = client["onelink"]  # Database name
collection = db["onelink"]  # Collection name





@app.route('/public/<path:filename>')
def custom_static(filename):
    return send_from_directory('assets', filename)





@app.route("/")
def start():
    try:
        # Fetch the specific submission by ID
        data1 = []
        data2 = []
        data1 = collection.find_one({"category": 'Template'})
        data2 = collection.find_one({"category": 'Google Drive'})
        return render_template('home.html',title="Get Templates, Drive Links, Websites, Everything on Onelink", data1=data1,data2=data2)
    except Exception:
        return "404"
    return render_template('home.html',title="Get Everything on Onelink", name="Jay")

@app.route("/link/<link_id>")
def product(link_id):
    try:
        # Fetch the specific submission by ID
        data = collection.find_one({"onelinkid": int(link_id)})
        print('data',data)
        if not data:
            return "404"
        if not (".jpg" in data['img'] or ".png" in data['img'] or ".webp" in data['img']):
            data['img'] = 'https://images.unsplash.com/photo-1506465139073-93b61c0d4795?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fHN0cmVldCUyMHJvYWR8ZW58MHx8MHx8fDA%3D'


        return render_template('product.html',data=data)
    except Exception:
        return "404"
    return render_template('product.html')

@app.route("/add")
def add_form():
    return render_template('add.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    last_entry = collection.find_one(sort=[("onelinkid", -1)])  # Sort by "id" in descending order
    if 'onelinkid' in last_entry:
        next_id = last_entry["onelinkid"] + 1 if last_entry else 1  # If no entries, start with ID 1
    else:
        next_id =1
    data = {"onelinkid": next_id,
        'title':request.form['title'],
            'category':request.form['category'],
            'img':request.form['img'],
            'url':request.form['url'],
            'username':request.form['username'],
            'description':request.form['description']
            }
    
    # Insert form data into MongoDB
    mdata = collection.insert_one(data)
 
    redir = '/link/'+str(next_id)
    return redirect(redir)