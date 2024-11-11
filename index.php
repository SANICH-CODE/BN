<?php
session_start();

// Проверяем наличие данных пользователей
$users = [];
if (file_exists('users.json')) {
    $json_data = file_get_contents('./home/bnteamxyz/server.bn-team.xyz/tg-bot/users.json');
    $users = json_decode($json_data, true);
}

// Обрабатываем форму входа
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['username']) && isset($_POST['password'])) {
        $telegram_id = $_POST['username']; // Использую поле username как Telegram ID
        $password = $_POST['password']; // Пароль

        // Поиск пользователя
        if (isset($users[$telegram_id])) {
            // Проверка пароля
            if ($users[$telegram_id]['password'] === $password) {
                // Успешный вход
                $_SESSION['user'] = $users[$telegram_id];
                header("Location: /profile/");
                exit();
            } else {
                $error_message = "Неверный пароль.";
            }
        } else {
            $error_message = "Неверный UserID.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Вход</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- Добавьте ваш собственный CSS файл здесь -->
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="form-container">
        <span class="arrow" onclick="arrowClick();"><i class="fa fa-arrow-circle-left" aria-hidden="true"></i></span>
        <img src="https://images.unsplash.com/photo-1489703197108-878f05f4b31b?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=943be4a53094e573abf05d8b1f20aced&auto=format&fit=crop&w=1504&q=80" alt="Background image" class="bg">
        <div class="overlay"></div>
        <div class="choose-form">
            <div class="logo">
                <i class="fa fa-snowflake-o" aria-hidden="true"></i>
                <h1>BN <span class="bold">Team</span></h1>
            </div>
            <div class="buttons">
                <a href="#" class="button button-signup" onclick="signUp();">Регистрация</a>
                <a href="#" class="button button-login" onclick="login();">Вход</a>
                <a href="/" class="button button-exit">Назад</a>
            </div>
        </div>
        <div class="login-form form" style="display: block;"> <!-- Убедитесь, что входная форма отображается первой -->
            <div class="form-wrapper">
                <form method="post">
                    <label for="login-username">UserID</label>
                    <input id="login-username" type="username" placeholder="UserID" name="username" pattern=".{3,}" title="UserID должен содержать ikke менее 3 символов" required>
                    <label for="login-password">Пароль</label>
                    <input id="login-password" type="password" placeholder="пароль" name="password" pattern=".{3,}" title="Пароль должен содержать не менее 3 символов" required>
                    <a href="#" class="forgot-password">Забыл?</a>
                    <button type="submit" class="button button-submit">Вход</button>
                </form>
                
                <?php if (isset($error_message)): ?>
                    <p style="color: red;"><?= htmlspecialchars($error_message) ?></p>
                <?php endif; ?>
            </div>
        </div>
        <div class="register-form form" style="display: none;"> <!-- Скрываем форму регистрации -->
            <div class="form-wrapper">
                <form method="post">
                    <label for="signup-id">Регистрация доступна только чеерез телеграм</label>
     
                    
                    <button type="submit" onclick="location.href = 'https://t.me/BelarusNature_bot?start'" class="button button-submit">Регистрация (Telegram)</button>
                </form>
                
            </div>
        </div>
    </div>

    <script>
        function arrowClick() {
            window.history.back(); // Возврат на предыдущую страницу
        }

        function login() {
            document.querySelector('.login-form').style.display = 'block';
            document.querySelector('.register-form').style.display = 'none';
        }

        function signUp() {
            document.querySelector('.login-form').style.display = 'none';
            document.querySelector('.register-form').style.display = 'block';
        }
    </script>
    <script  src="./script.js"></script>
</body>
</html>
