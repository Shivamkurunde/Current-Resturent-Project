<?php
session_start();

// Set hardcoded credentials
$valid_user = "admin";
$valid_pass = "Shivam705819@12345";

// Handle logout
if (isset($_GET['logout'])) {
    session_unset();
    session_destroy();
    header("Location: index.php");
    exit();
}

// Handle login form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';

    // Server-side validation
    $error = '';
    if (!preg_match("/^[a-zA-Z\s]+$/", $username)) {
        $error = "Username must contain only letters and spaces.";
    } elseif (!preg_match("/^(?=.*[A-Z])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,}$/", $password)) {
        $error = "Password must have at least one capital letter and one special character.";
    } elseif ($username === $valid_user && $password === $valid_pass) {
        $_SESSION['loggedin'] = true;
        $_SESSION['username'] = $username;
        header("Location: home.php");
        exit();
    } else {
        $error = "Invalid username or password!";
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous" />
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    <script src="https://kit.fontawesome.com/1e8988dde9.js" crossorigin="anonymous"></script>

    <link rel="stylesheet" href="/.css">
    <script src="/static/Experiment.js" defer></script>
    <style>
        .error-message {
            color: red;
            font-size: 14px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div id="sectionLogin" class="healthy-food-section pt-5 pb-5">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-12 col-md-6 col-lg-5">
                    <div class="shadow p-4 mb-3" style="border-radius: 16px; background-color: white;">
                        <?php if (!isset($_SESSION['loggedin'])): ?>
                            <h1 class="healthy-food-section-heading text-center mb-4">Login to Annapurana</h1>
                            <?php if (!empty($error)): ?>
                                <p class="error-message text-center"><?php echo $error; ?></p>
                            <?php endif; ?>
                            <form id="loginForm" method="post" action="">
                                <div class="form-group">
                                    <label for="username" class="healthy-food-section-description">Username</label>
                                    <input type="text" class="form-control" id="username" name="username" placeholder="Enter your username" required>
                                </div>
                                <div class="form-group">
                                    <label for="password" class="healthy-food-section-description">Password</label>
                                    <input type="password" class="form-control" id="password" name="password" placeholder="Enter your password" required>
                                </div>
                                <div class="text-center text-white mt-5">
                                    <button type="submit" class="custom-login-button">Login</button>
                                </div>
                            </form>
                            <div class="text-center mt-3 pt-3">
                                <p id="login-page-description">Experience premium quality and <br> authentic tastes with Annapurana Restaurent</p>
                            </div>
                        <?php else: ?>
                            <h1 class="healthy-food-section-heading text-center mb-4">Welcome, <?php echo $_SESSION['username']; ?>!</h1>
                            <p class="text-center">You are successfully logged in.</p>
                            <div class="text-center mt-4">
                                <a href="?logout=true" class="btn btn-danger">Sign Out</a>
                                <a href="home.php" class="btn btn-primary ml-2">Go to Home</a>
                            </div>
                        <?php endif; ?>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Client-side validation (optional, as server-side is now primary)
        document.getElementById("loginForm")?.addEventListener("submit", function(event) {
            let username = document.getElementById("username")?.value.trim();
            let password = document.getElementById("password")?.value;

            // Check username
            if (!/^[a-zA-Z\s]+$/.test(username)) {
                alert("Username must contain only letters and spaces.");
                event.preventDefault();
                return;
            }

            // Check password
            if (!/^(?=.*[A-Z])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,}$/.test(password)) {
                alert("Password must have at least one capital letter and one special character.");
                event.preventDefault();
                return;
            }
        });
    </script>
</body>
</html>