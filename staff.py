from flask import *
from database import *
import uuid

staff=Blueprint('staff',__name__)

@staff.route('/staff_home')
def staff_home():
	data={}
	q="select count(Cust_ID) as count from tbl_customer"
	res=select(q)
	data['res']=res[0]['count']


	return render_template('staff_home.html',data=data)



@staff.route('/staff_mange_staff',methods=['get','post'])
def staff_mange_staff():
	
    
	if 'register' in request.form:
		f=request.form['fname']
		l=request.form['lname']
		n=request.form['num']
		h=request.form['hname']
		s=request.form['street']
		d=request.form['district']
		st=request.form['state']
		pin=request.form['pin']
		u=request.form['uname']
		p=request.form['pwd']
		

		q="SELECT * FROM `tbl_login` WHERE `Username`='%s' AND `Password`='%s'"%(u,p)
		print(q)
		res=select(q)
		if res:
			flash("Username and Password already exist !")
			return redirect(url_for('staff.staff_mange_staff'))
		else:
			q="insert into tbl_login values('%s','%s','Staff','1')"%(u,p)
			insert(q)
			q="insert into tbl_staff values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s',curdate(),'1')"%(u,f,l,n,h,s,d,st,pin)
			insert(q)
			flash("Staff Details added Successfully...")

	data={}
	q="select * from tbl_staff"
	res=select(q)
	data['res']=res
	
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
		un=request.args['un']

	else:
		action=None

	if action=="inactive":
		q="update tbl_staff set Staff_Status='0' where Staff_ID='%s'"%(cid)
		update(q)
		q="update tbl_login set Status='0' where Username='%s'"%(un)
		update(q)

		return redirect(url_for("staff.staff_mange_staff"))
	if action=="active":
		q="update tbl_staff set Staff_Status='1' where Staff_ID='%s'"%(cid)
		update(q)
		q="update tbl_login set Status='1' where Username='%s'"%(un)
		update(q)
		return redirect(url_for("staff.staff_mange_staff"))

	if action=="update":
		q="select * from tbl_staff where Staff_ID='%s'"%(cid)
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
		q="update tbl_staff set Staff_Fname='%s',Staff_Lname='%s',Staff_Phone='%s',Staff_Hname='%s',Staff_Street='%s',Staff_Dist='%s',Staff_State='%s',Staff_Pin='%s' where Staff_ID='%s'"%(f,l,n,h,s,d,st,pin,cid)
		update(q)
		flash("Updated Successfully...")
		return redirect(url_for("staff.staff_mange_staff"))
	return render_template('staff_mange_staff.html',data=data)



@staff.route('/staff_manage_vendors',methods=['get','post'])
def staff_manage_vendors():
	if 'submit' in request.form:
		vn=request.form['vname']
		m=request.form['email']
		n=request.form['num']
		h=request.form['hname']
		d=request.form['district']
		st=request.form['state']
		pin=request.form['pin']
		
		

		q="insert into tbl_vendor values(null,'0','%s','%s','%s','%s','%s','%s','%s',curdate(),'1')"%(vn,m,n,h,d,st,pin)
		insert(q)
		flash("Vendor Details added Successfully...")
		return redirect(url_for("staff.staff_manage_vendors"))
	data={}
	q="select * from tbl_vendor"
	res=select(q)
	data['res']=res
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']

	else:
		action=None

	if action=="inactive":
		q="update tbl_vendor set Vendor_Status='0' where Vendor_ID='%s'"%(cid)
		update(q)
		return redirect(url_for("staff.staff_manage_vendors"))
	if action=="active":
		q="update tbl_vendor set Vendor_Status='1' where Vendor_ID='%s'"%(cid)
		update(q)
		return redirect(url_for("staff.staff_manage_vendors"))

	if action=="update":
		q="select * from tbl_vendor where Vendor_ID='%s'"%(cid)
		res=select(q)
		data['up']=res
		
	if 'update' in request.form:
		c=request.form['vname']
		e=request.form['email']
		n=request.form['num']
		a=request.form['hname']
		d=request.form['district']
		st=request.form['state']
		pin=request.form['pin']
		q="update tbl_vendor set Vendor_Name='%s',Vendor_Email='%s',Vendor_Phone='%s',Vendor_Hname='%s',Vendor_Dist='%s',Vendor_State='%s',Vendor_Pin='%s' where Vendor_ID='%s'"%(c,e,n,a,d,st,pin,cid)
		update(q)
		flash("Updated Successfully...")
		return redirect(url_for("staff.staff_manage_vendors"))
	return render_template('staff_manage_vendors.html',data=data)

