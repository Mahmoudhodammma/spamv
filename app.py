from flask import *
import requests,time

app = Flask('name')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/api-v1/Spam/',methods=['GET'])
def home_page():
	num = request.args.get("Number")
	tim = str(time.time()).split('.')[0]
	u= requests.get(f"http://www.legaluk.co/index.php/Home/Public/send_phone_code.html?code_type=reg&itc=20&phone={num}&time={time}")
	if 'تم إرسال رمز التحقق بنجاح' in u.text:
		return jsonify(Status="Successful Send Message",Developer="@H_AMO_DY") 
	else:
		return jsonify(Status="Dont Send Message", Developer="@H_AMO_DY") 

if __name__ =="__main__":
	app.run()
