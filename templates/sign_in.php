<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate required fields
    $required = ['name', 'email', 'phone', 'password'];
    foreach ($required as $field) {
        if (empty($_POST[$field])) {
            die("Error: $field is required!");
        }
    }

    // Store user data
    $_SESSION['user'] = [
        'name' => $_POST['name'],
        'email' => $_POST['email'],
        'phone' => $_POST['phone']
    ];

    // Generate and store OTP (for demo)
    $_SESSION['otp'] = rand(100000, 999999);
    
    // In production: Uncomment to send real OTP via Twilio
    /*
    require_once __DIR__.'/../vendor/autoload.php';
    $twilio = new Twilio\Rest\Client('YOUR_SID', 'YOUR_TOKEN');
    $twilio->messages->create(
        $_POST['phone'],
        [
            'from' => 'YOUR_TWILIO_NUMBER',
            'body' => 'Your OTP is: '.$_SESSION['otp']
        ]
    );
    */

    header("Location: otp.php");
    exit();
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Sign In | Annapurna Restaurant</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="../static/Experiment.css">
    <style>
        .error-message { color: red; margin: 10px 0; }
        .healthy-food-section { min-height: 100vh; }
    </style>
</head>
<body>
    <div id="sectionSignIn" class="healthy-food-section pt-5 pb-5">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-12 col-md-6 col-lg-5">
                    <div class="shadow p-4 mb-3" style="border-radius: 16px; background-color: white;">
                        <h1 class="text-center mb-4">Sign In to Annapurna</h1>
                        
                        <form id="signInForm" method="post" action="sign_in.php">
                            <div class="form-group">
                                <label>Full Name</label>
                                <input type="text" class="form-control" name="name" required>
                            </div>
                            <div class="form-group">
                                <label>Email</label>
                                <input type="email" class="form-control" name="email" required>
                            </div>
                            <div class="form-group">
                                <label>Phone Number</label>
                                <input type="tel" class="form-control" name="phone" required>
                            </div>
                            <div class="form-group">
                                <label>Password</label>
                                <input type="password" class="form-control" name="password" required>
                            </div>
                            <div class="text-center mt-4">
                                <button type="submit" class="btn btn-primary btn-block">Sign In</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    
    <script>
        // Client-side validation
        document.getElementById('signInForm').addEventListener('submit', function(e) {
            const phone = document.querySelector('[name="phone"]').value;
            const password = document.querySelector('[name="password"]').value;
            
            if (!/^\d{10,15}$/.test(phone)) {
                alert('Phone must be 10-15 digits');
                e.preventDefault();
            }
            
            if (!/^(?=.*[A-Z])(?=.*[!@#$%^&*]).{6,}$/.test(password)) {
                alert('Password needs 1 uppercase, 1 special character, and 6+ length');
                e.preventDefault();
            }
        });
    </script>
</body>
</html>