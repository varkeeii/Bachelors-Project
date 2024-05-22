from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('home.html')

@public.route('/about')
def about():
    return render_template('about.html')

@public.route('/contact')
def contact():
    return render_template('contact.html')

@public.route('/login',methods=['get','post'])
def login():
    if 'login' in request.form:
        u=request.form['uname']
        p=request.form['pwd']
        q="select * from tbl_login where Username='%s' and Password='%s' and Status='1'"%(u,p)
        res=select(q)

        if res:
            session['Username']=res[0]['Username']
            session['utype']=res[0]['User_Type']
            print("///////////////////////",session['utype'])
            uid=session['Username']
            if res[0]['User_Type']=="admin":
                flash("login Successfully")
                return redirect(url_for('admin.admin_home'))
            elif res[0]['User_Type']=="Customer":
                q="select * from tbl_customer where Username='%s'"%(uid)
                val=select(q)
                session['cid']=val[0]['Cust_ID']
                cid=session['cid']
                flash("login Successfully")
                return redirect(url_for('customer.customer_home'))
            elif res[0]['User_Type']=="Staff":
                q="select * from tbl_staff where Username='%s'"%(uid)
                val=select(q)
                session['sid']=val[0]['Staff_ID']
                sid=session['sid']
                flash("login Successfully")
                return redirect(url_for('staff.staff_home'))
            elif res[0]['User_Type']=="Courier":
                q="select * from tbl_courier where Username='%s'"%(uid)
                val=select(q)
                session['coid']=val[0]['Cour_ID']
                coid=session['coid']
                flash("login Successfully")
                return redirect(url_for('courier.courier_home'))
            flash('login success')
        else:
            flash('Ivalid Username or Password')
    return render_template('login.html')

@public.route('/registration',methods=['get','post'])
def registration():
    if 'register' in request.form:
        f=request.form['fname']
        l=request.form['lname']
        n=request.form['num']
        g=request.form['gen']
        h=request.form['hname']
        s=request.form['street']
        d=request.form['district']
        st=request.form['state']
        pin=request.form['pin']
        u=request.form['uname']
        p=request.form['pwd']
        
        q="SELECT * FROM `tbl_login` WHERE `Username`='%s' or `Password`='%s'"%(u,p)
        print(q)
        res=select(q)
        if res:
            flash("Username and Password already exist !")
            return redirect(url_for('public.registration'))
        else:
            q="insert into tbl_login values('%s','%s','Customer','1')"%(u,p)
            insert(q)
            q="insert into tbl_customer values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s',curdate(),'1','%s')"%(u,f,l,n,h,s,d,st,pin,g)
            insert(q)
            flash("Registered Successfully...")
    return render_template('registration.html')






            
            
        



