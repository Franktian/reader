export function login(username, password) {
    const URL = 'http://192.168.0.13:8000/user/login';
    const REQUEST_OPTIONS = {
        'method': 'POST',
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': JSON.stringify({
            'username': username,
            'password': password
        })
    };

    return fetch(URL, REQUEST_OPTIONS).then(response => {
        return response.json();
    })
}

export function register(username, password) {
    const URL = 'http://192.168.0.13:8000/user/register';
    const REQUEST_OPTIONS = {
        'method': 'POST',
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': JSON.stringify({
            'username': username,
            'password': password
        })
    };

    return fetch(URL, REQUEST_OPTIONS).then(response => {
        return response.json();
    });
}
