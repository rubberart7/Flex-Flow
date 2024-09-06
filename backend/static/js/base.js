document.querySelector(".navBarButtons").addEventListener("click", (event) => {
    if (event.target.classList.contains("home-button")) {
        window.location.href='/';
    }

    if (event.target.classList.contains("account-creation")) {
        window.location.href = '/signup'
    }

    if (event.target.classList.contains("workout-plans")) {
        window.location.href = '/workout-plans'
    }

    if (event.target.classList.contains("meal-plans")) {
        window.location.href = '/meal-plans'
    }

    if (event.target.classList.contains("exercise-library")) {
        window.location.href = '/exercise-library'
    }
});