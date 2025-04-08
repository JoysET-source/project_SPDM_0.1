# import os
# from flask import Flask, render_template, request, redirect, url_for
# import stripe
# from dotenv import load_dotenv
#
# load_dotenv()
#
# app = Flask(__name__)
#
# stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
#
# @app.route("/")
# def home():
#     return render_template("index.html")
#
# @app.route("/abbonati")
# def abbonati():
#     return render_template("checkout.html", stripe_public_key=os.getenv("STRIPE_PUBLIC_KEY"))
#
# @app.route("/create-checkout-session", methods=["POST"])
# def create_checkout_session():
#     session = stripe.checkout.Session.create(
#         payment_method_types=['card'],
#         line_items=[{
#             'price': os.getenv("STRIPE_PRICE_ID"),
#             'quantity': 1,
#         }],
#         mode='subscription',
#         success_url=url_for('success', _external=True),
#         cancel_url=url_for('cancel', _external=True),
#         metadata={
#             "email": request.form["email"]
#         }
#     )
#     return redirect(session.url, code=303)
#
# @app.route("/success")
# def success():
#     return "Pagamento completato. Ora puoi accedere."
#
# @app.route("/cancel")
# def cancel():
#     return "Pagamento annullato."
#
# @app.route("/webhook", methods=["POST"])
# def stripe_webhook():
#     payload = request.data
#     sig_header = request.headers.get("Stripe-Signature")
#     endpoint_secret = os.getenv("STRIPE_ENDPOINT_SECRET")
#
#     try:
#         event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
#     except stripe.error.SignatureVerificationError:
#         return "Webhook non verificato", 400
#
#     if event['type'] == 'checkout.session.completed':
#         session = event['data']['object']
#         email = session['metadata']['email']
#         # Salva l'utente nel DB qui
#         print(f"Nuovo abbonato: {email}")
#
#     return '', 200
#
# if __name__ == "__main__":
#     app.run(debug=True)
