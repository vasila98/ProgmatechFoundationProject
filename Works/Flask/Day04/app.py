from flask import Flask,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        _ad=request.form['ad']
        return f'<h1>{_ad} sagol</h1>'
    return 'salam'

@app.route('/about')
def about():
    return f"""
        <form action='/' method='POST' >
        <input type='text' placeholder='Name' name='ad'>
        <input type='submit' value='Gonder'>
        </form>
    """
    

if __name__=='__main__':
    app.run(debug=True)

    





