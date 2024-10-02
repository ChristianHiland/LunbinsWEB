// Send a Click Count For Lunbin
const image = document.getElementById('LUNBIN_IMG');
image.addEventListener('click', () => {
    image.classList.toggle('move-up');
    console.log("Lunbin clicked!");
    setTimeout(LunbinDOWN, 100);
    fetch('/save_clicks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'clickCount=1'
    })
});


function LunbinDOWN() {
    image.classList.remove('move-up');
}