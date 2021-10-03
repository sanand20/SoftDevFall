from flask import Flask
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?
# I have seen this kind of syntax in Java, where you have to declare the type before declaring an object.

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
# Usually, when I see a "/" in this environment, I assume that is being used to separate directories or files.

def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
#This depends on how you are running the file. If we directly run this file, it will print "__main__" in the command line or idle. If the file is being imported and run, it will print the file name.
    return "No hablo queso!"  # Q3: Will this appear anywhere? How u know?
#Yes, this will appear if hello_world() is called because the function would then return such string.

app.run()  # Q4: Where have you seen similar construcs in other languages?
#This construct is similar to those in Java, where methods associated with certain objects can be called in such manner. An example would be arrayList.get(0).

                
