(function (window) {
    let sleep = {};
    sleep.fn = {};
    sleep.fn.post = function (url, obj, success) {
        let data = new FormData();
        for (let i in obj) {
            if (obj.hasOwnProperty(i)) {
                data.append(i, obj[i]);
            }
        }
        let xhr = new XMLHttpRequest();
        xhr.open('POST', url, true);
        xhr.onreadystatechange = function (e) {
            if (xhr.readyState === 4 && xhr.status === 200) {
                let responseJSON = JSON.parse(xhr.responseText);
                success(responseJSON);
            }
        };
        xhr.send(data);
    };
    window.sleep = sleep;
})(window);