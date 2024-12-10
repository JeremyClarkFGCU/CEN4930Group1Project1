// Initialize script.js
const player = videojs('droneVideo');
player.src({
    src: 'rtmp://localhost:18554/live/mystream', // Your RTMP stream address
    type: 'rtmp/flv'
});

// Initialize Socket.IO
const socket = io('http://localhost:3000'); // Replace with your Python script's address

socket.on('connect', () => {
    console.log('Connected to Python script');
});

socket.on('frame', (data) => {
    const image = new Image();
    image.onload = () => {
        const canvas = document.getElementById('videoCanvas');
        const ctx = canvas.getContext('2d');
        ctx.drawImage(image, 0, 0);

        // ... (Code to send image data to Google Cloud Vision API and draw boxes) ...
    };
    image.src = 'data:image/jpeg;base64,' + data;
});