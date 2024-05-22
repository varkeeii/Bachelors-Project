from flask import *
from database import *

customer=Blueprint('customer',__name__)

@customer.route('/customer_home')
def customer_home():
	return render_template('customer_home.html')

@customer.route('/cust_profile',methods=['get','post'])
def cust_profile():
    data={}
    cid=session['cid']
    # q="select * from tbl_customer where Cust_ID='%s'"%(cid)
    # res=select(q)
    # data['up']=res

    q="select * from tbl_customer where Cust_ID='%s'"%(cid)
    res=select(q)
    data['up']=res
        
    if 'update' in request.form:
        f=request.form['fname']
        l=request.form['lname']
        n=request.form['num']
        h=request.form['hname']
        s=request.form['street']
        d=request.form['district']
        st=request.form['state']
        pin=request.form['pin']
        gender=request.form['gender']
        q="update tbl_customer set Cust_Fname='%s',Cust_Lname='%s',Cust_Phone='%s',Cust_Hname='%s',Cust_Street='%s',Cust_Dist='%s',Cust_State='%s',Cust_Pincode='%s',gender='%s' where Cust_ID='%s'"%(f,l,n,h,s,d,st,pin,gender,cid)
        update(q)
        return redirect(url_for("customer.cust_profile"))
    return render_template('cust_profile.html',data=data)



@customer.route('/customer_view_all_product',methods=['get','post'])
def customer_view_all_tbl_item():
	data={}
	q="select * from tbl_category "
	res=select(q)
	data['cat']=res
	
	

	if 'select' in request.form:
		bran=request.form['bran']+'%'
		q="SELECT * FROM tbl_item INNER JOIN tbl_category USING(Cat_ID) INNER JOIN tbl_purchase_child USING(Item_ID) INNER JOIN tbl_purchase_master USING(PM_ID) where Item_Status='1' GROUP BY Item_ID"
	
		res=select(q)
		data['item']=res


	if 'srch' in request.form:
		search='%'+request.form['search']+'%'
		q="SELECT * FROM tbl_item INNER JOIN tbl_category USING(Cat_ID)  where ( Cat_Name like '%s' and  Item_Status='1'  and Stock <> 0)  or ( Item_Name like '%s' and  Item_Status='1'  and Stock <> 0) "%(search,search)
		
		res=select(q)
		data['item']=res
	else:
		q="SELECT * FROM tbl_item INNER JOIN tbl_category USING(Cat_ID)  where Item_ID in (select Item_ID from tbl_purchase_child ) and Item_Status='1' and tbl_category.Cat_Status='1'"
		res=select(q)
		data['item']=res

		print("hello") 


	return render_template('customer_view_all_product.html',data=data)

@customer.route('/customer_view_product',methods=['get','post'])
def customer_view_tbl_item():
	data={}
	id=request.args['id']

	q="SELECT * FROM `tbl_item` WHERE Item_ID IN (SELECT Item_ID FROM `tbl_cart_child` INNER JOIN `tbl_cart_master` USING (CM_ID) WHERE Cust_ID='%s' and Cart_Status='pending') and Item_ID='%s' "%(session['cid'],id)
	print(q)
	data['cartoff']=select(q)
	q="SELECT * FROM tbl_item INNER JOIN tbl_category USING(Cat_ID) where Item_ID='%s' GROUP BY Item_ID"%(id)
	print(q)
	res=select(q)
	data['spro']=res
	return render_template('customer_view_product.html',data=data)


@customer.route('/customer_add_tocart',methods=['get','post'])
def customer_add_tocart():
	data={}
	st=request.args['stock']
	item=request.args['iname']
	amount=request.args['price']
	pid=request.args['id']
	

	if 'btn' in request.form:
		qty=request.form['quantity']
		total=request.form['total']
		if int(st)< int(qty):
			flash('Enter less quantity')
		else:
			q="SELECT * FROM `tbl_cart_master` WHERE `Cart_Status`='pending' and Cust_ID='%s'"%(session['cid'])
			res=select(q)
			if res:
				oid=res[0]['CM_ID']
			else:
				q="INSERT INTO `tbl_cart_master` VALUES(NULL,'%s','0','pending',CURDATE())"%(session['cid'])
				oid=insert(q)
			q="select * from tbl_cart_child where Item_ID='%s' and CM_ID='%s'"%(pid,oid)
			res1=select(q)
			if res1:
				a=res1[0]['qty']
				qty=request.form['quantity']




				c=int(a)+int(qty)
				print(c)

				if int(c) > int(st):
					
					flash('Out Of Stock')
					
				else:
					q="UPDATE `tbl_cart_child` SET `qty`=qty+'%s' , `price`=`price`+'%s' where CC_ID='%s' and Item_ID='%s' "%(qty,total,res1[0]['CC_ID'],pid)
					print(q)
					update(q)
			else:
				q="INSERT INTO `tbl_cart_child` VALUES (NULL,'%s','%s','%s','%s','pending')"%(oid,pid,qty,total)
				insert(q)
			
			q="update tbl_cart_master set Total_amount=Total_amount+'%s' where CM_ID='%s'"%(total,oid)
			print(q)
			update(q)
			# q="select * from tbl_cart_master"
			# res3=select(q)
			# if res3:
			# 	tot_amount=res3[0]['Total_amount']
			# 	price2=tot_amount-300
			# 	q="update tbl_cart_master set Total_amount='%s' where CM_ID='%s'"%(price2,oid)
			# 	print(q)
			# 	update(q)
			flash("Successfully added to Cart")
			return redirect(url_for("customer.customer_view_cart"))

	
	return render_template('customer_add_tocart.html',data=data,item=item,amount=amount)

