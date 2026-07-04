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

    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value.trim();

    if (email === "" || password === "") {
        alert("Please fill all fields.");
        return false;
    }

    if (!email.includes("@") || !email.includes(".")) {
        alert("Please enter a valid email address.");
        return false;
    }

    alert("Welcome! Login Successful.");

    return true;
}