from myproject import app,db
from flask import render_template,redirect,request,url_for,flash,abort
from flask_login import login_user,login_required,logout_user
from myproject.models import User
from myproject.forms import LoginForm,RegistrationForm,HowToSplit
from werkzeug.security import generate_password_hash, check_password_hash
from myproject.mainform import FriendForm,PercentageDiv
from myproject.functionality import Allocator,PercDiv




@app.route('/')
def home():
    return render_template('home.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You logged out!")
    return redirect(url_for('home'))


@app.route('/login',methods = ['GET','POST'])
def login():
     form = LoginForm()
     if form.validate_on_submit():
         user = User.query.filter_by(email = form.email.data).first()

         if user.check_password(form.password.data) or user.login_user(form.email.data) and user is not None:
             login_user(user)
             flash('Logged in successfully')
             return redirect(url_for('split_method'))

     return render_template('login.html',form=form)


@app.route('/getdataperc' ,methods = ['GET','POST'])
@login_required
def getdataperc():
    form = PercentageDiv()
    return render_template('getdataperc.html',form = form)

@login_required
@app.route('/getdata')
def getdata():
    form = FriendForm()
    return render_template('getdata.html', form = form)
@login_required
@app.route('/Split_method')
def split_method():
    form = HowToSplit()
    return render_template('getdata1.html',form = form)


@app.route('/displayperc', methods = ['POST'])
def display_perc():
    form = PercentageDiv()
    n = form.number_of_members.data
    friends_string = form.friends_list.data
    percentage_string = form.percentage_each.data
    money_string = form.money_paid.data
    i = 0
    friend = ''
    friend_list = []
    while i < len(friends_string):
        if friends_string[i] is ',':
            friend_list.append(friend)
            friend = ''
        elif i == len(friends_string) - 1:
            friend += friends_string[i]
            friend_list.append(friend)
        else:
            friend += friends_string[i]
        i += 1
    i = 0
    money = ''
    money_list = []
    while i < len(money_string):
        if money_string[i] == ',':
            money_list.append(int(money))
            money = ''
        elif i == len(money_string) - 1:
            money += money_string[i]
            money_list.append(int(money))
        else:
            money += money_string[i]
        i += 1
    if len(money_list) < n:
        diff = n - len(money_list)
        while diff == 0:
            money_list.append(0)
            diff -= 1
    i = 0
    percentage_each = ''
    percentage_list = []
    while i < len(percentage_string):
        if percentage_string[i] == ',':
            percentage_list.append(int(percentage_each))
            percentage_each = ''
        elif i == len(percentage_string) - 1:
            percentage_each += percentage_string[i]
            percentage_list.append(int(percentage_each))
        else:
            percentage_each += percentage_string[i]
        i += 1
    total_perc = 0
    for i in percentage_list:
        total_perc += i
    if len(percentage_list) < n:
        diff = n - len(percentage_list)
        while diff == 0:
            percentage_list.append(0)
            diff -= 1
    members = {}
    j = 0
    for i in friend_list:
        members[i] = money_list[j]
        j += 1
    total = 0
    for i in money_list:
        total += i
    print(total, members,percentage_list)
    allocate = PercDiv(total, members,percentage_list)
    print_list = allocate.Allocate_money()
    print(print_list)
    return render_template('dispaly.html', print_list=print_list)



@app.route('/display',methods = ['POST'])
def display_data():
        form = FriendForm()
        n = form.number_of_members.data
        friends_string = form.friends_list.data
        money_string = form.money_paid.data
        i = 0
        friend = ''
        friend_list = []
        while i < len(friends_string):
            if friends_string[i] is ',':
                friend_list.append(friend)
                friend = ''
            elif i == len(friends_string) - 1:
                friend += friends_string[i]
                friend_list.append(friend)
            else:
                friend += friends_string[i]
            i += 1
        i = 0
        money = ''
        money_list = []
        while i < len(money_string):
            if money_string[i] == ',':
                money_list.append(int(money))
                money = ''
            elif i == len(money_string) - 1:
                money += money_string[i]
                money_list.append(int(money))
            else:
                money += money_string[i]
            i += 1
        if len(money_list) < n:
            diff = n - len(money_list)
            while diff == 0:
                money_list.append(0)
                diff -= 1
        members = {}
        j = 0
        for i in friend_list:
            members[i] = money_list[j]
            j += 1
        total = 0
        for i in money_list:
            total += i
        print(total, members)
        allocate = Allocator(total, members)
        print_list = allocate.Allocate_money()
        return render_template('dispaly.html', print_list=print_list)


@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)

        db.session.add(user)   #adding user to our database
        db.session.commit()   #saving the changes made in database
        flash("Thanks for registration!")
        return redirect(url_for('login'))
    return render_template('register.html',form=form)


if __name__ == "__main__":
    app.run(debug = True)
