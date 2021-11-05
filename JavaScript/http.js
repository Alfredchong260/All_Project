const request = require('request');
const iconv = require('iconv-lite');

const requestPromise = (url) => {
    return new Promise((resolve, reject) => {

    request(url, {encoding: null}, (err, res, body) => {
            if (res,statusCode == 200) {
                const bufs = iconv.decode(body, 'gb2312');
                const html = bufs.toString('utf-8');
                resolve(html);
            } else {
            reject(err)
            }

    });
})
}

