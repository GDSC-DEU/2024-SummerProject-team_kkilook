const cities = ["Busan,KR", "Haeundae,KR", "Sasang,KR", "Suyeong,KR", "Yeonje,KR", "Jung-gu,KR"];
const apiUrl = "http://127.0.0.1:8000/weather/";

function createWeatherCard(data) {
    return `
        <div class="weather-card">
            <img src="http://openweathermap.org/img/wn/${data.icon}@2x.png" alt="${data.description}">
            <div class="temperature">${data.temperature} °C</div>
            <div class="description">${data.description}</div>
            <div class="city">${data.city}</div>
            <div class="details">
                <div>🌬 ${data.wind_speed} m/s</div>
                <div>💧 ${data.humidity}%</div>
            </div>
        </div>
    `;
}

async function loadWeather() {
    const container = document.getElementById('weather-container');
    container.innerHTML = '';

    for (const city of cities) {
        try {
            const response = await fetch(apiUrl + city);
            const data = await response.json();
            container.innerHTML += createWeatherCard(data);
        } catch (error) {
            console.error('Error fetching weather data:', error);
        }
    }
}

loadWeather();
