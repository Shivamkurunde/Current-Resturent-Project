import random
import string
import os
from flask import current_app
from flask_mail import Mail, Message
from models import db, OTP

class OTPService:
    def __init__(self, mail):
        self.mail = mail
    
    def generate_otp(self, length=6):
        """Generate a random numeric OTP"""
        return ''.join(random.choices(string.digits, k=length))
    
    def create_otp(self, email):
        """Create and store OTP in database"""
        # Delete any existing unused OTPs for this email
        existing_otps = OTP.query.filter_by(email=email, is_used=False).all()
        for otp in existing_otps:
            db.session.delete(otp)
        
        # Generate new OTP
        otp_code = self.generate_otp()
        expiry_minutes = int(os.getenv('OTP_EXPIRY_MINUTES', 5))
        
        # Create OTP record
        new_otp = OTP(email=email, otp_code=otp_code, expiry_minutes=expiry_minutes)
        db.session.add(new_otp)
        db.session.commit()
        
        return otp_code
    
    def send_otp_email(self, email, otp_code):
        """Send OTP via email"""
        try:
            restaurant_name = os.getenv('RESTAURANT_NAME', 'Annpurana Pure Veg Hotel')
            sender_name = os.getenv('SENDER_NAME', 'Shivam')
            
            subject = f"Your OTP for {restaurant_name}"
            
            html_body = f"""
            <html>
            <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
                <div style="text-align: center; background-color: #f8f9fa; padding: 20px; border-radius: 10px;">
                    <h2 style="color: #28a745;">{restaurant_name}</h2>
                    <h3 style="color: #333;">Email Verification</h3>
                    
                    <p style="color: #666; font-size: 16px;">
                        Welcome to {restaurant_name}! Please use the following OTP to complete your registration:
                    </p>
                    
                    <div style="background-color: #007bff; color: white; padding: 15px; border-radius: 8px; margin: 20px 0;">
                        <h1 style="margin: 0; letter-spacing: 3px;">{otp_code}</h1>
                    </div>
                    
                    <p style="color: #dc3545; font-size: 14px;">
                        <strong>⏰ This OTP will expire in {os.getenv('OTP_EXPIRY_MINUTES', 5)} minutes</strong>
                    </p>
                    
                    <p style="color: #666; font-size: 14px;">
                        If you didn't request this, please ignore this email.
                    </p>
                    
                    <hr style="margin: 30px 0; border: 1px solid #eee;">
                    <p style="color: #999; font-size: 12px;">
                        Best regards,<br>
                        {sender_name}<br>
                        {restaurant_name}
                    </p>
                </div>
            </body>
            </html>
            """
            
            text_body = f"""
            {restaurant_name} - Email Verification
            
            Welcome to {restaurant_name}!
            
            Your OTP for registration: {otp_code}
            
            This OTP will expire in {os.getenv('OTP_EXPIRY_MINUTES', 5)} minutes.
            
            If you didn't request this, please ignore this email.
            
            Best regards,
            {sender_name}
            {restaurant_name}
            """
            
            msg = Message(
                subject=subject,
                recipients=[email],
                html=html_body,
                body=text_body
            )
            
            self.mail.send(msg)
            return True
            
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return False
    
    def verify_otp(self, email, otp_code):
        """Verify OTP code"""
        otp_record = OTP.query.filter_by(
            email=email, 
            otp_code=otp_code, 
            is_used=False
        ).first()
        
        if otp_record and otp_record.is_valid():
            otp_record.is_used = True
            db.session.commit()
            return True
        
        return False
    
    def send_registration_otp(self, email):
        """Complete OTP generation and sending process"""
        otp_code = self.create_otp(email)
        if self.send_otp_email(email, otp_code):
            return True
        return False