@staff.route('/staff_manage_courier',methods=['get','post'])
def staff_manage_courier():
	if 'submit' in request.form:
		cn=request.form['cname']
		n=request.form['num']
		a=request.form['addr']
		d=request.form['district']
		s=request.form['state']
		pin=request.form['pin']
		u=request.form['uname']
		p=request.form['pwd']
		r="select * from tbl_login where Username='%s'"%(u)
		res=select(r)
		if res:
			flash("Username already exists...")
			return redirect(url_for("staff.staff_manage_courier"))
		else:
		
			q="insert into tbl_login values('%s','%s','Courier','1')"%(u,p)
			insert(q)
			q="insert into tbl_courier values(null,'%s','0','%s','%s','%s','%s','%s','%s','1')"%(u,cn,n,a,d,s,pin)
			insert(q)
			flash("Courier Details added Successfully...")
			return redirect(url_for("staff.staff_manage_courier"))
	data={}
	q="select * from tbl_courier"
	res=select(q)
	data['res']=res
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
		un=request.args['un']

	else:
		action=None

	if action=="inactive":
		# q="SELECT * FROM `tbl_cart_master` INNER JOIN `tbl_payment` USING (CM_ID) INNER JOIN `tbl_delivery` USING (Payment_id) INNER JOIN `tbl_courier` USING (Cour_ID) WHERE `Cour_ID` IN ( SELECT `Cour_ID` FROM `tbl_delivery` ) AND `tbl_cart_master`.Cart_Status <> 'delivered'"
		q="SELECT * FROM  `tbl_cart_master` INNER JOIN `tbl_cart_child` USING (CM_ID) INNER JOIN `tbl_payment` USING (`CM_ID`) INNER JOIN `tbl_delivery` USING (Payment_ID) WHERE Cart_Status = 'dispatch' AND Cour_ID='%s'"%(cid)
		val=select(q)
		for w in val:
			q="update tbl_cart_master set Cart_Status='checkout' where CM_ID='%s'"%(w['CM_ID'])
			update(q)
			q="delete from tbl_delivery where Cour_id='%s'"%(cid)
			delete(q)
		q="update tbl_courier set Cour_Status='0' where Cour_id='%s' "%(cid)
		update(q)
		q="update tbl_login set Status='0' where Username=(select Username from tbl_courier where Cour_id='%s')"%(cid)
		update(q)
		# exist=select(q)
		# if exist:
		# 	flash("Cant Deactivate Couriers on Delivery")
		# else:
		# 	q="update tbl_courier set Cour_Status='0' where Cour_ID='%s'"%(cid)
		# 	update(q)
		# 	q="update tbl_login set Status='0' where Username='%s'"%(un)
		# 	update(q)
		return redirect(url_for("staff.staff_manage_courier"))
	if action=="active":
		q="update tbl_courier set Cour_Status='1' where Cour_ID='%s'"%(cid)
		update(q)
		q="update tbl_login set Status='1' where Username='%s'"%(un)
		update(q)
		return redirect(url_for("staff.staff_manage_courier"))

	if action=="update":
		q="select * from tbl_courier where Cour_ID='%s'"%(cid)
		res=select(q)
		data['up']=res
		
	if 'update' in request.form:
		c=request.form['cname']
		n=request.form['num']
		a=request.form['addr']
		d=request.form['district']
		s=request.form['state']
		pin=request.form['pin']
		q="update tbl_courier set Cour_Name='%s',Cour_Phone='%s',Cour_Address='%s',Cour_Dist='%s',Cour_State='%s',Cour_Pin='%s' where Cour_ID='%s'"%(c,n,a,d,s,pin,cid)
		update(q)
		flash("Updated Successfully...")
		return redirect(url_for("staff.staff_manage_courier"))
	return render_template('staff_manage_courier.html',data=data)

@staff.route('/staff_manage_category',methods=['get','post'])
def staff_manage_category():
	if 'submit' in request.form:
		cat=request.form['cat']
		desc=request.form['desc']
		r="select * from tbl_category where Cat_Name='%s'"%(cat)
		res=select(r)
		if res:
			flash("Category already exists...")
			return redirect(url_for("staff.staff_manage_category"))
		else:
			q="insert into tbl_category values(null,'%s','%s','1')"%(cat,desc)
			insert(q)
			flash("Category Added Successfully...")
			return redirect(url_for("staff.staff_manage_category"))
	data={} 

	q="select * from tbl_category"
	res=select(q)
	data['res']=res
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']

	else:
		action=None

	if action=="inactive":
		q="update tbl_category set Cat_Status='0' where Cat_ID='%s'"%(cid)
		update(q)
		return redirect(url_for("staff.staff_manage_category"))
	if action=="active":
		q="update tbl_category set Cat_Status='1' where Cat_ID='%s'"%(cid)
		update(q)
		return redirect(url_for("staff.staff_manage_category"))

	if action=="update":
		q="select * from tbl_category where Cat_ID='%s'"%(cid)
		res=select(q)
		data['up']=res
		
	if 'update' in request.form:
		c=request.form['cat']
		desc=request.form['desc']
		
		q="update tbl_category set Cat_Name='%s',Cat_desc='%s' where Cat_ID='%s'"%(c,desc,cid)
		update(q)
		flash("Category Updated Successfully...")
		return redirect(url_for("staff.staff_manage_category"))
	return render_template('staff_manage_category.html',data=data)

# @staff.route('/staff_manage_type',methods=['get','post'])
# def staff_manage_type():
	
# 	if 'submit' in request.form:
# 		typ=request.form['typ']
# 		r="select * from tbl_type where Type_Name='%s'"%(typ)
# 		res=select(r)
# 		if res:
# 			flash("Type already exists...")
# 			return redirect(url_for("staff.staff_manage_type"))
# 		else:
# 			q="insert into tbl_type values(null,'%s','1')"%(typ)
# 			insert(q)
# 			flash("Type Added Successfully...")
# 			return redirect(url_for("staff.staff_manage_type"))
# 	data={}
# 	q="select * from tbl_type"
# 	res=select(q)
# 	data['res']=res
# 	if "action" in request.args:
# 		action=request.args['action']
# 		cid=request.args['cid']

# 	else:
# 		action=None

