from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/profile/<name>')
def profile(name):
    return  render_template('profile.html',name=name,IsActive=True)
@app.route('/books')
def book():
    books=[{'Name':'Fourth Wing','Author':'Rebecca Yarros','Cover':"https://imgs.search.brave.com/udH7vcVE6tEyu2XT4gXJD8qe5RxDsCoGqiYu1s96wvM/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS50aGVldmVyeWdp/cmwuY29tL3dwLWNv/bnRlbnQvdXBsb2Fk/cy8yMDIzLzA0L3Rl/Zy1mb3VydGgtd2lu/Zy1yZXZpZXctMS5q/cGc"},
           {'Name':'Lessons in chemistry','Author':'Garmus','Cover':"https://imgs.search.brave.com/fU0_DS6VAdKdSWzP2kiFxS7ykDoT46oeOo_h8aevmps/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMtbmEuc3NsLWlt/YWdlcy1hbWF6b24u/Y29tL2ltYWdlcy9J/LzgxdUlBdlduMktM/LmpwZw"},
           {'Name':'Lion and Lamb','Author':'Patterson','Cover':"https://imgs.search.brave.com/b1r-34YquRsDt10s2YaMy3KSeEzGVlLN1XXQqKTc27w/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/aGFjaGV0dGVib29r/Z3JvdXAuY29tL3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDIzLzA1/Lzk3ODAzMTY0MDQ4/OTEtMi5qcGc_Zml0/PTQxMiw2NDA"}]
    return  render_template('book.html',books=books)

app.run(debug=True)