@customer.route('/customer_view_cart',methods=['get','post'])
def customer_view_cart():
	data={}
	cid=session['cid']
	# q="select sum(price) as sum from tbl_cart_child inner join tbl_cart_master using (CM_ID) where Cust_ID='%s' and Cart_Status='pending'"%(cid)
	# tot=select(q)[0]['sum']
	# print(tot)
	# q="update tbl_cart_master set Total_amount='%s' where Cust_ID='%s' and Cart_Status='pending'"%(tot,cid)
	# update(q)
	q="SELECT * ,`tbl_cart_child`.qty AS qty,tbl_cart_child.price as price,tbl_item.price as it_price FROM  `tbl_cart_master`,`tbl_cart_child`,`tbl_item`,`tbl_purchase_child` WHERE `tbl_purchase_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `tbl_item`.`Item_ID`=`tbl_cart_child`.`Item_ID` AND `tbl_cart_child`.`CM_ID`=`tbl_cart_master`.`CM_ID` AND `Cust_ID`='%s'  AND `Cart_Status`='pending' group by tbl_cart_child.Item_ID"%(session['cid'])
	print(q)
	res=select(q)
	print(len(res))
	data['val']=len(res)
	data['res']=res
 
	if 'action' in request.args:
		action=request.args['action']
		odid=request.args['odid']
		omid=request.args['omid']
		price=request.args['price']
	else:
		action=None

	if action == "remove":
		q="select * from tbl_cart_child where CC_ID='%s'"%(odid)
		print(q)
		amount=select(q)[0]['price']
		q="delete from tbl_cart_child where CC_ID='%s'"%(odid)
		delete(q)
		q="update tbl_cart_master set Total_amount=Total_amount-'%s' where CM_ID='%s'"%(amount,omid)
		update(q)
		q="select * from tbl_cart_child where CM_ID='%s'"%(omid)
		res7=select(q)
		if len(res7) < 1:
			q="delete from tbl_cart_master where CM_ID='%s'"%(omid)
			delete(q)
		return redirect(url_for("customer.customer_view_cart"))


	for i in range(1,len(res)+1):
		if 'del'+str(i) in request.form:
			orderdetails_id=request.form['orderdetails_id'+str(i)]
			totp=request.form['totp']
			total_single_price=request.form['singletotal'+str(i)]
			single_price=request.form['single'+str(i)]
			print("single : ",single_price)

			omid=request.form['om_id']
			print("sssssssssssssssssssssssssssssssssssssssss",omid)

			q="DELETE FROM `tbl_cart_child` WHERE `CC_ID`='%s'"%(orderdetails_id)
			delete(q)
			# c="select * from tbl_cart_child inner join tbl_cart_master(CM_ID) where CC_ID='%s'"%(orderdetails_id)
			# res1=select(c)
			# price=res1[0]['']
			
			q="UPDATE `tbl_cart_master` SET `Total_amount`=`Total_amount`-'%s' WHERE `CM_ID`='%s'"%(single_price,omid)
			update(q)

			q="select * from tbl_cart_master where Total_amount='0' and Cart_Status='pending'"
			val=select(q)
			if val:
				q="delete from tbl_cart_master where CM_ID='%s'"%(omid)
				delete(q)
				return redirect(url_for('customer.customer_view_cart'))

		if 'add'+str(i) in request.form:
			print("Haiii")
			orderdetails_id=request.form['orderdetails_id'+str(i)]
			total_single_price=request.form['singletotal'+str(i)]
			single_price=request.form['single'+str(i)]
			
			print(total_single_price)
			print("SING ; ",single_price)
			omid=request.form['om_id']

			q="select * from tbl_cart_child where `CC_ID`='%s'"%(orderdetails_id)
			print(q)
			res2=select(q)

			# q="DELETE FROM `tbl_cart_child` WHERE `CC_ID`='%s'"%(orderdetails_id)
			# delete(q)

			q="UPDATE `tbl_cart_child` SET `qty`=`qty`+1,price=price+'%s'  WHERE `CC_ID`='%s'"%(single_price,orderdetails_id)
			update(q)

			q="UPDATE `tbl_cart_master` SET `Total_amount`=`Total_amount`+'%s' WHERE `CM_ID`='%s'"%(single_price,omid)
			update(q)
		


			q="select * from tbl_cart_child where qty='0' and  `CC_ID`='%s'"%(orderdetails_id)
			val=select(q)
			if val:
				q="delete from tbl_cart_child where CC_ID='%s'"%(orderdetails_id)
				delete(q)

			q="select * from tbl_cart_master where Total_amount='0' and Cart_Status='pending'"
			val=select(q)
			if val:
				q="delete from tbl_cart_master where CM_ID='%s'"%(omid)
				delete(q)

			return redirect(url_for('customer.customer_view_cart'))

		if 'addss'+str(i) in request.form:
			print("Haiii")
			orderdetails_id=request.form['orderdetails_id'+str(i)]
			total_single_price=request.form['singletotal'+str(i)]
			single_price=request.form['single'+str(i)]
			print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr",single_price)

			omid=request.form['om_id']

			q="select * from tbl_cart_child where `CC_ID`='%s'"%(orderdetails_id)
			print(q)
			res2=select(q)

			# q="DELETE FROM `tbl_cart_child` WHERE `CC_ID`='%s'"%(orderdetails_id)
			# delete(q)

			q="UPDATE `tbl_cart_child` SET `qty`=`qty`-1,price=price-'%s'  WHERE `CC_ID`='%s'"%(single_price,orderdetails_id)
			update(q)

			q="UPDATE `tbl_cart_master` SET `Total_amount`=`Total_amount`-'%s' WHERE `CM_ID`='%s'"%(single_price,omid)
			update(q)


			q="select * from tbl_cart_child where qty='0' and  `CC_ID`='%s'"%(orderdetails_id)
			val=select(q)
			if val:
				q="delete from tbl_cart_child where CC_ID='%s'"%(orderdetails_id)
				delete(q)

			q="select * from tbl_cart_master where Total_amount='0' and Cart_Status='pending'"
			val=select(q)
			if val:
				q="delete from tbl_cart_master where CM_ID='%s'"%(omid)
				delete(q)

			return redirect(url_for('customer.customer_view_cart'))


	if 'btncheckout' in request.form:
		total=request.form['total']
		omid=request.form['om_id']
		q="update tbl_cart_master set Cart_Status='checkout' where CM_ID='%s'"%(omid)
		print(q)
		update(q)
		print(len(res))
		print(len(res)+1)
		for i in range(1,len(res)+1):
			print("Haqiiix",i)
			qty=request.form['qty'+str(i)]
			single_price=request.form['single'+str(i)]
			Item_ID=request.form['pid'+str(i)]
			total_single_price=request.form['singletotal'+str(i)]
			# q="update tbl_cart_child set qty='%s', price='%s' where Item_ID='%s' and CM_ID='%s'"%(qty,total_single_price,Item_ID,omid)
			# print(q)
			# update(q)
			# q="UPDATE `tbl_item` SET `Stock`=`Stock`-'%s' WHERE `Item_ID`='%s'"%(qty,Item_ID)
			# print(q)
			# update(q)

		return redirect(url_for("customer.customer_payment",total=total,omid=omid))

	

	return render_template('customer_view_cart.html',data=data)
    