# 	if action=="inactive":
# 		q="update tbl_type set Type_Status='0' where Type_ID='%s'"%(cid)
# 		update(q)
# 		return redirect(url_for("staff.staff_manage_type"))
# 	if action=="active":
# 		q="update tbl_type set Type_Status='1' where Type_ID='%s'"%(cid)
# 		update(q)
# 		return redirect(url_for("staff.staff_manage_type"))

# 	if action=="update":
# 		q="select * from tbl_type where Type_ID='%s'"%(cid)
# 		res=select(q)
# 		data['up']=res
		
# 	if 'update' in request.form:
# 		t=request.form['typ']
		
# 		q="update tbl_type set Type_Name='%s' where Type_ID='%s'"%(t,cid)
# 		update(q)
# 		flash("Type Updated Successfully...")
# 		return redirect(url_for("staff.staff_manage_type"))
# 	return render_template('staff_manage_type.html',data=data)

# @staff.route('/staff_manage_brand',methods=['get','post'])
# def staff_manage_brand():
	
# 	if 'submit' in request.form:
# 		bran=request.form['bran']
# 		r="select * from tbl_brand where Brand_Name='%s'"%(bran)
# 		res=select(r)
# 		if res:
# 			flash("Brand already exists...")
# 			return redirect(url_for("staff.staff_manage_brand"))
# 		else:
# 			q="insert into tbl_brand values(null,'%s','1')"%(bran)
# 			insert(q)
# 			flash("Brand Added Successfully...")
# 			return redirect(url_for("staff.staff_manage_brand"))
# 	data={}
# 	q="select * from tbl_brand"
# 	res=select(q)
# 	data['res']=res
# 	if "action" in request.args:
# 		action=request.args['action']
# 		cid=request.args['cid']

# 	else:
# 		action=None

# 	if action=="inactive":
# 		q="update tbl_brand set Brand_Status='0' where Brand_ID='%s'"%(cid)
# 		update(q)
# 		return redirect(url_for("staff.staff_manage_brand"))
# 	if action=="active":
# 		q="update tbl_brand set Brand_Status='1' where Brand_ID='%s'"%(cid)
# 		update(q)
# 		return redirect(url_for("staff.staff_manage_brand"))

# 	if action=="update":
# 		q="select * from tbl_brand where Brand_ID='%s'"%(cid)
# 		res=select(q)
# 		data['up']=res
		
# 	if 'update' in request.form:
# 		b=request.form['bran']
		
# 		q="update tbl_brand set Brand_Name='%s' where Brand_ID='%s'"%(b,cid)
# 		update(q)
# 		flash("Brand Updated Successfully...")
# 		return redirect(url_for("staff.staff_manage_brand"))
# 	return render_template('staff_manage_brand.html',data=data)


# @staff.route('/staff_manage_color',methods=['get','post'])
# def staff_manage_color():
#     if 'submit' in request.form:
#         color=request.form['color']
#         r="select * from tbl_color where Color_Name='%s'"%(color)
#         res=select(r)
#         if res:
#             flash("Color already exists...")
#             return redirect(url_for("staff.staff_manage_color"))
#         else:
#             q="insert into tbl_color values(null,'%s','1')"%(color)
#             insert(q)
#             flash("Color Added Successfully...")
#             return redirect(url_for("staff.staff_manage_color"))
#     data={}
#     q="select * from tbl_color"
#     res=select(q)
#     data['res']=res
#     if "action" in request.args:
#         action=request.args['action']
#         cid=request.args['cid']

#     else:
#         action=None
    
#     if action=="inactive":
#         q="update tbl_color set Color_Status='0' where Color_ID='%s'"%(cid)
#         update(q)
#         return redirect(url_for("staff.staff_manage_color"))
#     if action=="active":
#         q="update tbl_color set Color_Status='1' where Color_ID='%s'"%(cid)
#         update(q)
#         return redirect(url_for("staff.staff_manage_color"))
    
#     if action=="update":
#         q="select * from tbl_color where Color_ID='%s'"%(cid)
#         res=select(q)
#         data['up']=res
        
#     if 'update' in request.form:
#         b=request.form['color']
        
#         q="update tbl_color set Color_Name='%s' where Color_ID='%s'"%(b,cid)
#         update(q)
#         flash("Colour Updated Successfully...")
#         return redirect(url_for("staff.staff_manage_color"))
#     return render_template('staff_manage_color.html',data=data)




