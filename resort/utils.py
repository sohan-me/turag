from django.core.mail import EmailMessage
import os
from html import escape


class Util:
  @staticmethod
  def send_email(data):
    email = EmailMessage(
      subject=data['subject'],
      body=data['body'],
      from_email= 'turagwaterfrontresort5541@gmail.com',
      to=[data['to_email']],

    )
    email.content_subtype = 'html'
    email.send()

  # Email for payment link after booking validation by admin
  @staticmethod
  def send_payment_email(data):
    payment_link = f"https://turagwaterfrontresort.com/make-payment"

    email = EmailMessage(
        subject='Your Room Booking Request at Turag Resort',
        body=f"""
        <html>
                <head>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            background-color: #f4f4f4;
                            padding: 20px;
                        }}
                        .container {{
                            max-width: 600px;
                            background: #ffffff;
                            padding: 20px;
                            margin: 0 auto;
                            border-radius: 8px;
                            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        }}
                        .header {{
                            text-align: center;
                            margin-bottom: 20px;
                        }}
                        .header img {{
                            max-width: 150px;
                        }}
                        .content {{
                            font-size: 16px;
                            line-height: 1.6;
                            color: #333333;
                        }}
                        .footer {{
                            margin-top: 20px;
                            font-size: 14px;
                            text-align: center;
                            color: #B89146;
                        }}
                        ul li strong {{
                            color: #B89146;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="header">
                            <img src="https://i.ibb.co.com/xSML0rg8/logo.png" alt="Turag Resort">
                        </div>
                        <div class="content">
                            <p>Dear {data.get('full_name')},</p>
                            <p>We are pleased to inform you that we have received your room booking request at <strong>Turag Waterfront Resort</strong>.</p>
                            <p><strong>Booking Details:</strong></p>
                            <ul>
                                <li><strong>Booking ID:</strong> {data.get('booking_id')}</li>
                                <li><strong>Room Name:</strong> {data.get('room_title')}</li>
                                <li><strong>Check-in Date:</strong> {data.get('check_in')}</li>
                                <li><strong>Check-out Date:</strong> {data.get('check_out')}</li>
                            </ul>
                            <p>Your booking request has been received. To confirm your reservation, please complete your payment using the following link:</p>
                            <p><a href="{payment_link}" target="_blank" style="color: #B89146; font-weight: bold;">Click here to pay</a></p>
                            <p>Thank you for choosing Turag Waterfront Resort. We look forward to welcoming you soon!</p>
                        </div>
                        <div class="footer">
                            Sincerely, <br>
                            <strong>Turag Waterfront Resort</strong>
                        </div>
                    </div>
                </body>
            </html>
            """,
            from_email='turagwaterfrontresort5541@gmail.com',
            to=[data.get('to_email')],
        )
    email.content_subtype = 'html'
    email.send()




  # Email after booking cancellation by admin
  @staticmethod
  def send_cancellation_email(data):
    payment_link = f"https://turagwaterfrontresort.com/api/make-payment/"

    email = EmailMessage(
        subject='Turag Resort: Important Update on Your Booking Request',
        body=f"""
        <html>
                <head>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            background-color: #f4f4f4;
                            padding: 20px;
                        }}
                        .container {{
                            max-width: 600px;
                            background: #ffffff;
                            padding: 20px;
                            margin: 0 auto;
                            border-radius: 8px;
                            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        }}
                        .header {{
                            text-align: center;
                            margin-bottom: 20px;
                        }}
                        .header img {{
                            max-width: 150px;
                        }}
                        .content {{
                            font-size: 16px;
                            line-height: 1.6;
                            color: #333333;
                        }}
                        .footer {{
                            margin-top: 20px;
                            font-size: 14px;
                            text-align: center;
                            color: #B89146;
                        }}
                        ul li strong {{
                            color: #B89146;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="header">
                            <img src="https://i.ibb.co.com/xSML0rg8/logo.png" alt="Turag Resort">
                        </div>
                        <div class="content">
                          <p>Dear {data.get('full_name')},</p>
                          <p>We regret to inform you that the room you requested at <strong>Turag Waterfront Resort</strong> is currently unavailable for your chosen dates.</p>
                          <p><strong>Booking Details (Requested):</strong></p>
                          <ul>
                              <li><strong>Booking ID:</strong> {data.get('booking_id')}</li>
                              <li><strong>Room Name:</strong> {data.get('room_title')}</li>
                              <li><strong>Check-in Date:</strong> {data.get('check_in')}</li>
                              <li><strong>Check-out Date:</strong> {data.get('check_out')}</li>
                          </ul>
                          <p>We sincerely apologize for any inconvenience this may cause. Due to high demand, the {data.get('room_title')} room is fully booked for your selected period.</p>

                          <p>Please reply to this email or call us at +8801730863933 or +8801730863934 to discuss with other options. We are committed to finding a solution that meets your needs.</p>

                          <p>Thank you for considering Turag Waterfront Resort. We apologize again for the unavailability of your requested room.</p>
                      </div>
                        <div class="footer">
                            Sincerely, <br>
                            <strong>Turag Waterfront Resort</strong>
                        </div>
                    </div>
                </body>
            </html>
            """,
            from_email='turagwaterfrontresort5541@gmail.com',
            to=[data.get('to_email')],
        )
    email.content_subtype = 'html'
    email.send()


  @staticmethod
  def send_transaction_email(data):

    email = EmailMessage(
        subject='Turag Resort: We received your payment.',
        body = f"""
        <html>
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        padding: 20px;
                    }}
                    .container {{
                        max-width: 600px;
                        background: #ffffff;
                        padding: 20px;
                        margin: 0 auto;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }}
                    .header {{
                        text-align: center;
                        margin-bottom: 20px;
                    }}
                    .header img {{
                        max-width: 150px;
                    }}
                    .content {{
                        font-size: 16px;
                        line-height: 1.6;
                        color: #333333;
                    }}
                    .footer {{
                        margin-top: 20px;
                        font-size: 14px;
                        text-align: center;
                        color: #B89146;
                    }}
                    ul li strong {{
                        color: #B89146;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <img src="https://i.ibb.co.com/xSML0rg8/logo.png" alt="Turag Resort">
                    </div>
                    <div class="content">
                        <p>Dear {escape(data.get('full_name', 'Guest'))},</p>
                        <p>We are pleased to inform you that your payment has been successfully received, and your booking at <strong>Turag Waterfront Resort</strong> is now confirmed.</p>
                        <p><strong>Booking Details (Requested):</strong></p>
                        <ul>
                            <li><strong>Booking ID:</strong> {escape(str(data.get('booking_id', 'N/A')))}</li>
                            <li><strong>Transaction ID:</strong> {escape(str(data.get('trans_id', 'N/A')))}</li>
                            <li><strong>Room Name:</strong> {escape(data.get('room_title', 'N/A'))}</li>
                            <li><strong>Paid Amount:</strong> {escape(str(data.get('paid_amount', '0.00')))}</li>
                        </ul>
                        <p>We look forward to welcoming you soon. If you have any special requests or require assistance, please feel free to contact us.</p>
                        <p>For any inquiries, call us at <strong>+8801730863933</strong> or <strong>+8801730863934</strong>.</p>
                        <p>Thank you for choosing <strong>Turag Waterfront Resort</strong>!</p>
                    </div>
                    <div class="footer">
                        Sincerely, <br>
                        <strong>Turag Waterfront Resort</strong>
                    </div>
                </div>
            </body>
        </html>
        """,

        from_email='turagwaterfrontresort5541@gmail.com',
        to=[data.get('to_email')],
        )
    email.content_subtype = 'html'
    email.send()