@customer.route('/customer_payment',methods=['get','post'])
def customer_payment():
	data={}
	total=request.args['total']
	om_id=request.args['omid']

	if 'btn' in request.form:
     
		name=request.form['name']
		number=request.form['number']
		expry=request.form['expry']
		cid=session['cid']
		r="select * from tbl_card where Card_Name like '%s' and Card_No like '%s' and Exp_Date like '%s' and Cust_ID like '%s'"%(name,number,expry,cid)
		res1=select(r)
		if res1:
			q="INSERT INTO `tbl_payment` VALUES(NULL,'%s','%s','%s',CURDATE())"%(om_id,res1[0]['Card_ID'],total)
			insert(q)
			# s="update tbl_cart_master set Cart_Status='Checkout' where CM_ID='%s'"%(om_id)
			# update(s)
			# q="select * from tbl_item inner join tbl_cart_child using(Item_ID) where CM_ID='$s' "%(om_id)
			# res3=select(q)
			# if res3:
			# 	qty=res3[0]['qty']
			# 	itemid=res3[0]['Item_ID']
			# q="UPDATE `tbl_item` SET `Stock`=`Stock`-'%s' WHERE `Item_ID`='%s'"%(qty,itemid)
			# print(q)
			# update(q)
			
		else:
			r="INSERT INTO `tbl_card` VALUES(NULL,'%s','%s','%s','%s','1')"%(cid,number,name,expry)
			print(r)
			res=insert(r)
			q="INSERT INTO `tbl_payment` VALUES(NULL,'%s','%s','%s',CURDATE())"%(om_id,res,total)
			insert(q)
			# s="update tbl_cart_master set Cart_Status='Checkout' where CM_ID='%s'"%(om_id)
			# update(s)
			# q="select * from tbl_item inner join tbl_cart_child using(Item_ID) where CM_ID='%s'"%(om_id)
			# res3=select(q)
			# if res3:
			# 	qty=res3[0]['qty']
			# 	itemid=res3[0]['Item_ID']
			# q="UPDATE `tbl_item` SET `Stock`=`Stock`-'%s' WHERE `Item_ID`='%s'"%(qty,itemid)
			# print(q)
			# update(q)
		q="select * from tbl_cart_master inner join tbl_cart_child using(CM_ID) inner join tbl_item using(Item_ID) where CM_ID='%s'"%(om_id)	
		result=select(q)
		if result:
			for i in result:
				product_id=i['Item_ID']
				quantity=i['qty']
				q="update tbl_item set Stock=Stock-'%s' where Item_ID='%s'"%(quantity,product_id)
				update(q)
				q="select * from tbl_item where Item_ID='%s' and Stock='0'"%(product_id)
				
				res5=select(q)
				if res5:
					q="select * from tbl_purchase_child where Item_ID='%s' and p_status='available' order by PC_ID desc"%(product_id)
					print(q)
					res=select(q)
					if res:
						pdid=res[0]['PC_ID']
						quan=res[0]['Quantity']
						sellp=res[0]['selling_price']
						q="update tbl_item set price='%s', Stock='%s' where Item_ID='%s'"%(sellp,quan,product_id)
						print(q)
						update(q)
						q="update tbl_purchase_child set p_status='stock added' where PC_ID='%s'"%(pdid)
						update(q)
					else:
						a=5
				else:
					b=4 
		flash("payment finished...")
		return redirect(url_for('customer.customer_home'))
			
		
		flash("Order placed Successfully")
		return redirect(url_for('customer.customer_home',total=total,om_id=om_id))

	return render_template('customer_payment.html',data=data,total=total,om_id=om_id)