@staff.route('/staff_manage_item',methods=['get','post'])
def staff_manage_item():
	
	data={}

		
		
	q="select * from tbl_category where Cat_Status='1'"
	res=select(q)
	data['cat']=res


	if 'submit' in request.form:
		cat=request.form['cat']
		itemname=request.form['itemname']
		des=request.form['des']
		img=request.files['img']
		path='static/uploads/'+str(uuid.uuid4())+img.filename 
		img.save(path)

		q="select * from tbl_item where Item_Name='%s'"%(itemname)
		val=select(q)
		if val:
			flash("This Item already Exist")
		else:

			profper=request.form['profper']
			q="insert into tbl_item values(null,'%s','%s','%s','%s','0','%s','0','1')"%(itemname,cat,des,path,profper)
			insert(q)
			flash("Item Added Successfully")
		return redirect(url_for("staff.staff_manage_item"))


	q="select * from tbl_item inner join tbl_category using(Cat_ID) where tbl_category.Cat_Status='1'"
	res=select(q)
	data['res']=res
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']

	else:
		action=None

	if action=="inactive":
		q="update tbl_item set Item_Status='0' where Item_ID='%s'"%(cid)
		update(q)
		return redirect(url_for("staff.staff_manage_item"))
	if action=="active":
		q="update tbl_item set Item_Status='1' where Item_ID='%s'"%(cid)
		update(q)
		return redirect(url_for("staff.staff_manage_item"))

	if action=="update":
		q="select * from tbl_item where Item_ID='%s'"%(cid)
		res=select(q)
		data['up']=res
		
	if 'update' in request.form:
		
		i=request.form['itemname']
		des=request.form['des']
		p=request.form['profper']
		
  
		q="SELECT * FROM tbl_item  WHERE Item_ID='%s'"%(cid)
		res=select(q)
		pro=res[0]['Profit_Percentage']

		q="update tbl_item set Item_Name='%s',Description='%s',Profit_Percentage='%s' where Item_ID='%s'"%(i,des,p,cid)
		update(q)
		flash("Item Updated Successfully...")

		q="SELECT * FROM tbl_purchase_child  WHERE Item_ID='%s' GROUP BY Cost_Price"%(cid)
		res=select(q)
		if res:
			data['c1']=res
			for i in data['c1']:
				cp=i['Cost_Price']
				sp=int(float(cp))+(int(float(cp))*(int(float(pro))/100))
				nsp=int(float(cp))+(int(float(cp))*(int(float(p))/100))
				q="update tbl_purchase_child set selling_price='%s' WHERE selling_price='%s'"%(nsp,sp)
				update(q)
				qq="update tbl_item set price='%s' where Item_ID='%s'"%(nsp,cid)
				update(qq)
				q="select * from tbl_cart_child where Item_ID='%s' and delivery_status = 'pending'"%(cid)
				res2=select(q)
				print(res2)
				if res2:
					oldprice=res2[0]['price']
					val=res2[0]['qty']*sp
					q="update  tbl_cart_child set price='%s' where Item_ID='%s'"%(val,cid)
					update(q)
					q="select * from tbl_cart_child"
					res4=select(q)
					if res4:
						newprice=res4[0]['price']
					q="select * from tbl_cart_master"
					res3=select(q)
					if res3:
						tot_amount=res3[0]['Total_amount']
						cmid=res3[0]['CM_ID']
						price1=tot_amount-oldprice
						newtot=price1+newprice
						q="update tbl_cart_master set Total_amount='%s' where CM_ID='%s' "%(newtot,cmid)
						res=update(q)
						print(res)
				

				# q="update tbl_cart_child set price=*'%s' WHERE Item_ID='%s'"%(cid)
				# update(q)

		return redirect(url_for('staff.staff_manage_item'))
				
				
		
		
	return render_template('staff_manage_item.html',data=data)

	

@staff.route('/staff_manage_purchase',methods=['get','post'])
def staff_manage_purchase():
	data={}
	q="select * from tbl_vendor where Vendor_Status='1'"
	res=select(q)
	data['vname']=res
	r="select * from tbl_item inner join tbl_category using (Cat_ID) where Item_Status='1' and tbl_category.Cat_Status='1'"
	res=select(r)
	data['itemid']=res
	if 'submit' in request.form:
		vn=request.form['vname']
		cp=int(request.form['costp'])
		quan=request.form['quan']
		tot=request.form['tot']
		itemid=request.form['itemid']
		
		q="select * from  tbl_item where Item_ID='%s'"%(itemid)
		print(q)
		c=select(q)
		profitPer =int(c[0]['Profit_Percentage'])
		print(profitPer)

		percentage = (cp*profitPer)/100
		
		selling_price=cp+percentage
		
		s="select * from tbl_purchase_master where Pur_Status='pending' and Vendor_ID='%s'"%(vn)
		res=select(s)
		if res:
			pmid=res[0]['PM_ID']
		else:
			q="insert into tbl_purchase_master values(null,'%s','0',0,curdate(),'pending')"%(vn)
			pmid=insert(q)
			
		q="select * from tbl_purchase_child where PM_ID ='%s' and Item_ID='%s' and Cost_Price='%s' "%(pmid,itemid,cp)
		val=select(q)
		if val:
			q="update tbl_purchase_child set Quantity=Quantity+'%s' where PM_ID='%s'"%(quan,pmid)
			update(q)
			# q="update tbl_item set Stock=Stock+'%s' where Item_ID='%s'"%(quan,itemid)
			# update(q)
			
		else:
			q="insert into tbl_purchase_child values(null,'%s','%s','%s','%s','%s','available')"%(pmid,itemid,quan,cp,selling_price)
			insert(q)
			# q="update tbl_item set Stock=Stock+'%s' where Item_ID='%s'"%(quan,itemid)
			# update(q)
		
		q="update tbl_purchase_master set Tot_amount=Tot_amount+'%s' where PM_ID='%s'"%(tot,pmid)
		update(q)
		return redirect(url_for("staff.staff_manage_purchase"))
		
	q="select * from tbl_purchase_child inner join tbl_purchase_master using(PM_ID) inner join tbl_vendor using(Vendor_ID) inner join tbl_item using(Item_ID) where Pur_Status='pending'"
	print(q)
	res=select(q)
	data['res']=res
	q="select * from tbl_purchase_child inner join tbl_purchase_master using(PM_ID) inner join tbl_vendor using(Vendor_ID) inner join tbl_item using(Item_ID) where Pur_Status='pending' group by PM_ID"
	print(q)
	res1=select(q)
	data['res1']=res1

	if 'action' in request.args:
		action=request.args['action']
		pmid=request.args['pmid']
	else:
		action=None
		
	if action == "checkout":
		# q="update tbl_purchase_master set Pur_Status='Purchased' where PM_ID='%s'"%(pmid)
		# update(q)
		q="select * from tbl_purchase_master inner join tbl_purchase_child using(PM_ID) inner join tbl_vendor using (Vendor_Id) where Pur_Status='pending'"
		res=select(q)
		if res:
			for i in res:
				proid=i['Item_ID']
				sellpingprice=i['selling_price']
				quantity=i['Quantity']
				pdetailsid=i['PC_ID']
				v=i['Vendor_Name']
				am=i['Tot_amount']
				
				q="select * from tbl_item where Item_ID='%s' and Stock='0'"%(proid)
				res1=select(q)
				if res1:
					q="update tbl_item set Stock='%s',price='%s' where  Item_ID='%s'"%(quantity,sellpingprice,proid)
					update(q)
					q="update tbl_purchase_child set p_status='stock added' where PC_ID='%s'"%(pdetailsid)
					update(q)
					q="update tbl_purchase_master set Pur_Status='paid' where PM_ID='%s'"%(res[0]['PM_ID'])
					update(q)
					# flash('Purchase Completed...')
				else:
					q="update tbl_purchase_master set Pur_Status='paid' where PM_ID='%s'"%(res[0]['PM_ID'])
					update(q)
				flash('Purchase Completed by  ' +v+' amount: '+am)
				q="select * from tbl_cart_child where Item_ID='%s'"%(proid)
				variable1=select(q)
				for j in variable1:
					cart_qty=j['qty']
					q="update tbl_cart_child set price='%s'*'%s' where Item_ID='%s'"%(sellpingprice,cart_qty,proid)
					update(q)
				return redirect(url_for("staff.staff_manage_purchase"))


	return render_template('staff_manage_purchase.html',data=data)

