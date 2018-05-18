(function (window) {
    let sleep = {};

    /**
     * post function
     * config = {
     *      data:{},
     *      success:func()
     * }
     * */
    sleep.post = function (url, config) {
        let data = new FormData();
        for (let i in config.data) {
            if (config.data.hasOwnProperty(i)) {
                data.append(i, config.data[i]);
            }
        }
        let xhr = new XMLHttpRequest();
        xhr.open('POST', url, true);
        xhr.onreadystatechange = function (e) {
            if (xhr.readyState === 4 && xhr.status === 200) {
                let responseJSON = JSON.parse(xhr.responseText);
                config.success(responseJSON);
            }
        };
        xhr.send(data);
    };
    window.sleep = sleep;
})(window);