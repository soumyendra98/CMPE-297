document.getElementById('get-songs-button').addEventListener('click', handleGenreSelection);

function handleGenreSelection() {
    const genre = document.getElementById('genre-select').value;
    if (genre) {
        fetchSongs(genre).then(songs => {
            displaySongs(songs);
        });
    }
}

function fetchSongs(genre) {
    // This is a placeholder URL. Replace with the actual Spotify API endpoint.
    const url = `https://api.spotify.com/v1/genres/${genre}/songs`;
    return fetch(url).then(response => response.json());
}

function displaySongs(songs) {
    const songList = document.getElementById('song-list');
    songList.innerHTML = '';
    songs.forEach(song => {
        const songItem = document.createElement('div');
        songItem.textContent = song.name;
        songList.appendChild(songItem);
    });
}