@staff.route('/staff_view_user',methods=['get','post'])
def staff_view_user():
	data={}
	q="select * from tbl_customer inner join tbl_login using(Username)"
	res=select(q)
	data['res']=res
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
		un=request.args['un']

	else:
		action=None

	if action=="inactive":
		q="update tbl_customer set Cust_Status='0' where Cust_ID='%s'"%(cid)
		update(q)
		q="update tbl_login set Status='0' where Username='%s'"%(un)
		update(q)
		return redirect(url_for("staff.staff_view_user"))
	if action=="active":
		s="update tbl_customer set Cust_Status='1' where Cust_ID='%s'"%(cid)
		update(s)
		q="update tbl_login set Status='1' where Username='%s'"%(un)
		update(q)
		return redirect(url_for("staff.staff_view_user"))
	return render_template('staff_view_user.html',data=data)

@staff.route('/staff_view_booking',methods=['get','post'])
def staff_view_booking():
	data={}
	q="SELECT * FROM `tbl_cart_master`, `tbl_cart_child` ,`tbl_customer`,`tbl_item`, tbl_payment WHERE `tbl_customer`.`Cust_ID`=`tbl_cart_master`.`Cust_ID`  AND`tbl_cart_master`.`CM_ID`=`tbl_cart_child`.`CM_ID` AND `tbl_cart_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `tbl_cart_master`.`CM_ID`=`tbl_payment`.`CM_ID`"
	print(q)
	res=select(q)
	data['view']=res

	return render_template('staff_view_booking.html',data=data)


@staff.route('/staff_order_custom_details',methods=['get','post'])
def staff_order_custom_details():
	data={}
	cid=request.args['cid']
	q="SELECT * FROM `tbl_customer` WHERE `Cust_ID`='%s'"%(cid)
	res=select(q)
	data['view']=res

	return render_template('staff_order_custom_details.html',data=data)

@staff.route('/staff_view_payment',methods=['get','post'])
def staff_view_tbl_payment():
	data={}
	cid=request.args['cid']
	omid=request.args['omid']
	# q="SELECT * FROM `tbl_customer`,`tbl_cart_master`,`tbl_payment` WHERE `tbl_customer`.`Cust_ID`=`tbl_cart_master`.`Cust_ID` AND `tbl_cart_master`.`CM_ID`=`tbl_payment`.`CM_ID` and Cust_ID='%s' and CM_ID='%s'"%(cid,omid)
	q="SELECT * FROM `tbl_customer`,`tbl_cart_master`,`tbl_payment` WHERE `tbl_customer`.`Cust_ID`=`tbl_cart_master`.`Cust_ID` AND `tbl_cart_master`.`CM_ID`=`tbl_payment`.`CM_ID` AND `tbl_cart_master`.`Cust_ID`='%s' AND `tbl_payment`.`CM_ID`='%s'"%(cid,omid)
	res=select(q)
	data['view']=res

	return render_template('staff_view_payment.html',data=data)

@staff.route('/staff_viewd_delivery_status',methods=['get','post'])
def staff_viewd_delivery_status():
	data={}
	omid=request.args['omid']
	q="SELECT * FROM `tbl_cart_master` WHERE `CM_ID`='%s'"%(omid)
	res=select(q)
	data['res']=res
	return render_template('staff_viewd_delivery_status.html',data=data)	





