// const request = require('request');
// const iconv = require('iconv-lite');

// const requestPromise = (url) => {
//     return new Promise((resolve, reject) => {

//     request(url, {encoding: null}, (err, res, body) => {
//             if (res,statusCode == 200) {
//                 const bufs = iconv.decode(body, 'gb2312');
//                 const html = bufs.toString('utf-8');
//                 resolve(html);
//             } else {
//             reject(err)
//             }

//     });
// })
// }

const http = require('https');
const cheerio = require('cheerio');
const fs = require('fs');

// const url = "http://news.baidu.com/"
// var strHtml = '';

// http.get(url, (res) => {
//     res.on("data", (chunk) => {
//         strHtml += chunk;
//     })

//     res.on("end", () => {
//         // console.log(strHtml);
//         var $ = cheerio.load(strHtml)

//         $('#channel-all li').each((item, i) => {
//             // console.log($(i).text());
//             console.log($(i).text());
//             // console.log(i);
//         })
//     })
// })


function saveImage(img_url) {
    http.get(img_url, (res) => {
        res.setEncoding('binary')

        var imageData = '';
        res.on('data', (chunk) => {
            imageData += chunk;
        }).on('end', () => {
                if (!fs.existsSync("./images")) {
                    fs.mkdirSync("./images")
                }

                fs.writeFile("./images/" + Math.random() + '.png', imageData, 'binary', (err) => {
                    if(err) throw err;
                    console.log('保存成功')
                })
            })
    })
}

// saveImage('https://pic2.zhimg.com/v2-c9934e23ffaa2bc24af2c921962b56e2_r.jpg')

const url = 'https://songshuhui.net/shuma/';
http.get(url, (res) => {
    var Html = '';
    res.on('data', (chunk) => {
        Html += chunk;
    }).on('end', () => {
        var $ = cheerio.load(Html)

        var title = $('.listText a').text().trim()
        console.log(title)
        })
})
