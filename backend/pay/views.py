from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import razorpay

# Initialize Razorpay Client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def donate(request):
    if request.method == "POST":
        amount = int(request.POST.get("amount")) * 100  # Convert to paisa

        try:
            order_data = {
                "amount": amount,
                "currency": "INR",
                "payment_capture": 1,
            }
            order = razorpay_client.order.create(data=order_data)
            return JsonResponse(order)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return render(request, "pay.html", {"razorpay_key": settings.RAZORPAY_KEY_ID})

def donate_general(request):
    if request.method == "POST":
        amount = int(request.POST.get("amount")) * 100  # Convert to paisa

        try:
            order_data = {
                "amount": amount,
                "currency": "INR",
                "payment_capture": 1,
            }
            order = razorpay_client.order.create(data=order_data)
            return JsonResponse(order)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return render(request, "donate.html", {"razorpay_key": settings.RAZORPAY_KEY_ID})

@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            # Extract the payment details sent from frontend
            params_dict = {
                "razorpay_order_id": data["razorpay_order_id"],
                "razorpay_payment_id": data["razorpay_payment_id"],
                "razorpay_signature": data["razorpay_signature"]
            }

            # Verify Razorpay Signature
            result = razorpay_client.utility.verify_payment_signature(params_dict)

            if result:
                return JsonResponse({"status": "success", "message": "Payment Verified!"})
            else:
                return JsonResponse({"status": "failure", "message": "Signature verification failed"}, status=400)

        except Exception as e:
            return JsonResponse({"status": "failure", "message": str(e)}, status=400)

    return JsonResponse({"status": "error", "message": "Invalid Request"}, status=400)
