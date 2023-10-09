const { getSongs, displaySongs } = require('./script');

test('getSongs function should fetch data from API', () => {
    // Mock fetch function
    global.fetch = jest.fn(() =>
        Promise.resolve({
            json: () => Promise.resolve({ tracks: { track: [] } }),
        })
    );

    getSongs('rock');

    expect(global.fetch).toHaveBeenCalledTimes(1);
    expect(global.fetch).toHaveBeenCalledWith(
        'http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=rock&api_key=YOUR_API_KEY&format=json'
    );
});

test('displaySongs function should create div for each track', () => {
    // Mock document.getElementById function
    document.getElementById = jest.fn(() => {
        return {
            innerHTML: '',
            appendChild: jest.fn(),
        };
    });

    var tracks = [
        { name: 'Song 1', artist: { name: 'Artist 1' } },
        { name: 'Song 2', artist: { name: 'Artist 2' } },
    ];

    displaySongs(tracks);

    expect(document.getElementById).toHaveBeenCalledTimes(1);
    expect(document.getElementById).toHaveBeenCalledWith('song-list');
});
