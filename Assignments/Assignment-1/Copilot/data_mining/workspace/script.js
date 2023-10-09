document.getElementById('get-songs-button').addEventListener('click', function() {
    var genre = document.getElementById('genre-select').value;
    if (genre) {
        getSongs(genre);
    } else {
        alert('Please select a genre');
    }
});

function getSongs(genre) {
    // Replace with the URL of the Last.fm API
    var apiUrl = 'http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=' + genre + '&api_key=	ab50758b73ea3a4c5bedc98fbfb0e647&format=json';

    fetch(apiUrl)
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            displaySongs(data.tracks.track);
        })
        .catch(function(error) {
            console.error('Error:', error);
        });
}

function displaySongs(tracks) {
    var songList = document.getElementById('song-list');
    songList.innerHTML = '';

    tracks.forEach(function(track) {
        var trackDiv = document.createElement('div');
        trackDiv.textContent = track.name + ' by ' + track.artist.name;
        songList.appendChild(trackDiv);
    });
}