# @staff.route('/staff_complaint',methods=['get','post'])
# def staff_complaint():
# 	data={}

# 	q="SELECT * FROM `complaint` INNER JOIN `tbl_customer` USING (`Cust_ID`)"
# 	res=select(q)
# 	data['view']=res

# 	j=0
# 	for i in range(1,len(res)+1):
# 		print('submit'+str(i))
# 		if 'submit'+str(i) in request.form:
# 			reply=request.form['reply'+str(i)]
# 			print(reply)
# 			print(j)
# 			print(res[j]['complaint_id'])
# 			q="UPDATE `complaint` SET `reply`='%s' WHERE `complaint_id`='%s'" %(reply,res[j]['complaint_id'])
# 			print(q)
# 			update(q)
# 			flash("success")
# 			return redirect(url_for('staff.staff_complaint')) 	
# 		j=j+1

# 	return render_template('staff_complaint.html',data=data)

@staff.route('/staff_view_sales_report',methods=['get','post'])
def staff_view_sales_report():
	data={}
	# if 'sale' in request.form:
	# 	daily=request.form['daily']
	# 	if request.form['monthly']=="":
	# 		monthly=""
	# 	else:
	# 		monthly=request.form['monthly']+'%'
	# 	print(monthly)
	# 	customer=request.form['customer']+'%'
		
	# 	q="SELECT * FROM `tbl_cart_child` INNER JOIN `tbl_payment` USING(`CM_ID`) INNER JOIN `tbl_cart_master` USING(`CM_ID`) INNER JOIN `tbl_item` USING(`Item_ID`) INNER JOIN `tbl_category` USING (`Cat_ID`) INNER JOIN `tbl_type` USING (`Type_ID`) INNER JOIN `tbl_color` USING (`Color_ID`) INNER JOIN `tbl_brand` USING (`Brand_ID`) INNER JOIN `tbl_customer` USING(`Cust_ID`) WHERE `Cust_Fname` LIKE '%s' OR `tbl_payment`.`Payment_Date` LIKE '%s' OR `tbl_payment`.`Payment_Date` LIKE '%s'"%(customer,daily,monthly)
	# 	print(q)
	# 	res=select(q)
	# 	data['report']=res
	# 	session['res']=res
	# 	r=session['res']
	# else:
	# 	q="SELECT * FROM `tbl_cart_child` INNER JOIN `tbl_cart_master` USING(`CM_ID`) INNER JOIN `tbl_item` USING(`Item_ID`) INNER JOIN `tbl_category` USING (`Cat_ID`) INNER JOIN `tbl_type` USING (`Type_ID`) INNER JOIN `tbl_color` USING (`Color_ID`) INNER JOIN `tbl_brand` USING (`Brand_ID`) INNER JOIN `tbl_customer` USING(`Cust_ID`)"
	# 	res=select(q)
	# 	data['report']=res


	# q="select sum(Total_amount) as total_amounts from tbl_cart_master"
	# data['total_amount']=select(q)

	q1="SELECT * FROM `tbl_payment` ORDER BY Payment_Date ASC"
	res1=select(q1)
	if res1:
		data['maxd']=res1[0]['Payment_Date']




	if 'sale' in request.form:
		daily=request.form['dailys']+'%'
		print(daily)
		monthly=request.form['monthlys']+'%'
		print(monthly)
		customer=request.form['customer']+'%'
		

		if daily == '%' and monthly == "%" and customer == "%":
			flash("###############################")
			print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
		else:
			if daily != '%':
				q="""SELECT * , sum(amount) as total_amounts FROM `tbl_cart_child`,`tbl_cart_master`,`tbl_payment`,`tbl_customer` ,`tbl_item`,`tbl_category` WHERE 
    (`tbl_customer`.`Cust_ID`=`tbl_cart_master`.`Cust_ID` AND `tbl_payment`.`CM_ID`=`tbl_cart_master`.`CM_ID` and `tbl_cart_master`.`CM_ID`
    =`tbl_cart_child`.`CM_ID` and `tbl_cart_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `tbl_item`.`Cat_ID`=`tbl_category`.`Cat_ID`  AND 
    `Payment_Date` LIKE '%s')group BY tbl_cart_child.CM_ID  """%(daily)
				res=select(q)
				data['report']=res
				session['res']=res
				r=session['res']
				data['total']=res
			elif monthly != "%":
				q="SELECT * , sum(amount) as total_amounts FROM `tbl_cart_child`,`tbl_cart_master`,`tbl_payment`,`tbl_customer`,`tbl_item`,`tbl_category` WHERE  (`tbl_customer`.`Cust_ID`=`tbl_cart_master`.`Cust_ID` AND `tbl_payment`.`CM_ID`=`tbl_cart_master`.`CM_ID` and `tbl_cart_master`.`CM_ID`=`tbl_cart_child`.`CM_ID` AND `tbl_cart_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `tbl_item`.`Cat_ID`=`tbl_category`.`Cat_ID` and `tbl_cart_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `tbl_item`.`Cat_ID`=`tbl_category`.`Cat_ID`  AND `Payment_Date` LIKE '%s' ) group BY tbl_cart_child.CM_ID"""%(monthly)
				print(q)
				res=select(q)
				data['total']=res			
				data['report']=res
				print(data['total'])
				session['res']=res
				r=session['res']
				
			elif customer != "%":
				q="SELECT * , SUM(amount) AS total_amounts FROM `tbl_cart_child`,`tbl_cart_master`,`tbl_payment`,`tbl_customer`,`tbl_item`,`tbl_category` WHERE  (`tbl_customer`.`Cust_ID`=`tbl_cart_master`.`Cust_ID` AND `tbl_payment`.`CM_ID`=`tbl_cart_master`.`CM_ID` AND `tbl_cart_master`.`CM_ID`=`tbl_cart_child`.`CM_ID` AND `tbl_cart_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `tbl_item`.`Cat_ID`=`tbl_category`.`Cat_ID`AND `Cust_Fname` LIKE '%s' ) group BY tbl_cart_child.CC_ID"%(customer)
				res=select(q)
				data['total']=res

				data['report']=res
				session['res']=res
				r=session['res']
    
			# q="SELECT * FROM `tbl_purchase_child`,`tbl_purchase_master`,`tbl_vendor`,`tbl_item` WHERE (`tbl_vendor`.`Vendor_ID`=`tbl_purchase_master`.`Vendor_ID` AND `tbl_purchase_master`.`PM_ID`=`tbl_purchase_child`.`PM_ID` AND `tbl_purchase_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `Pur_Date` LIKE '%s') OR (`tbl_vendor`.`Vendor_ID`=`tbl_purchase_master`.`Vendor_ID` AND `tbl_purchase_master`.`PM_ID`=`tbl_purchase_child`.`PM_ID` AND `tbl_purchase_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `Pur_Date` LIKE '%s') OR (`tbl_vendor`.`Vendor_ID`=`tbl_purchase_master`.`Vendor_ID` AND `tbl_purchase_master`.`PM_ID`=`tbl_purchase_child`.`PM_ID` AND `tbl_purchase_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `Vendor_Name` LIKE '%s') "%(daily,monthly,vendor)
			# print(q)
			# res=select(q)
			# if res:
			# 	data['report']=res
			# 	session['res']=res
			# 	r=session['res']

	else: 
		q="SELECT * FROM `tbl_cart_child`,`tbl_cart_master`,`tbl_payment`,`tbl_customer`,`tbl_item`,`tbl_category` WHERE `tbl_customer`.`Cust_ID`=`tbl_cart_master`.`Cust_ID` AND `tbl_payment`.`CM_ID`=`tbl_cart_master`.`CM_ID` and `tbl_cart_master`.`CM_ID`=`tbl_cart_child`.`CM_ID` and `tbl_cart_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `tbl_item`.`Cat_ID`=`tbl_category`.`Cat_ID`  "
		res=select(q)
		data['report']=res

		q="select sum(amount) as total_amounts from tbl_payment"
		data['total']=select(q)

  
		
		

	return render_template('staff_view_sales_report.html',data=data)




