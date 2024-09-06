document.querySelector(".navBarButtons").addEventListener("click", (event) => {
    if (event.target.classList.contains("home-button")) {
        window.location.href='/';
    }

    if (event.target.classList.contains("account-creation")) {
        window.location.hred = '/signup'
    }
});