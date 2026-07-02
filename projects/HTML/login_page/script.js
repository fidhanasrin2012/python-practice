function showPassword() {

    let password = document.getElementById("password");

    if (password.type === "password") {
        password.type = "text";
    }
    else {
        password.type = "password";
    }

}

function validateLogin() {

    let username = document.getElementById("username").value.trim();
    let password = document.getElementById("password").value.trim();

    if (username === "" || password === "") {

        alert("Please fill all fields.");
        return false;

    }

    alert("Login Successful!");

    return true;

}