@staff.route('/staff_salesreport',methods=['get','post'])
def staff_salesreport():
	data={}
	
	r=session['res']
	data['r']=r


	return render_template('staff_salesreport.html',data=data)

@staff.route('/staff_view_customer_report',methods=['get','post'])
def staff_view_customer_report():
	data={}
	if 'sale' in request.form:
		
		customer=request.form['customer']+'%'
		
		q="SELECT * FROM `tbl_customer` WHERE `Cust_Fname` LIKE '%s'"%(customer)
		print(q)
		res=select(q)
		data['report']=res
		session['res']=res
		r=session['res']
	else:
		q="SELECT * FROM `tbl_customer`"
		res=select(q)
		data['report']=res
		
		

	return render_template('staff_view_customer_report.html',data=data)

@staff.route('/staff_customerreport',methods=['get','post'])
def staff_customerreport():
	data={}
	
	r=session['res']
	data['r']=r


	return render_template('staff_customerreport.html',data=data)

@staff.route('/staff_assign_courier',methods=['get','post'])
def staff_assign_courier():
	data={}
	q="select * from tbl_courier where Cour_Status='1'"
	res=select(q)
	data['cname']=res
	payment_id=request.args['payment_id']
	omid=request.args['omid']
	if 'submit' in request.form:
		cn=request.form['cname']
		q="INSERT INTO `tbl_delivery` VALUES(NULL,'%s','%s',CURDATE())"%(payment_id,cn)
		insert(q)
		q="update `tbl_cart_master` set `Cart_Status`='dispatch' where CM_ID='%s'"%(omid)
		print(q)
		update(q)
		return redirect(url_for('staff.staff_home',payment_id=payment_id))
		# s="select * from tbl_courier where Cour_Name='%s'"%(cn)
		# res=select(s)
		# if res:
		# 	couid=res[0]['Cour_ID']
		

	return render_template('staff_assign_courier.html',data=data)

@staff.route('/staff_view_staff_report',methods=['get','post'])
def staff_view_staff_report():
	data={}
	if 'sale' in request.form:
		
		customer=request.form['staff']+'%'
		
		q="SELECT * FROM `tbl_staff` WHERE `Staff_Fname` LIKE '%s'"%(customer)
		print(q)
		res=select(q)
		data['report']=res
		session['res']=res
		r=session['res']
	else:
		q="SELECT * FROM `tbl_staff`"
		res=select(q)
		data['report']=res
		session['res']=res
		r=session['res']
		
		

	return render_template('staff_view_staff_report.html',data=data)


@staff.route('/staff_staffreport',methods=['get','post'])
def staff_staffreport():
	data={}
	
	r=session['res']
	data['r']=r


	return render_template('staff_staffreport.html',data=data)