@customer.route('/customer_view_orders',methods=['get','post'])
def customer_view_orders():
	data={}

	q="SELECT * FROM `tbl_cart_master`, `tbl_cart_child` , `tbl_item` WHERE `tbl_cart_master`.`CM_ID`=`tbl_cart_child`.`CM_ID` AND `tbl_cart_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `Cust_ID`='%s'"%(session['cid'])
	res=select(q)
	data['res']=res

	return render_template('customer_view_orders.html',data=data)

@customer.route('/bill')
def bill():
    data={}
    cmid=request.args['cmid']
    q="SELECT * FROM `tbl_cart_child` INNER JOIN tbl_cart_master USING(CM_ID)  inner join tbl_item using(Item_ID) inner join tbl_customer using(Cust_ID) WHERE Cust_ID='%s' and CM_ID='%s'  ORDER BY CM_ID"%(session['cid'],cmid)
    res=select(q)
    data['res']=res
    q="SELECT * FROM `tbl_cart_child` INNER JOIN tbl_cart_master USING(CM_ID)  inner join tbl_item using(Item_ID) inner join tbl_customer using(Cust_ID) WHERE Cust_ID='%s' and CM_ID='%s'  GROUP BY CM_ID"%(session['cid'],cmid)
    res1=select(q)
    data['res1']=res1
    return render_template("bill.html",data=data)





# @customer.route('/customer_send_complaint',methods=['get','post'])
# def customer_send_complaint():
# 	data={}
# 	if 'submit' in request.form:
# 		complaint=request.form['complaint']
# 		q="INSERT INTO `complaint` VALUES(NULL,'%s','%s','pending',CURDATE())"%(session['cid'],complaint)
# 		insert(q)

# 	q="SELECT * FROM `complaint` WHERE `Cust_ID`='%s'"%(session['cid'])
# 	res=select(q)
# 	data['view']=res

# 	return render_template('customer_send_complaint.html',data=data)
