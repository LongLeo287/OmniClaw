const style = document.createElement('style');
style.innerHTML = `
@keyframes logoAnimation {
    from {
        transform: scale(1);
    }
    to {
        transform: scale(1.5);
    }
}

.logo-animate {
    animation: logoAnimation 2s infinite alternate;
}
`;
document.head.appendChild(style);

document.addEventListener("DOMContentLoaded", () => {
    const checkForElement = setInterval(() => {
        const logoImage = document.querySelector('img[alt="LogoWithText"]');
        if (logoImage) {
            logoImage.classList.add('logo-animate');
            clearInterval(checkForElement);
        }
    }, 100);
});
