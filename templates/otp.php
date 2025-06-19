<?php
session_start();

// Redirect if no OTP exists
if (empty($_SESSION['otp'])) {
    header("Location: sign_in.php");
    exit();
}

// Verify OTP
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if ($_POST['otp'] == $_SESSION['otp']) {
        // Clear OTP after successful verification
        unset($_SESSION['otp']);
        header("Location: home.php");
        exit();
    } else {
        $error = "Invalid OTP!";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>OTP Verification | Annapurna Restaurant</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="../static/Experiment.css">
    <style>
        .otp-container { max-width: 400px; margin: 0 auto; }
    </style>
</head>
<body>
    <div class="healthy-food-section pt-5 pb-5">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-12 col-md-6 col-lg-5">
                    <div class="shadow p-4 mb-3" style="border-radius: 16px; background-color: white;">
                        <h1 class="text-center mb-4">OTP Verification</h1>
                        
                        <?php if (isset($error)): ?>
                            <div class="alert alert-danger"><?php echo $error; ?></div>
                        <?php endif; ?>
                        
                        <p class="text-center">Enter the 6-digit OTP sent to your phone</p>
                        
                        <form method="post">
                            <div class="form-group">
                                <input type="text" class="form-control text-center" name="otp" 
                                       placeholder="123456" maxlength="6" required>
                            </div>
                            <div class="text-center mt-4">
                                <button type="submit" class="btn btn-primary btn-block">Verify</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>