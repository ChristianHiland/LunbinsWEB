// Send a Click Count For Lunbin
const image = document.getElementById('LUNBIN_IMG');
image.addEventListener('click', () => {
    console.log("Lunbin clicked!");
    fetch('/save_clicks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'clickCount=1'
    })
});