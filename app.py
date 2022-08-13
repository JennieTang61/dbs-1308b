#!/usr/bin/env python
# coding: utf-8

# In[7]:


from flask import Flask,render_template,request


# In[8]:


import joblib


# In[9]:


app=Flask(__name__)


# In[10]:


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates=float(request.form.get("rates"))
        print(rates)
        model1=joblib.load("regression_DBS")
        pred1=model1.predict([[rates]])
        model2=joblib.load("tree_DBS")
        pred2=model2.predict([[rates]])
        
        #return(render_template("index.html",result1="temp",result2="temp"))
        return(render_template("index.html",result1=pred1,result2=pred2))
    else:
        return(render_template("index.html",result1="waiting",result2="waiting"))
    


# In[ ]:


if __name__ =="__main__":
    app.run()


# In[6]:


__name__


# In[ ]:





# In[ ]:




