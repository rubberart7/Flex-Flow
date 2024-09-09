const loginForm = document.getElementById("login-form");
const signUpForm = document.getElementById("signup-form");
const switchLogin = document.getElementById("signup-link");
const switchSignUp = document.getElementById("login-link");

switchSignUp.addEventListener("click", () => {
    signUpForm.classList.add("hidden");
    loginForm.classList.remove("hidden");
});

switchLogin.addEventListener("click", () => {
    loginForm.classList.add("hidden");
    signUpForm.classList.remove("hidden");
});