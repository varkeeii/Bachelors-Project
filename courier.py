from flask import *
from database import *

courier=Blueprint('courier',__name__)

@courier.route('/courier_home')
def courier_home():
	
	return render_template('courier_home.html')


@courier.route('/courier_view_courier_item',methods=['get','post'])
def courier_view_courier_item():
	data={}
	cid=session['coid']
	q="select * from `tbl_cart_master`,`tbl_cart_child`,`tbl_customer`,`tbl_item`,`tbl_delivery`,`tbl_payment` where `tbl_cart_master`.`CM_ID` = `tbl_cart_child`.`CM_ID` and `tbl_cart_master`.`Cust_ID`=`tbl_customer`.`Cust_ID` and `tbl_cart_child`.`Item_ID`=`tbl_item`.`Item_ID` and `tbl_cart_master`.`CM_ID`=`tbl_payment`.CM_ID and `tbl_payment`.`Payment_ID`=`tbl_delivery`.`Payment_ID` and `Cart_Status`='dispatch' AND tbl_delivery.Cour_ID='%s'"%(session['coid'])
	print(q)
	res=select(q)
	data['view']=res
	

	if 'action' in request.args:
		action=request.args['action']
		omid=request.args['omid']
	else:
		action=None

	if action=='accept':
		# q="INSERT INTO `tbl_delivery` VALUES (NULL,'%s','%s',CURDATE(),'pickup')"%(omid,cid)
		# insert(q)

		q="UPDATE `tbl_cart_master` SET `Cart_Status`='pickup' WHERE `CM_ID`='%s'"%(omid)
		update(q)
		flash("Couier Accepted")
		return redirect(url_for('courier.courier_home'))
	return render_template('courier_view_courier_item.html',data=data)
@courier.route('/courier_view_pickup_courier',methods=['get','post'])
def courier_view_pickup_courier():
	
	data={}
	q="SELECT * FROM `tbl_customer`,`tbl_item`,`tbl_cart_master`,`tbl_cart_child`,`tbl_delivery` WHERE `tbl_customer`.`Cust_ID`=`tbl_cart_master`.`Cust_ID` AND `tbl_cart_child`.`CM_ID`=`tbl_cart_master`.`CM_ID` AND `tbl_cart_child`.`Item_ID`=`tbl_item`.`Item_ID` AND `tbl_cart_master`.`Cart_Status`='pickup' AND `Cour_ID`='%s'"%(session['coid'])
	res=select(q)
	data['view']=res

	if 'action' in request.args:
		action=request.args['action']
		dil_id=request.args['dil_id']
		omid=request.args['omid']
	else:
		action=None

	if action=='accept':
		q="UPDATE `tbl_cart_master` SET `Cart_Status`='delivered' WHERE `CM_ID`='%s'"%(omid)
		update(q)
		q="UPDATE `tbl_cart_child` SET `delivery_status`='delivered' WHERE `CM_ID`='%s'"%(omid)
		update(q)
		# q="UPDATE `tbl_delivery` SET `status`='delivered' WHERE `Delivery_ID`='%s'"%(dil_id)
		# update(q)
		return redirect(url_for('courier.courier_home'))
	return render_template('courier_view_pickup_courier.html',data=data)