@staff.route('/staff_view_purchase_report',methods=['get','post'])
def staff_view_purchase_report():
	data={}
 
	q1="SELECT * FROM `tbl_purchase_master` ORDER BY `Pur_Date` DESC"
	res1=select(q1)
	if res1:
		result=0
		for i in res1:
			val=i['Tot_amount']
			result=int(result)+int(val)
			data['total_amountss'] = result
			data['total']=res1
	print(res1[0]['Pur_Date'])
	data['maxd']=res1[0]['Pur_Date']
	
	
	
 
	if 'sale' in request.form:
		daily=request.form['dailys']+'%'
		print(daily)
		monthly=request.form['monthlys']+'%'
		print(monthly)
		vendor=request.form['vendor']+'%'
		

		if daily == '%' and monthly == "%" and vendor == "%":
			
			print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
		else:
			if daily != '%':
				q="""SELECT *  FROM `tbl_purchase_child`,`tbl_purchase_master`,`tbl_vendor`,`tbl_item` WHERE 
    (`tbl_vendor`.`Vendor_ID`=`tbl_purchase_master`.`Vendor_ID` AND `tbl_purchase_master`.`PM_ID`
    =`tbl_purchase_child`.`PM_ID` AND `tbl_purchase_child`.`Item_ID`=`tbl_item`.`Item_ID` AND 
    `Pur_Date` LIKE '%s')  """%(daily)
				print(q)
				res2=select(q)
				if res2:
					result=0
					for i in res2:
						val=i['Tot_amount']
						result=int(result)+int(val)
						data['total_amountss'] = result
					
				data['report']=res2
				session['res']=res2
				r=session['res']
				data['total']=res2	
			elif monthly != "%":
				q="SELECT *  FROM `tbl_purchase_child`,`tbl_purchase_master`,`tbl_vendor`,`tbl_item` WHERE  (`tbl_vendor`.`Vendor_ID`=`tbl_purchase_master`.`Vendor_ID` AND `tbl_purchase_master`.`PM_ID`=`tbl_purchase_child`.`PM_ID` AND `tbl_purchase_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `Pur_Date` LIKE '%s') """%(monthly)
				print(q)
				res=select(q)
				if res:
					result=0
					for i in res:
						val=i['Tot_amount']
						result=int(result)+int(val)
						data['total_amountss'] = result
				data['total']=res			
				data['report']=res
				print(data['total'])
				session['res']=res
				r=session['res']
				
			elif vendor != "%":
				q="SELECT * , sum(Tot_amount) as total_amountss FROM `tbl_purchase_child`,`tbl_purchase_master`,`tbl_vendor`,`tbl_item` WHERE  (`tbl_vendor`.`Vendor_ID`=`tbl_purchase_master`.`Vendor_ID` AND `tbl_purchase_master`.`PM_ID`=`tbl_purchase_child`.`PM_ID` AND `tbl_purchase_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `Vendor_Name` LIKE '%s') group by tbl_purchase_child.PC_ID "%(vendor)
				res=select(q)
				if res:
					result=0
					for i in res:
						val=i['Tot_amount']
						result=int(result)+int(val)
						data['total_amountss'] = result
				data['total']=res

				data['report']=res
				session['res']=res
				r=session['res']
    
			# q="SELECT * FROM `tbl_purchase_child`,`tbl_purchase_master`,`tbl_vendor`,`tbl_item` WHERE (`tbl_vendor`.`Vendor_ID`=`tbl_purchase_master`.`Vendor_ID` AND `tbl_purchase_master`.`PM_ID`=`tbl_purchase_child`.`PM_ID` AND `tbl_purchase_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `Pur_Date` LIKE '%s') OR (`tbl_vendor`.`Vendor_ID`=`tbl_purchase_master`.`Vendor_ID` AND `tbl_purchase_master`.`PM_ID`=`tbl_purchase_child`.`PM_ID` AND `tbl_purchase_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `Pur_Date` LIKE '%s') OR (`tbl_vendor`.`Vendor_ID`=`tbl_purchase_master`.`Vendor_ID` AND `tbl_purchase_master`.`PM_ID`=`tbl_purchase_child`.`PM_ID` AND `tbl_purchase_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `Vendor_Name` LIKE '%s') "%(daily,monthly,vendor)
			# print(q)
			# res=select(q)
			# if res:
			# 	data['report']=res
			# 	session['res']=res
			# 	r=session['res']

	else:
		q="SELECT * FROM `tbl_purchase_child`,`tbl_purchase_master`,`tbl_vendor`,`tbl_item` WHERE `tbl_vendor`.`Vendor_ID`=`tbl_purchase_master`.`Vendor_ID` AND `tbl_purchase_master`.`PM_ID`=`tbl_purchase_child`.`PM_ID` AND `tbl_purchase_child`.`Item_ID`=`tbl_item`.`Item_ID` "
		res=select(q)
		data['report']=res

		q="select sum(Tot_amount) as total_amountss from tbl_purchase_master"
		data['total']=select(q)

  
	
		
		

	return render_template('staff_view_purchase_report.html',data=data)

@staff.route('/staff_purchasereport',methods=['get','post'])
def staff_purchasereport():
	data={}
	
	r=session['res']
	data['r']=r
 


	return render_template('staff_purchasereport.html',data=data)



@staff.route('/report')
def report():

	

	return render_template('report.html')
